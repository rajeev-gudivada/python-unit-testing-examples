# Summary

This is an example repo for unit testing in Python.

# Project Setup

Run the following commands to set up the project, run the test suite, and start developing

**NOTE**: This project uses Python3. If Python3 isn't installed, go to [python.org](https://www.python.org/) and install it for your system.

```
git clone https://github.com/aaronlelevier/python-unit-testing-examples.git
cd testing_example

# create and activate virtualenv
python3 -m venv venv
source venv/bin/activate

# install dependencies
pip install -r requirements.txt

# install project as a package (best practice per pytest)
pip install -e .
```

# Run Test Suite

This repo's goal is to demonstrate testing in Python, so the first thing would be to run the test suite. To do so, run this command from the `project directory`:

```
py.test
```

All tests are located in the `tests/` dir.

# License

MIT
