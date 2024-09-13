# password_generator

Description.  
The package `password_generator` is used to:
- Generate strong and secure passwords.
- Customize password length and types of characters (uppercase, digits, special characters).

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install `password_generator`:

```bash
pip install password_generator
```

## Usage

```python
from password_generator import generator
password = generator.generate_password(length=12, use_upper=True, use_digits=True, use_special=True)
print(password)
```

## Author
Mohan

## License
[MIT](https://choosealicense.com/licenses/mit/)
