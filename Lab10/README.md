# Introduction to Regular Expressions (Regex) in Python

Regular expressions (regex) are a powerful tool for working with text strings, allowing you to search, manipulate, and analyze textual data in an extremely flexible way. In Python, regex is supported by the `re` module, which offers several functions for performing advanced operations on strings.

### What is a regex?

A **regex** is a sequence of characters that defines a search pattern. It can be used to:
- Check if a string matches a specific pattern.
- Extract specific parts of a string.
- Replace portions of text based on a pattern.

### Main Functions in the `re` Module

The most common functions in the `re` module include:
- `re.match()`: Searches for a pattern at the beginning of a string.
- `re.search()`: Searches for a pattern anywhere in the string.
- `re.findall()`: Returns all occurrences of a pattern in a list.
- `re.sub()`: Replaces parts of text that match a pattern with another string.

### Using Raw Strings (r'pattern')

In 99% of regex exercises in Python, it is recommended to use **raw strings** when defining a pattern. Raw strings are prefixed with an "r", for example: `r'pattern'`. This prevents special characters like the backslash (`\`) from being interpreted as escape characters, making regex patterns easier to read and eliminating the need to double backslashes (e.g., `\\`).

Example:
```python
import re

# Using a raw string to define the pattern
pattern = r'\d{3}'
text = "My number is 123"
match = re.search(pattern, text)

if match:
    print("Found:", match.group())
Why Use Regex?
Regex is useful when dealing with complex textual data, such as:

Validating formats of emails, phone numbers, postal codes, etc.
Analyzing system logs to extract specific information.
Manipulating strings in various file formats like CSV, XML, or JSON.
In short, regular expressions are a powerful and flexible tool for managing textual data in Python.
```
## Table
![924EC57C-DDFE-4C11-B4B7-41395897D6AA](https://github.com/user-attachments/assets/7b4ef251-d6c6-4a60-9b58-930348d240d5)
![500EB1BC-C006-4BA7-9A17-324527EC160C](https://github.com/user-attachments/assets/b58c2866-f1ef-495b-ae4b-17295301c8d1)
![DCE9C33D-0E85-4A59-BDDE-466439A49114](https://github.com/user-attachments/assets/1149c04d-83e3-4f19-bc68-a90f30558536)

