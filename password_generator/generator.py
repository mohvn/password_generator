from .utils import get_characters
import random

class PasswordGenerator:
    def __init__(self, length=12, use_upper=True, use_digits=True, use_special=True):
        self.length = length
        self.use_upper = use_upper
        self.use_digits = use_digits
        self.use_special = use_special

    def generate(self):
        characters = get_characters(self.use_upper, self.use_digits, self.use_special)
        password = ''.join(random.choice(characters) for _ in range(self.length))
        return password

def generate_password(length=12, use_upper=True, use_digits=True, use_special=True):
    generator = PasswordGenerator(length, use_upper, use_digits, use_special)
    return generator.generate()

