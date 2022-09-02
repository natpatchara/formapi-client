# formapi-client

Github repository for example client of Checkbox and radiobutton labelling API

## Table of contents
* [Table of contents](#Table-of-contents)
* [project structure](#Project-structure)
* [Technologies](#Technologies)
* [Setup](#Setup)
* [Status](#Status)
* [Reference](#Reference)

## Project structure
```
    .
    ├── package.txt             # Text file containing list of additional packages
    ├── requirement.txt         # Text file containing list of requirement libraries
    ├── main.py                 # Main python script for running streamlit application
    └── README.md

```

## Technologies
* python 3.9.7
* streamlit 1.0.0
* opencv-python 4.5.1.48

## Setup
Clone this project then install requirement libraries with following command
```
    >pip install -r requirement.txt
```
Or install to your virtual environment of choice (eg. poetry, conda, etc.)

Then try run following script to check your installation
```
    > python
    >>> import streamlit
    >>> streamlit.__version__
    '1.0.0'
```
if your console return similar output then your installation is finished

## Status
As of writing this markdown file, this project is compatible for small real world usage. Example of such client was used together with API for testing purposes.
Example of some input and output image to such API can be form-restapi repository.

In summary our current features and todo includes:

* features
    * Working script for hosting streamlit client

* todo
    * Improve documentation
    * Intensive testing
    * Optimization

## Reference
* [Streamlit documentation](https://docs.streamlit.io/library/get-started)
