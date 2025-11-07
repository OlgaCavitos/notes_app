# Створити дескриптор, який перевіряє коректність email та кешує результати
import re
from functools import lru_cache


class EmailValidator:
    def __init__(self):
        self._cache = {}

    @staticmethod
    @lru_cache(maxsize=100)
    def _is_valid_email(email: str) -> bool:
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))

    def __get__(self, obj, owner):
        if obj is None:
            return self
        return self._cache[id(obj)]

    def __set__(self, obj, value):
        if not isinstance(value, str):
            raise TypeError('Email must be a string')
        if not self._is_valid_email(value):
            raise ValueError('Invalid email format')

        self._cache[id(obj)] = value

    def __delete__(self, obj):
        del self._cache[id(obj)]


class User:
    email = EmailValidator()

    def __init__(self, email):
        self.email = email


user = User('correct@example.com')
print(f"Valid emil: {user.email}")
try:
    user_invalid = User('correc@texample.com')

    print(f"Valid emil: {user.email}")
except ValueError as e:
    print(f"Error is: {e}")

