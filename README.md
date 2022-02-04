# Mogoca - Mock Google Cloud API & Services

<p align="center">
    <em>Mock Google Cloud API & Services</em>
</p>

[![build](https://github.com/hyahiaoui/mogoca/workflows/Build/badge.svg)](https://github.com/hyahiaoui/mogoca/actions)
[![codecov](https://codecov.io/gh/hyahiaoui/mogoca/branch/main/graph/badge.svg)](https://codecov.io/gh/hyahiaoui/mogoca)
[![Dependabot Status](https://api.dependabot.com/badges/status?host=github&repo=hyahiaoui/mogoca)](https://dependabot.com)
[![PyPI version](https://badge.fury.io/py/mogoca.svg)](https://badge.fury.io/py/mogoca)

---

**Documentation**: <a href="https://hyahiaoui.github.io/mogoca/" target="_blank">https://hyahiaoui.github.io/mogoca/</a>

**Source Code**: <a href="https://github.com/hyahiaoui/mogoca" target="_blank">https://github.com/hyahiaoui/mogoca</a>

---

## Development

### Setup environement

You should have [Pipenv](https://pipenv.readthedocs.io/en/latest/) installed. Then, you can install the dependencies with:

```bash
pipenv install --dev
```

After that, activate the virtual environment:

```bash
pipenv shell
```

### Run unit tests

You can run all the tests with:

```bash
make test
```

Alternatively, you can run `pytest` yourself:

```bash
pytest
```

### Format the code

Execute the following command to apply `isort` and `black` formatting:

```bash
make format
```

## License

This project is licensed under the terms of the MIT license.
