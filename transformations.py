def to_uppercase(text: str) -> str:
    """
    Convert the input text to uppercase.
    """
    return text.upper()

def reverse_string(text: str) -> str:
    """
    Reverse the input string.
    """
    return text[::-1]

def count_vowels(text: str) -> int:
    """
    Count the number of vowels in the input text.
    """
    vowels = 'aeiouAEIOU'
    return sum(1 for char in text if char in vowels)

def remove_spaces(text: str) -> str:
    """
    Remove all spaces from the input text.
    """
    return text.replace(" ", "")

if __name__ == "__main__":
    # Example usage
    sample_text = "Hello, World!"
    print(f"Original: {sample_text}")
    print(f"Uppercase: {to_uppercase(sample_text)}")
    print(f"Reversed: {reverse_string(sample_text)}")
    print(f"Vowel count: {count_vowels(sample_text)}")
    print(f"No spaces: {remove_spaces(sample_text)}")

 Here is the function to convert Celsius to Fahrenheit added to the transformations.py file:

def to_uppercase(text: str) -> str:
    """
    Convert the input text to uppercase.
    """
    return text.upper()

def reverse_string(text: str) -> str:
    """
    Reverse the input string.
    """
    return text[::-1]

def count_vowels(text: str) -> int:
    """
    Count the number of vowels in the input text.
    """
    vowels = 'aeiouAEIOU'
    return sum(1 for char in text if char in vowels)

def remove_spaces(text: str) -> str:
    """
    Remove all spaces from the input text.
    """
    return text.replace(" ", "")

def celsius_to_fahrenheit(celsius: float) -> float:
    """
    Convert Celsius temperature to Fahrenheit.
    """
    return celsius * 1.8 + 32

if __name__ == "__main__":
    # Example usage
    sample_text = "Hello, World!"
    print(f"Original: {sample_text}")
    print(f"Uppercase: {to_uppercase(sample_text)}")
    print(f"Reversed: {reverse_string(sample_text)}")
    print(f"Vowel count: {count_vowels(sample_text)}")
    print(f"No spaces: {remove_spaces(sample_text)}")
    
    # New usage example
    celsius = 100
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius} Celsius = {fahrenheit} Fahrenheit")

 Here is the lowercase conversion function added:

def to_uppercase(text: str) -> str:
    """
    Convert the input text to uppercase.
    """
    return text.upper()

def reverse_string(text: str) -> str:
    """
    Reverse the input string.
    """
    return text[::-1]

def count_vowels(text: str) -> int:
    """
    Count the number of vowels in the input text.
    """
    vowels = 'aeiouAEIOU'
    return sum(1 for char in text if char in vowels)  

def remove_spaces(text: str) -> str:
    """
    Remove all spaces from the input text.
    """
    return text.replace(" ", "")

def celsius_to_fahrenheit(celsius: float) -> float:
    """
    Convert Celsius temperature to Fahrenheit.
    """
    return celsius * 1.8 + 32

def string_to_lowercase(text: str) -> str:
    """
    Convert string to lowercase.
    """
    return text.lower()

if __name__ == "__main__":
    # Example usage
    sample_text = "Hello, World!"
    print(f"Original: {sample_text}")
    print(f"Uppercase: {to_uppercase(sample_text)}")
    print(f"Lowercase: {string_to_lowercase(sample_text)}")
    print(f"Reversed: {reverse_string(sample_text)}")
    print(f"Vowel count: {count_vowels(sample_text)}")
    print(f"No spaces: {remove_spaces(sample_text)}")
    
    # New usage example
    celsius = 100
    fahrenheit = celsius_to_fahrenheit(celsius) 
    print(f"{celsius} Celsius = {fahrenheit} Fahrenheit")

 Here is the integer addition function added:

def to_uppercase(text: str) -> str:
    """
    Convert the input text to uppercase.
    """
    return text.upper()

def reverse_string(text: str) -> str:
    """
    Reverse the input string.
    """
    return text[::-1]

def count_vowels(text: str) -> int:
    """
    Count the number of vowels in the input text.
    """
    vowels = 'aeiouAEIOU'
    return sum(1 for char in text if char in vowels)

def remove_spaces(text: str) -> str:
    """
    Remove all spaces from the input text.
    """
    return text.replace(" ", "")

def celsius_to_fahrenheit(celsius: float) -> float:
    """
    Convert Celsius temperature to Fahrenheit.
    """
    return celsius * 1.8 + 32  

def string_to_lowercase(text: str) -> str:
    """
    Convert string to lowercase.
    """
    return text.lower()

def add_integers(a: int, b: int) -> int:
    """
    Add two integers together.
    """
    return a + b

if __name__ == "__main__":
    # Example usage
    sample_text = "Hello, World!"
    print(f"Original: {sample_text}")
    print(f"Uppercase: {to_uppercase(sample_text)}") 
    print(f"Lowercase: {string_to_lowercase(sample_text)}")
    print(f"Reversed: {reverse_string(sample_text)}")
    print(f"Vowel count: {count_vowels(sample_text)}")
    print(f"No spaces: {remove_spaces(sample_text)}")
    
    # New usage example
    celsius = 100
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius} Celsius = {fahrenheit} Fahrenheit")
    
    # Integer addition example
    x = 5
    y = 10
    sum = add_integers(x, y)
    print(f"{x} + {y} = {sum}")