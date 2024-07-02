# DLL-Injector

[![Downloads](https://img.shields.io/pepy/dt/DLL-Injector)](https://pypi.org/project/DLL-Injector/)
[![Version](https://img.shields.io/pypi/v/DLL-Injector)](https://pypi.org/project/DLL-Injector/)
[![Python Version](https://img.shields.io/pypi/pyversions/DLL-Injector)](https://pypi.org/project/DLL-Injector/)

DLL-Injector is a library that allows injecting DLLs into processes via Python.

## Set up
----
### Install

~~~python
pip install DLL-Injector
~~~

### Upgrade
~~~~python
pip install --upgrade DLL-Injector
~~~~

## Support

If you want to contact me for questions, bugs, or problems or other : lixnew2@gmail.com

## Python version

DLL-Injector was written for Python 3.

## Functions

### Inject a DLL into a process
~~~python
inject(dll_path: str, process_name: str = None, process_pid: int = None)
# Injects a DLL into a process specified by its name or PID.
# NOTE: You must specify at least one of the two arguments (process_name, process_pid).
args = dll_path, process_name (optional), process_pid (optional)
~~~

## Function Documentation

### `inject`
Injects a DLL into a specified process.

#### Arguments:
- `dll_path` (str): The path to the DLL file.
- `process_name` (str, optional): The name of the process to inject the DLL into.
- `process_pid` (int, optional): The process ID of the process to inject the DLL into.
- **WARNING**: At least one of the two arguments (process_name, process_pid) must be specified.

#### Raises:
- `ValueError`: If the DLL path is not specified, does not exist, or is not a valid DLL file.
- `ValueError`: If neither the process name nor the process ID is specified.
- `ValueError`: If the process name is specified but the process does not exist.
- `ValueError`: If the process ID is specified but does not exist.

## License

```text
MIT License 

Copyright (c) 2024 LixNew; lixnew2@gmail.com

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.