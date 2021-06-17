## Tiny Test Hatchery

```
# Note: Install Python 3
# Update pip and install virtualenv (dependency encapsulator) and black (linter; IDE needs to be restarted)

# Note: install Poetry for Linux
# Note: it doesn't matter if you pass it to `python` or `python3`
$: curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

# Note: install Poetry for Windows
$: (Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python
# Note: do NOT update Poetry, it will break itself

$: python get-poetry.py --uninstall
```

```
# Note: `.toml` project name and package have to match (tiny-test-hatchery; tiny_test_hatchery)
$: poetry install  # install all dependencies
```

More info about [poetry](https://github.com/MislavJaksic/Knowledge-Repository/tree/master/Technology/Software/BuildTool/poetry).   

### dist

```
$: pip install dist/tiny_test_hatchery-0.0.1-py3-none.any.whl

$: tiny-test-hatchery
```

### docs

```
$: poetry shell
$: cd docs
# Note: review source/conf.py and source/index.rst
$: make html
# Note: see docs in docs/build/apidocs/index.html
```

### tiny_test_hatchery

```
$: poetry run python ./tiny_test_hatchery/runner.py
```

### tests

```
$: poetry run pytest --durations=0
```

```
$: poetry run pytest --cov=tiny_test_hatchery --cov-report=html tests
#: Note: see coverage report in htmlcov/index.html
```

### poetry.lock

Dependencies, Python version and the virtual environment are managed by `Poetry`.

```
$: poetry search Package-Name
$: poetry add Package-Name[==Package-Version]
```

### pyproject.toml

Define project entry point and metadata.  

### setup.cfg

Configure Python libraries.  

### Linters

```
$: poetry run black .
```

### cProfile

```
$: poetry run python ./tiny_test_hatchery/profiler.py
```

### Build and publish

```
$: poetry build

# Note: get the token from your PiPy account
$: poetry config pypi-token.pypi PyPI-Api-Access-Token
```

```
$: poetry publish --build
```

```
https://pypi.org/project/tiny-test-hatchery/
```
