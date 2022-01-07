# FlakeHell

It's a [Flake8](https://gitlab.com/pycqa/flake8) wrapper to make it cool.

+ [Lint md, rst, ipynb, and more](https://flakehell.github.io/flakehell/parsers.html).
+ [Shareable and remote configs](https://flakehell.github.io/flakehell/config.html#base).
+ [Legacy-friendly](https://flakehell.github.io/flakehell/commands/baseline.html): ability to get report only about new errors.
+ Caching for much better performance.
+ [Use only specified plugins](https://flakehell.github.io/flakehell/config.html#plugins), not everything installed.
+ [Make output beautiful](https://flakehell.github.io/flakehell/formatters.html).
+ [pyproject.toml](https://www.python.org/dev/peps/pep-0518/) support.
+ [Check that all required plugins are installed](https://flakehell.github.io/flakehell/commands/missed.html).
+ [Syntax highlighting in messages and code snippets](https://flakehell.github.io/flakehell/formatters.html#colored-with-source-code).
+ [PyLint](https://github.com/PyCQA/pylint) integration.
+ [Powerful GitLab support](https://flakehell.github.io/flakehell/formatters.html#gitlab).
+ Codes management:
    + Manage codes per plugin.
    + Enable and disable plugins and codes by wildcard.
    + [Show codes for installed plugins](https://flakehell.github.io/flakehell/commands/plugins.html).
    + [Show all messages and codes for a plugin](https://flakehell.github.io/flakehell/commands/codes.html).
    + Allow codes intersection for different plugins.

![output example](../assets/grouped.png)

## Compatibility

FlakeHell supports all flake8 plugins, formatters, and configs. However, FlakeHell has it's own beautiful way to configure enabled plugins and codes. So, options like `--ignore` and `--select` unsupported. You can have flake8 and FlakeHell in one project if you want but enabled plugins should be explicitly specified.

```eval_rst
.. toctree::
    :maxdepth: 1
    :caption: Main Info

    config
    formatters
    plugins
    parsers
    ide
    troubleshooting

.. toctree::
    :maxdepth: 1
    :caption: Commands

    commands/lint
    commands/baseline
    commands/plugins
    commands/codes
    commands/code
    commands/missed
```
