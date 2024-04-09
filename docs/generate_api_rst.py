from collections import defaultdict
from importlib.metadata import Distribution


def get_package_path():
    return Distribution.from_name("reportlab")._path.parent / "reportlab"


def get_modules(path):
    groups = defaultdict(list)
    path_str = str(path).rstrip("/")
    for py_path in path.rglob("*.py"):
        if py_path.stem.startswith("_") and not py_path.stem == "__init__":
            # Internal module.
            continue
        group = str(py_path.parent)[len(path_str) :].lstrip("/").replace("/", ".")
        groups[group].append(py_path.stem)
    return dict(groups)


def write_automodule(group, module, skip_module_name=False):
    path = f"reportlab.{group}"
    if not skip_module_name:
        path += f".{module}"
    if path.endswith("."):
        path = path[:-1]
    if ".." in path:
        path = path.replace("..", ".")
    escaped_path = path.replace(".", "\.")
    underline = "-" * len(escaped_path)

    return f"""
{escaped_path}
{underline}

.. automodule:: {path}
    :members:
    :undoc-members:
"""


def write_rst_file(submodules):
    content = """
API Reference
=============
""".lstrip()

    for group_name in sorted(submodules):
        group = submodules[group_name]
        if "__init__" in group:
            content += write_automodule(
                group=group_name, module="__init__", skip_module_name=True
            )
        for module in sorted(group):
            if module == "__init__":
                continue
            content += write_automodule(
                group=group_name, module=module, skip_module_name=False
            )

    with open("api.rst", mode="wt") as fd:
        fd.write(content)


def main():
    package_path = get_package_path()
    submodules = get_modules(package_path)
    write_rst_file(submodules)


if __name__ == "__main__":
    main()
