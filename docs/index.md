---
layout: default
title: Python Programming Notes
---

## **1. Built-In Data Types**

### **1.1. Numeric**

**Basic operations** can be performed on numbers.

Note that there is **operator precedence**: */ then +- then *left* *right*.

<ins>**Operators**</ins>

* Addition `+`
* Subtraction `-`
* Multiplication `*`
* Division (float) `/`
* Floor division (int, rounded down towards minus infinity) `//`
* Modulus `%`
* Exponent `x ** y`

#### **1.1.1. `int`**

Integers are **whole numbers**. They do not contain a fractional part.

Computations using integers are significantly faster than using floating-point numbers.

Python 3 `int` has **no maximum size**. To store very large values, Python 2 uses `long`, while Python 3 uses `int`.

#### **1.1.2. `float`**

Floats are **real numbers**. They contain a fractional part after the decimal point.

The maximum `float` value on a 64-bit computer is *1.7976931348623157e+308* which means move the decimal point 308 places right.

The minimum `float` value is *2.2250738585072014e-308*, which has 307 zeros before the decimal point.

Python `float` has **52 digits** of precision. For more precise numbers, use `decimal` data type.

#### **1.1.3. `complex`**

Complex numbers contain **a real and an imaginary part**.

### **1.2. Iterator**

### **1.3. Sequence/Iterators**

A sequence is a **set** of items. For example:
* `"Hello World"` contains a set of 11 character items.
* `computer_parts = ["computer", "monitor", "keyboard", "mouse", "mouse mat"]` contains a set of 5 string items.

Each item in a sequence is also a sequence.
For example, `computer_parts` is a sequence, and `"computer"` is a sequence as well.

Because a sequence is **ordered**, we can use indexes to access individual items in the sequence.
For example, `computer_parts[1] = "monitor"`, and `computer_parts[1][0] = "m"`.

Except for range sequence type, all sequence types can be concatenated or multiplied.

#### **1.3.1. `str`**

Strings are **arrays** of bytes representing unicode characters.
However, Python does not have a `character` data type, a single character is simply a string of length 1.

<ins>**String operators**</ins>

* Concatenates strings: `string1 + string2`
* Repeats the string for x times: `string * x`
* Slices the string: `string[x]`
* Range-slices the string: `string[x:y]`
* Range-slices the string with steps: `string[x:y:-1]`
* Checks for membership: `x in string`
* Checks for non-membership: `x not in string`
* Suppresses an escape sequence (raw string): `print(**r**"C:\Users\timbuchalka\notes.txt")`
* Performs string formatting: `%c %s %i %d %u %o %x %X %e %E %f %g %G`
* Formats as f-string (formatted string literal): `print(f"Pi is approximately {22 / 7:12.50f}")`

<ins>**Escape sequences**</ins>

* Newline `\n`
* Ignore newline `\ then newline`
* Backslash `\\`
* Single quote `'`
* Double quote `"`
* Tab `\t`
* Character with 16-bit hex value `\uxxxx`
* Character with 32-bit hex value `\Uxxxxxxxx`

<ins>**Delimiting strings**</ins>

A delimiter is a sequence of one or more characters for specifying the boundary between regions in a string.

* "string" "string"<br>
  `"he's " "probably " "pining " "for the " "fjords"`
* string1, string2 (adds a space in between)<br>
  `string1, string2, string3, string4, string5`
* \ then newline<br>
  `"""This string has been \`<br>
  `split over \`<br>
  `several \`<br>
  `lines"""`
* 2 extra " (adds a newline in between)<br>
  `"""This string has been `<br>
  `split over `<br>
  `several `<br>
  `lines"""`

<ins>**Printing strings and numbers**</ins>

It is better to print a description of what a value is (`str`), before the value itself (e.g. `int`).

Strong typing violation occurs when we attempt to concatenate numbers with strings using `+`,
as the presence of a number instructs Python to attempt addition which fails.

We can concatenate data types with a string either by:
* Coercion via `str()`: `str(number) + "string"`
* Formatting via representation fields: `"{}.format()"`

#### **1.3.2. List**

#### **1.3.3. Tuple**

#### **1.3.4. Range**

This sequence type cannot be concatenated or multiplied.

Usage: start (inclusive), stop(exclusive), step (slicing)
* `range(stop)`
* `range(start, stop)`
* `range(start, stop, step)`


#### **1.3.5. Bytes And Bytearray**

### **1.4. Mapping**

### **1.5. File**

### **1.6. Class**

### **1.7. Exception**

## **2. Program Flow Control**

### **2.1. Blocks And Statements**

Python uses **indentation** to indicate when a new block starts,
instead of using braces {} or `BEGIN` and `END` around code.

### **2.2. `bool`*

Boolean values are either `True` or `False`.

<ins>**Built-in objects that are considered as `False`**</ins>:
* Constants: `None`, `False`
* Zero of any numeric type: `0`, `0.0`, `0j`, `Decimal(0)`, `Fraction(0,1)`
* Empty sequences and collections: `''`, `()`, `[]`, `{}`, `set()`, `range(0)`

<ins>**Comparison operations**</ins>:
* `<`
* `<=`
* `>`
* `>=`
* `==`
* `!=`
* `is` checks whether the objects are the same objects with the same memory location
* `is not` checks whether the objects are different objects

The concept of boolean values are used in `if-elif-else` blocks.

### **2.3. Loops**

A `for` loop works by **iterating over some set of values**, which comes from a `sequence`, such as string, range and list.
The loop will repeat for each item in a **pre-determined** sequence.

The code in the `while` loop will be executed as long as **the condition is true**.
A `while` loop can be used when you **can't determine** in advance how many times you will need to loop.

`continue` statement: stop the current iteration and move on to the next one
`break` statement: jump out of the loop completely

### **2.4. Binary Search**

When you have an **ordered** set of data to search through, you can split the data in half each time
by guessing the **mid-point** between the low and high values: `midpoint = low + (high-low) // 2`

The range of values halves with each guess. This simplifies the process of guessing a number.