---
layout: default
title: Python Programming
---

<h1 align="center">Welcome to Python Programming (Udemy)! 👋</h1>

<p align="center">
<i>Notes written by Rui En</i>
</p>

## 1. Built-In Data Types

### 1.1. Numeric

#### 1.1.1. `int`

Integers are whole numbers. They do not contain a fractional part.

Computations using integers are significantly faster than using floating-point numbers.

Python 3 `int` has no maximum size. To store very large values, Python 2 uses **long**, while Python 3 uses **int**.

#### 1.1.2. `float`

Floats are real numbers. They contain a fractional part after the decimal point.

The maximum `float` value on a 64-bit computer is 1.7976931348623157e+308 which means move the decimal point 308 places right.

The minimum `float` value is 2.2250738585072014e-308, which has 307 zeros before the decimal point.

Python `float` has 52 digits of precision. For more precise numbers, use `decimal` data type.

#### 1.1.3. `complex`

Complex numbers contain a real and an imaginary part.

### 1.2. Iterator

### 1.3. Sequence/Iterators

A sequence is an ordered set of items.

For example:
* `"Hello World"` contains a set of 11 character items.
* `computer_parts = ["computer", "monitor", "keyboard", "mouse", "mouse mat"]` contains a set of 5 string items.

Each item in a sequence is also a sequence.
For example, `computer_parts` is a sequence, and `"computer"` is a sequence as well.

Because a sequence is **ordered**, we can use indexes to access individual items in the sequence.
For example, `computer_parts[1] = "monitor"`, and `computer_parts[1][0] = "m"`.

Except for range sequence type, all sequence types can be concatenated or multiplied.

#### 1.3.1. `str`

Strings are arrays of bytes representing unicode characters.
However, Python does not have a **character** data type, a single character is simply a string of length 1.

<ins>Printing strings and numbers</ins>

It is better to print a description of what a value is (`str`), before the value itself (e.g. `int`).

Strong typing violation occurs when we attempt to concatenate numbers with strings using `+`,
as the presence of a number instructs Python to attempt addition which fails.

We can concatenate data types with a string either by:
* Coersion via `str()`: `str(number) + "string"`
* Formatting via representation fields: `"{}.format()"`

<ins></ins>

* Raw string: `print(**r**"C:\Users\timbuchalka\notes.txt")`
* f-string (formatted string literals): `print(name + f" is {age} years old")`
#### 1.3.2. List

#### 1.3.3. Tuple

#### 1.3.4. Range

This sequence type cannot be concatenated or multiplied.

#### 1.3.5. Bytes And Bytearray

### 1.4. Mapping

### 1.5. File

### 1.6. Class

### 1.7. Exception
