# pippractice
practice making a package installable via pip using [this tutorial](https://packaging.python.org/tutorials/packaging-projects/)

to install:

```bash
pip install -i https://test.pypi.org/simple/ pippractice
```

to use:

```python
>>> import pippractice as pipp
>>> pipp.name
'pippractice '
```







notes for me:

twine error workaround:

```bash
python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```

