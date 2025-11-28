# Undefined Python

A Python implementation of `undefined` value similar to JavaScript.

## Installation

```bash
pip install undefined-python
```

## Usage

```python
from undefined import undefined

if some_value is undefined:
    print("Value is undefined")

# undefined is falsy
if not undefined:
    print("undefined is falsy")
```

## Features
- Singleton pattern - only one instance exists

- Compatible with Python 2.7+ and Python 3.5+

- Falsy in boolean context

- Proper equality checking
