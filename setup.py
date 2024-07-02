from setuptools import setup, find_packages

setup(
    name="DLL-Injector",
    version="1.0.4",
    author="LixNew",
    author_email="lixnew2@gmail.com",
    description="DLL-Injector is a library for injecting DLLs into processes using Python.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/LixNew2/DLL-Injector",
    packages=find_packages("src"),
    package_dir={"": "src"},
    package_data={
        "dll_injector": ["libs/*.dll"]        
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "psutil"
    ],
)