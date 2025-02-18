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



| **Category**                 | **Symbol/Pattern**  | **Description**                                                        | **Example**                                      |
|------------------------------|---------------------|-------------------------------------------------------------------------|--------------------------------------------------|
| **Literal characters**        | cat                 | Matches exactly the specified text.                                     | cat matches "cat".                              |
| **Metacharacters**            | .                   | Matches any character except a newline.                                 | a.b matches "acb", "a2b".                       |
|                              | *                   | Zero or more repetitions of the preceding element.                       | a*b matches "b", "ab", "aaab".                  |
|                              | +                   | One or more repetitions of the preceding element.                        | a+b matches "ab", "aaab" (not "b").             |
|                              | ?                   | Zero or one repetition of the preceding element.                         | colou?r matches "color" or "colour".            |
| **Character classes**         | [abc]               | Any character among those specified.                                    | [abc] matches "a", "b", or "c".                 |
|                              | [^abc]              | Any character except those specified.                                   | [^abc] matches "d", "e" (not "a").              |
|                              | [0-9]               | Any numeric digit.                                                      | [0-9] matches "0", "1", "9".                    |
|                              | [a-z]               | Any lowercase letter.                                                   | [a-z] matches "a", "b", "z".                    |
| **Anchors**                   | ^                   | Matches the beginning of a string.                                      | ^cat matches "cat" only at the beginning.       |
|                              | $                   | Matches the end of a string.                                            | cat$ matches "cat" only at the end.             |
| **Groups and options**        | ()                  | Groups characters to create subspaces in patterns.                       | (abc) groups "abc".                             |
|                              | `                    | Represents a logical "or" (pipe).                                       |                                                  |
| **Quantifiers**               | {n}                 | Exactly n repetitions of the preceding element.                          | a{3} matches "aaa".                             |
|                              | {n,m}               | From n to m repetitions of the preceding element.                        | a{2,4} matches "aa", "aaa", "aaaa".             |
| **Backslash and similar**     | \d                  | Any numeric digit (equivalent to [0-9]).                                 | \d matches "0", "1", "9".                       |
|                              | \D                  | Any character that is not a numeric digit.                               | \D matches "a", "z" (not "5").                  |
|                              | \w                  | Any alphanumeric character or underscore (equivalent to [a-zA-Z0-9_]).   | \w matches "a", "9", "_".                        |
|                              | \W                  | Any character that is not alphanumeric or underscore.                   | \W matches "#", "%" (not "a").                 |
|                              | \s                  | Any whitespace character (spaces, tabs, etc.).                           | \s matches " ", "\t".                           |
|                              | \S                  | Any character that is not a whitespace.                                  | \S matches "a", "1" (not " ").                  |
|                              | \b                  | Matches a word boundary.                                                | \bword\b matches "word" as a whole word.        |
|                              | \B                  | Matches a position that is not a word boundary.                          | \Bword matches "password" but not "word" as an isolated word. |
|                              | \1, \2…             | References to captured groups in patterns.                              | (\d{2})-(\d{2})\1 matches "12-34-12".           |
|                              | \\                  | Represents a single backslash.                                          | \\d matches the text "\d" in the string (not a digit). |
