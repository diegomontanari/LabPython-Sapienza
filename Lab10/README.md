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

| Categoria           | Simbolo/Pattern                                                          | Descrizione                                                                    | Esempio                                   |
|---------------------|--------------------------------------------------------------------------|--------------------------------------------------------------------------------|-------------------------------------------|
| Caratteri letterali | cat                                                                      | Corrisponde esattamente al testo indicato.                                     | cat corrisponde a “cat”.                  |
| Metacaratteri       | .                                                                        | Corrisponde a qualsiasi carattere, tranne un ritorno a capo.                   | a.b corrisponde a “acb”, “a2b”.           |
| *                   | Zero o più ripetizioni dell’elemento precedente.                         | a*b corrisponde a “b”, “ab”, “aaab”.                                           |                                           |
| +                   | Una o più ripetizioni dell’elemento precedente.                          | a+b corrisponde a “ab”, “aaab” (non “b”).                                      |                                           |
| ?                   | Zero o una ripetizione dell’elemento precedente.                         | colou?r corrisponde a “color” o “colour”.                                      |                                           |
| Classi di caratteri | [abc]                                                                    | Qualsiasi carattere tra quelli specificati.                                    | [abc] corrisponde a “a”, “b” o “c”.       |
| [^abc]              | Qualsiasi carattere tranne quelli specificati.                           | [^abc] corrisponde a “d”, “e” (non “a”).                                       |                                           |
| [0-9]               | Qualsiasi cifra numerica.                                                | [0-9] corrisponde a “0”, “1”, “9”.                                             |                                           |
| [a-z]               | Qualsiasi lettera minuscola.                                             | [a-z] corrisponde a “a”, “b”, “z”.                                             |                                           |
| Ancore              | ^                                                                        | Corrisponde all’inizio di una stringa.                                         | ^cat corrisponde a “cat” solo all’inizio. |
| $                   | Corrisponde alla fine di una stringa.                                    | cat$ corrisponde a “cat” solo alla fine.                                       |                                           |
| Gruppi e opzioni    | ()                                                                       | Raggruppa i caratteri per creare sottospazi nei pattern.                       | (abc) raggruppa “abc”.                    |
| `                   | `                                                                        | Rappresenta un “o” logico (pipe).                                              |                                           |
| Quantificatori      | {n}                                                                      | Esattamente n ripetizioni dell’elemento precedente.                            | a{3} corrisponde a “aaa”.                 |
| {n,m}               | Da n a m ripetizioni dell’elemento precedente.                           | a{2,4} corrisponde a “aa”, “aaa”, “aaaa”.                                      |                                           |
| Backslash e simili  | \d                                                                       | Qualsiasi cifra numerica (equivale a [0-9]).                                   | \d corrisponde a “0”, “1”, “9”.           |
| \D                  | Qualsiasi carattere che non sia una cifra numerica.                      | \D corrisponde a “a”, “z” (non “5”).                                           |                                           |
| \w                  | Qualsiasi carattere alfanumerico o underscore (equivale a [a-zA-Z0-9_]). | \w corrisponde a “a”, “9”, “_”.                                                |                                           |
| \W                  | Qualsiasi carattere che non sia alfanumerico o underscore.               | \W corrisponde a “#”, “%” (non “a”).                                           |                                           |
| \s                  | Qualsiasi spazio bianco (spazi, tab, ecc.).                              | \s corrisponde a “ ”, “                                                        | ”.                                        |
| \S                  | Qualsiasi carattere che non sia uno spazio bianco.                       | \S corrisponde a “a”, “1” (non “ ”).                                           |                                           |
| \b                  | Corrisponde a un confine di parola.                                      | \bword\b corrisponde a “word” come parola intera.                              |                                           |
| \B                  | Corrisponde a un punto che non è un confine di parola.                   | \Bword corrisponde a “password” ma non a “word” come parola isolata.           |                                           |
| \1, \2…             | Riferimento ai gruppi catturati nei pattern.                             | (\d{2})-(\d{2})\1 corrisponde a “12-34-12” (il gruppo 1 è ripetuto alla fine). |                                           |
| \\                  | Rappresenta un singolo backslash.                                        | \\d corrisponde al testo “\d” nella stringa (non a una cifra).                 |                                           |


