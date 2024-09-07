

 Here are some pytest test cases for the transformations.py module:

```python
import transformations

def test_to_uppercase():
    assert transformations.to_uppercase("hello") == "HELLO"

def test_reverse_string():
    assert transformations.reverse_string("hello") == "olleh"

def test_count_vowels():
    text = "hello"
    assert transformations.count_vowels(text) == 2

def test_remove_spaces():
    text = "hello world" 
    assert transformations.remove_spaces(text) == "helloworld"
