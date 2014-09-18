Django Course
=============

A Django course

for

**everyone**.

## Tooling

### pip

pip is a packager management for Python.
Installation guide [here](http://pip.readthedocs.org/en/latest/installing.html)

Basic usage:

Installing a package:

	pip install Django==1.6.7
	pip install Django>=1.6.5,<=1.6.7

Installing from a file:

	pip install -r requirements.txt

Uninstalling a package:

	pip uninstall Django

Listing installed packages:

	pip freeze
	pip list

## virtualenv

virtualenv is a tool to create isolated Python environments.
Installation guide [here](http://virtualenv.readthedocs.org/en/latest/virtualenv.html#installation)

Basic usage:

Creating a virtualenv:

	virtualenv env

Activating a virtualenv:

	source env/bin/activate

Deactivating a virtualenv:

	deactivate

Removing a virtualenv:

	rm -r env

## Project environment

After having all necessary tools installed you need to install the Django framework.

There is a lot of ways to install Django but the easy way is as follows:

	pip install Django==1.6.7

For the project we have a [requirements file](https://pip.readthedocs.org/en/latest/user_guide.html#requirements-files)

	pip install -r requirements.txt
