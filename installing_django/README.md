# Installing Django

Before we install Django we need learn how to install and use some useful tools to improve our development workflow.

## pip

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

## Django

Now that you have pip and virtualenv you can install Django using pip.
Before using pip you should activate your virtualenv.

    pip install Django==1.6.7

That is it! Now you have Django installed and we are ready to the Django awesomeness.
