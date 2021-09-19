from os import path
from setuptools import setup

ROOT = path.abspath(path.dirname(__file__))

# Get requirements from file
with open(path.join(ROOT, "requirements.txt")) as f:
    requirements = [line.strip() for line in f.readlines() if not line.startswith("#")]

setup(
    name="snowdragon",
    version="1.0",
    description="Automatic snow layer classification from SMP measurements.",
    author="Anonymous Snowflake",
    author_email="90999349+anonymous-snowflake@users.noreply.github.com",
    install_requires=requirements,
    python_requires=">=3.6, <3.7",  # TODO: Check if higher version work as well
)
