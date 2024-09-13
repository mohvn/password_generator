from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="password_generator",
    version="0.0.1",
    author="Mohan",
    author_email="mohan.elias@proton.me",
    description="A simple and customizable password generator",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mohvn/password_generator"
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)
