import shutil
import subprocess
import sys
import tarfile
from pathlib import Path
from tempfile import TemporaryDirectory


def download_sdist(destination: Path) -> Path:
    destination.mkdir(parents=True, exist_ok=True)

    # --no-binary=:all: forces pip to obtain an sdist rather than a wheel.
    subprocess.run(
        [
            sys.executable,
            "-m",
            "pip",
            "download",
            "--no-binary=:all:",
            "--no-deps",
            "--no-cache-dir",
            "--dest",
            destination,
            "reportlab",
        ],
        check=True,
    )

    sdists = list(destination.glob("*.tar.gz"))
    if not sdists:
        raise RuntimeError(f"No source distribution found for {package}")

    return sdists[0]


def find_changes(sdist: Path, destination: Path) -> Path:
    extract_dir = destination / "extracted"
    extract_dir.mkdir()

    if not sdist.name.endswith((".tar.gz", ".tgz", ".tar")):
        raise RuntimeError(f"Unsupported sdist format: {sdist}")

    with tarfile.open(sdist, "r:*") as archive:
        for member in archive.getmembers():
            if Path(member.name).name == "CHANGES.md":
                fileobj = archive.extractfile(member)
                if fileobj is None:
                    raise RuntimeError(f"Cannot read {member.name}")
                return fileobj.read()

    raise FileNotFoundError("CHANGES.md was not present in the source distribution")


def main():
    with TemporaryDirectory() as directory:
        path = Path(directory)

        sdist_path = download_sdist(path)
        changes = find_changes(sdist_path, path)

        Path("CHANGES.md").write_bytes(changes)


if __name__ == "__main__":
    main()
