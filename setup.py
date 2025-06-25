from setuptools import setup, find_packages
import os

version = os.getenv("PACKAGE_VERSION", "0.0.1")

setup(
    name="crawlquest",
    version=version,
    description="Auto GET/POST web scraping helper for Python requests.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Rooam",
    author_email="leewr9@gmail.com",
    url="https://github.com/leewr9/crawlquest",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "requests>=2.25.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
