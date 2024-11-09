class InvalidAgeError(Exception):
    def __init__(self, message):
        super().__init__(message)

class Person:
    def set_age(self, age):
        if age < 0 or age > 120:
            raise InvalidAgeError("Возраст должен быть в диапазоне от 0 до 120.")
        self.age = age

try:
    person = Person()
    person.set_age(-5)  # Здесь вызывается исключение, т.к. возраст некорректен
except InvalidAgeError as e:
    print("Ошибка:", e)
