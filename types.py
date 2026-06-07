def get_full_name(first_name: str, last_name: str) -> str:
    return f"{first_name.capitalize()} {last_name.capitalize()}"


if __name__ == "__main__":
    full_name = get_full_name("john", "doe")
    print(full_name)  # Output: John Doe
