# Code Timestamp

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Languages](#languages)
4. [Installations](#installations)
5. [Usage](#usage)
6. [Run](#run)

## Overview

This script allows a user to set a timestamp on his python project

## Features

- Allows a user to set details about his python project timestamp

## Languages

- Python 3.9.7

## Installations

```shell
git clone https://github.com/favoursyre/python-timestamp.git && cd python-timestamp
```

```shell
pip install colored
pip install pyfiglet
```

## Usage

Instantiating the class

```python
author = "Syre Musk"
projectName = "Code Timestamp"
framework = "Python"
year, month, day, hour, minute, seconds = 2021, 12, 11, 13, 52, 10

codeTimestamp(author, projectName, framework, year, month, day, hour, minute, seconds).display(show = True)
#Note: You can set (show = False), if you don't want it to display
```

## Run

```shell
python code_timestamp.py
```

![Result](https://drive.google.com/uc?export=download&id=1NhdSsuSHCUipPHtX8RihU0y-l4SycPJo)
