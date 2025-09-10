def say_hello(name):
    """
    Function that says hello to a person.
    
    Args:
        name (str): The name of the person to greet
    
    Returns:
        str: A greeting message
    """
    return f"Hello, {name}!"


def main():
    """
    Main function to demonstrate the say_hello function
    """
    # Example usage
    person_name = "World"
    greeting = say_hello(person_name)
    print(greeting)
    
    # Interactive example
    user_name = input("Enter your name: ")
    personal_greeting = say_hello(user_name)
    print(personal_greeting)


if __name__ == "__main__":
    main()
