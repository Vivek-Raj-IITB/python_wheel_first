from setuptools import find_packages, setup

with open("app/README.md", "r") as f:
    long_description = f.read()

setup(
    name="DEEVEK",
    version="0.0.10",
    description="An funtion for boo that generated various types and lengths ids",
    package_dir={"": "app"},
    packages=find_packages(where="app"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Vivek-Raj-IITB/python_wheel_first",
    author="Vivek Raj",
    author_email="vivekraj7571@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    extras_require={
        "dev": ["pytest>=7.0", "twine>=4.0.2", "curses-2048" ],
    },
    python_requires=">=3.10",
)
