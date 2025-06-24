from setuptools import setup, find_packages

setup(
    name="crawlquest",
    version="0.1.0",
    description="Auto GET/POST web scraping helper for Python requests.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Rooam",
    author_email="leewr9@gmail.com",
    url="https://github.com/leewr9/crawlquest",
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=[
        "requests>=2.25.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
