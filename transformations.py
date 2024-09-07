 Here is the updated transformations.py file with the new add function:

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

def add(a: int, b: int) -> int:
    """
    Add two integers together.
    """
    return a + b

if __name__ == "__main__":
    # Example usage
    sample_text = "Hello, World!"
    print(f"Original: {sample_text}")
    print(f"Uppercase: {to_uppercase(sample_text)}")
    print(f"Reversed: {reverse_string(sample_text)}")
    print(f"Vowel count: {count_vowels(sample_text)}")
    print(f"No spaces: {remove_spaces(sample_text)}")
    print(f"2 + 3 = {add(2, 3)}")