# airflow-stubs

[![PyPI - Version](https://img.shields.io/pypi/v/airflow-stubs.svg)](https://pypi.org/project/airflow-stubs)

-----

## Table of Contents

- [airflow-stubs](#airflow-stubs)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Introduction](#introduction)
  - [Motivation](#motivation)
  - [Notes on regenerating](#notes-on-regenerating)
  - [License](#license)

## Installation

```console
pip install airflow-stubs
```

## Introduction

This is not meant to improve the type hints of Airflow. Instead it's meant to offer some basic type hints when Airflow is not installed.

Lots of stuff is broken. Use at your own risk.

## Motivation

Airflow has lots of dependencies.
I want to be able to run it via Docker Compose as in [simple-airflow](https://github.com/maresb/simple-airflow) without installing it in my project.
I do however want to define DAGs in my project that use [`@task.docker`](https://airflow.apache.org/docs/apache-airflow/stable/tutorial/taskflow.html#dependency-separation-using-docker-operator).
Installing the stubs alleviates some of the errors from not having Airflow installed in my environment.

## Notes on regenerating

```bash
rm -rf dist
docker run -it --name generate-airflow-stubs -v "$(pwd)/generate-stubs-in-container.sh:/generate-stubs-in-container.sh:ro" apache/airflow bash /generate-stubs-in-container.sh
docker cp generate-airflow-stubs:/home/airflow/out/airflow .
docker rm generate-airflow-stubs
rm -rf airflow-stubs
mv airflow airflow-stubs
python -m build .
```

In order to render `airflow.models.dag` I had to patch
[`get_members`](https://github.com/python/mypy/blob/5db161ffbfd7d9cdd837410cd5d581c0ba597623/mypy/stubgenc.py#L475-L488)
in mypy in order to retry on `RuntimeError: dictionary changed size during iteration`.
(I used `try: ... except RuntimeError: return self.get_members(obj)`.)

Publishing to PyPI is manual for now: `twine upload dist/*`.

## License

`airflow-stubs` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
