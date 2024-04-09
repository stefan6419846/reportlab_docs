# Documentation for reportlab

Inofficial API documentation for `reportlab`.

Unfortunately, `reportlab` does not provide any offical detailed API docs at the moment, just user docs. Although there is some configuration, it appears rather outdated and states:

> Sphinx is being used for the automated API references.  We have always been able to make our own documents in PDF, without using other peoples' libraries, and don't want to back away from this. So, the main User Guide will remain in PDF format for now.  However, programmers need API refs online, and we want to learn Sphinx (and use rst2pdf) in due course.

This [dates back to 2010](https://hg.reportlab.com/hg-public/reportlab/log/tip/docs/source/index.rst), so I do not really expect it to change in the near future.

To allow intersphinx from my own code, I decided that generating a custom version of the API docs would be required.
