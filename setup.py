
from setuptools import setup

with open("README.md") as file:
    long_description = file.read()

setup(
    name="pyklu",
    packages=["pyklu"],
    package_data={'': ['**/*.so']},
    version="0.1.0",
    license="GLPL",
    description="Klu Solver Python Interface",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Mabrains",
    author_email="contact@mabrains.com",
    url="https://github.com/mabrains/PyKLU",
    keywords=["python"],
    install_requires=["numpy", "scipy"],
)
