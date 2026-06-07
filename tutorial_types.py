def get_full_name(first_name: str, last_name: str) -> str:
    return f"{first_name.capitalize()} {last_name.capitalize()}"


def get_name_with_age(name: str, age: int) -> str:
    name_with_age = name + " is this old: " + str(age)
    return name_with_age


from typing import Any


def some_function(data: Any) -> None:
    print(f"Received data: {data}")


def say_hi(name: str | None = None):
    if name is None:
        print("Hi, there!")
    else:
        print(f"Hi, {name}!")


class Person:
    def __init__(self, name: str):
        self.name = name


def get_person_name(one_person: Person) -> str:
    return one_person.name


if __name__ == "__main__":
    person = Person("Alice")
    print(get_person_name(person))
