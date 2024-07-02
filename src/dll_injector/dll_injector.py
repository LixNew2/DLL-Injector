"""
DLL-Injector is a library for injecting DLLs into processes using Python.
"""

__copyright__  = """
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
"""

__version__ = '1.0.3'
__title__ = 'DLL-Injector'
__description__ = "DLL-Injector is a library for injecting DLLs into processes using Python."
__autor__ = 'LixNew'
__twitter__ = '@LixNew2'
__url__ = "https://github.com/LixNew2/DLL-Injector"

#Import
import psutil, ctypes, os

#Variables (const)
DLL_INJECTOR = ctypes.WinDLL("libs/dll_injector.dll")
DLL_INJECTOR.InjectDLL.argtypes = [ctypes.c_char_p, ctypes.c_int]
DLL_INJECTOR.restype = ctypes.c_int

#Private Functions
def _get_process_pid(process_name: str) -> int:
    """
    Get the process ID (PID) of a given process name.

    Args:
        process_name (str): The name of the process with its extension.

    Returns:
        int: The process ID (PID) of the process.
        None: If the process does not exist.

    Raises:
        ValueError: If the process does not exist.

    """
    
    for process in psutil.process_iter():
        if process.name() == process_name:
            return process.pid
    
    return None

def _check_process_pid(process_pid: int) -> bool:
    """
    Check if a process with the given PID exists.

    Args:
        process_pid (int): The PID of the process to check.

    Returns:
        bool: True if the process exists, False otherwise.
    """

    return psutil.pid_exists(process_pid)

def _is_dll(dll_path: str) -> bool:
    """
    Check if the given file path is a valid DLL file.

    Args:
        dll_path (str): The path to the DLL file.

    Returns:
        bool: True if the file is a valid DLL file, False otherwise.

    Raises:
        ValueError: If the file path does not end with '.dll' or if the DLL file cannot be read.
    """

    if not dll_path.endswith(".dll"):
        return False
    
    try:
        with open(dll_path, 'rb') as bytesfile:
            signature = bytesfile.read(2)
            return signature == b'MZ'
    except:
        raise ValueError(f"Cannot read this DLL file: {dll_path}")
    
#Public Function
def inject(dll_path : str, process_name : str = None,  process_pid : int = None) -> None:
    """
    Injects a DLL into a specified process.

    Args:
        dll_path (str): The path to the DLL file.
        process_name (str, optional): The name of the process to inject the DLL into. Defaults to None.
        process_pid (int, optional): The process ID of the process to inject the DLL into. Defaults to None.
        WARNING : At least one of the two arguments (process_name, process_pid) must be specified.

    Returns:
        None

    Raises:
        ValueError: If the DLL path is not specified, does not exist, or is not a DLL file.
        ValueError: If neither the process name or the process ID is specified.
        ValueError: If the process name is specified but the process ID does not exist.
        ValueError: If the process ID is specified but does not exist.

    """
    
    if not dll_path: # Check if the DLL path is specified
        raise ValueError("You must specify a DLL path")

    if not os.path.exists(dll_path): # Check if the DLL path exists
        raise ValueError(f"This DLL path does not exist : {dll_path}")

    if not _is_dll(dll_path): # Check if the DLL file is valid
        raise ValueError(f"This is not a DLL file : {dll_path}")
    
    if process_name is None and process_pid is None: # Check if the process name or the process ID is specified
        raise ValueError("You must specify a process name or a process id")
    
    if process_name: # Check if the process name is specified
        pid = _get_process_pid(process_name) # Get the process ID of the process name
        if pid is not None: # Check if the process exists
            DLL_INJECTOR.InjectDLL(dll_path.encode(), pid) # Inject the DLL into the process
        else:
            raise ValueError(f"This process does not exist: {process_name}")
    else: # If the process name is not specified 
        if _check_process_pid(process_pid): # Check if the process ID exists
            DLL_INJECTOR.InjectDLL(dll_path.encode(), process_pid) # Inject the DLL into the process   
        else:
            raise ValueError(f"This process pid does not exist: {process_pid}")
