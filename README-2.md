
# Python Simple Functions

This project includes three simple Python functions:

## 1. Even or Odd
Determines if a given integer is even or odd.

```python
def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"
```
**Example:**
```python
print(even_or_odd(10))  # Output: Even
```

---

## 2. Convert a Number to a String
Converts an integer into its string representation.

```python
def number_to_string(num):
    return str(num)
```
**Example:**
```python
print(number_to_string(123))  # Output: "123"
```

---

## 3. Remove String Spaces
Removes all spaces from a given string.

```python
def no_space(x):
    return x.replace(" ", "")
```
**Example:**
```python
print(no_space("A B C       V W X Y Z"))  
# Output: "ABCVWXYZ"
```

---

## How to Run
1. Save the code into a Python file (e.g., `functions.py`).
2. Run it using Python 3:

```bash
python functions.py
```
