# Boomerang to Insomnia export/import
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django.svg)
![boomerang - version](https://img.shields.io/badge/Boomerang-any-blue.svg)

Convert export JSON file from [Boomerang - SOAP & REST Client](https://chrome.google.com/webstore/detail/boomerang-soap-rest-clien/eipdnjedkpcnlmmdfdkgfpljanehloah) to [Insomnia](https://insomnia.rest/)

## Installation
### Some optional code changes

1. Change workspace name 
	```python
	# change workspace name
	"name": "Boomerang export workspace",
	```
2. Change base environment data  - *insomnia_env_parent*
	```python
	"data": {
				"key": "value"
			}
	```
3. Change custom environment data and name (from "DEV" to your own name)
	```python
	env_data = {
				"key": "value"
			}
	...create_env("DEV"...
	```

### Python script
Run python script.

```sh
$ python boom-to-inso.py
```
You should see *insomnia_import.json* file in root folder.

:heavy_check_mark: Now you can import file into Insomnia.
