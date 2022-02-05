# Mogoca - Mock Google Cloud API & Services

<p align="center">
    <em>In a nutshell, Mogoca is a library that allows your tests to easily mock out GCP Services.</em>
</p>

[![build](https://github.com/hyahiaoui/mogoca/workflows/Build/badge.svg)](https://github.com/hyahiaoui/mogoca/actions)
[![codecov](https://codecov.io/gh/hyahiaoui/mogoca/branch/main/graph/badge.svg)](https://codecov.io/gh/hyahiaoui/mogoca)
[![PyPI version](https://badge.fury.io/py/mogoca.svg)](https://badge.fury.io/py/mogoca)
[![license](https://img.shields.io/github/license/samuelcolvin/pydantic.svg)](https://github.com/samuelcolvin/pydantic/blob/master/LICENSE)

---

**This project is still in early alpha stage.**

---

**Documentation**: <a href="https://hyahiaoui.github.io/mogoca/" target="_blank">https://hyahiaoui.github.io/mogoca/</a>

**Source Code**: <a href="https://github.com/hyahiaoui/mogoca" target="_blank">https://github.com/hyahiaoui/mogoca</a>

---

## Installation

```bash
pip install mogoka
```

## Usage

*In progress*

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

### Available commands

You can check out the available commands, with their documentation, using

```bash
make help
```
or,

```bash
make
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
