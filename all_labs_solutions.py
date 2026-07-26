"""
I2235 – All Labs + TD8 + Dict/Sets Exercises
Solved with explanation comments in code.

How to use:
1) Save this file as: i2235_all_solutions.py
2) Run: python i2235_all_solutions.py
3) Choose from the menu to execute a specific exercise.
"""

import math
import random
import sys
import time
import string
import io
import os
import json
import builtins
import threading
import queue
import inspect
import keyword
import re
from pathlib import Path
from typing import List, Dict, Any, Optional

try:
    import tkinter as tk
    from tkinter import ttk, messagebox, simpledialog, filedialog
except Exception:  # pragma: no cover - tkinter might be unavailable in some environments
    tk = None
    ttk = None
    messagebox = None
    simpledialog = None
    filedialog = None


# ============================================================
# Lab 1 (Exercises 1 → 17)
# Source: I2235 Lab1 :contentReference[oaicite:9]{index=9}
# ============================================================

def lab1_ex1_answer():
    # Code:
    a = 12
    print(a)           # prints 12
    print(type(a))     # prints <class 'int'>
    b = 'good day'
    print(b)           # prints good day
    print(type(b))     # prints <class 'str'>

    # Explanation:
    # - a is an integer => type(a) is int
    # - b is a string => type(b) is str


def lab1_ex2_answer():
    # fval = -1.4e-3 means -1.4 * 10^-3 = -0.0014
    fval = -1.4e-3
    print(fval)  # -0.0014
    # Correct option is: b (-0.0014)


def lab1_ex3_answer():
    # Identify float vs int:
    nums = [2.9, 1e0, 1.0e0, -4, 2012034821, 32., -1e0, -1.0e0, 391, 29e-1, -5.22e25]
    for x in nums:
        # Explanation:
        # - If it contains decimal OR scientific notation => usually float in Python
        # - BUT note: 1e0 is float (1.0), -1e0 is float, etc.
        print(x, type(x))


def lab1_ex4_answer():
    # "3 = y" is invalid in Python because left side must be a variable name.
    # So it causes SyntaxError.
    print("Answer: syntax error (you cannot assign to a literal).")


def lab1_ex5_answer():
    # float = 3 is problematic because it overrides the built-in float type.
    # That can break future conversions like float("3.14").
    float = 3  # bad practice: shadowing built-in name
    print("Assigned float =", float)
    print("Answer: problematic because 'float' is a Python data type.")


def lab1_ex6_answer():
    x = 3
    x = 3.0
    x = '3'
    # Final assignment is a string, so type is str
    print(type(x))  # <class 'str'>


def lab1_ex7_answer():
    a = 22.35e1     # 223.5
    b = int(a)      # int truncates toward zero => 223
    c = float(b)    # 223.0
    print("a =", a)
    print("b =", b)
    print("c =", c)
    # Explanation:
    # - int() removes the decimal part (doesn't round)
    # - float(int_value) becomes x.0


def lab1_ex8_answer():
    x = 'hello'
    x = 'goodbye'  # overwritten
    print('hello', x)  # prints: hello goodbye
    # Explanation: first value is literal 'hello', second is variable x


def lab1_ex9_answer():
    x = 90
    z = 'hello'
    print(x, z)  # prints: 90 hello


def lab1_ex10():
    # Store your name and age in variables and print a sentence
    name = input("Enter your name: ").strip()
    age = int(input("Enter your age: "))

    # f-string makes formatting easy and readable
    print(f"Hello, my name is {name}, and I am {age} years old.")


def lab1_ex11():
    name = input("Enter your name: ").strip()
    birth_year = int(input("Enter your birth year: "))

    # Simple age estimation: current year - birth year
    # (In real life, exact age depends on birthday date.)
    current_year = 2026
    age = current_year - birth_year
    print(f"{name}, your age is approximately {age}.")


def lab1_ex12():
    # Print Twinkle in the exact multi-line format
    print("Twinkle, twinkle, little star,")
    print("How I wonder what you are!")
    print("Up above the world so high,")
    print("Like a diamond in the sky.")
    print("Twinkle, twinkle, little star,")
    print("How I wonder what you are")


def lab1_ex13():
    r = float(input("Enter radius r: "))
    area = math.pi * (r ** 2)
    print("Area =", area)
    # Explanation: area of circle = π r²


def lab1_ex14():
    first = input("First name: ").strip()
    last = input("Last name: ").strip()
    print(last, first)
    # Explanation: reverse order with a space


def lab1_ex15():
    n_str = input("Enter an integer n: ").strip()

    # Convert n, nn, nnn by string repetition then int conversion
    n = int(n_str)
    nn = int(n_str * 2)
    nnn = int(n_str * 3)

    print(n + nn + nnn)
    # Example: n=5 => 5 + 55 + 555 = 615


def lab1_ex16():
    # Print "here document" style string (multi-line)
    print('a string that you "don\'t" have to escape')
    print("This")
    print("is a ....... multi-line")
    print("heredoc string --------> example")


def lab1_ex17():
    r = 6
    volume = (4/3) * math.pi * (r ** 3)
    print("The volume of the sphere is:", volume)
    # Explanation: V = 4/3 π r³


# ============================================================
# Lab 2 (Exercises 1 → 10)
# Source: I2235 Lab2 :contentReference[oaicite:10]{index=10}
# ============================================================

def lab2_ex1():
    c = float(input("Celsius: "))
    f = (c * 9/5) + 32
    print("Fahrenheit:", f)
    # Explanation: classic conversion formula


def lab2_ex2():
    hours = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))
    pay = hours * rate
    print("Pay:", pay)


def lab2_ex3():
    hours = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))

    if hours > 40:
        overtime = hours - 40
        pay = 40 * rate + overtime * rate * 1.5
    else:
        pay = hours * rate

    print("Pay:", pay)
    # Explanation:
    # - First 40 hours normal
    # - Extra hours * 1.5 rate


def lab2_ex4():
    try:
        hours = float(input("Enter Hours: "))
        rate = float(input("Enter Rate: "))
    except ValueError:
        print("Error, please enter numeric input")
        return

    print("Pay:", hours * rate)
    # Explanation: try/except prevents crashing on non-numeric input


def lab2_ex5():
    s = input("Enter score (0.0 to 1.0): ").strip()
    try:
        score = float(s)
    except ValueError:
        print("Bad score")
        return

    if score < 0.0 or score > 1.0:
        print("Bad score")
    elif score >= 0.9:
        print("A")
    elif score >= 0.8:
        print("B")
    elif score >= 0.7:
        print("C")
    elif score >= 0.6:
        print("D")
    else:
        print("F")


def lab2_ex6():
    n = float(input("Enter number: "))
    diff = abs(n - 17)

    if n > 17:
        print(2 * diff)
    else:
        print(diff)

    # Explanation:
    # - abs gives positive difference
    # - if number > 17 => output 2 * difference


def lab2_ex7():
    n = int(input("Enter number: "))
    # Within 100 of 1000 or 2000 means |n-1000| <= 100 OR |n-2000| <= 100
    result = (abs(n - 1000) <= 100) or (abs(n - 2000) <= 100)
    print(result)


def lab2_ex8():
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))

    s = a + b + c
    if a == b == c:
        print(3 * s)
    else:
        print(s)


def lab2_ex9():
    n = int(input("Enter number: "))
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")
    # Explanation: even numbers have remainder 0 when divided by 2


def lab2_ex10():
    ch = input("Enter a letter: ").strip().lower()
    vowels = {'a', 'e', 'i', 'o', 'u'}
    print(ch in vowels)
    # Explanation: membership test in a set is fast & clean


# ============================================================
# Lab 3 (Exercises 1 → 9)
# Source: I2235 Lab3 :contentReference[oaicite:11]{index=11}
# ============================================================

def lab3_ex1_answer():
    # Program calls jane(), fred(), jane()
    # jane prints "ABC", fred prints "Zap"
    print("Answer: ABC Zap ABC")


def computegrade(score: float) -> str:
    # Explanation:
    # - This function returns a grade letter based on score range
    if score < 0.0 or score > 1.0:
        return "Bad score"
    if score >= 0.9:
        return "A"
    if score >= 0.8:
        return "B"
    if score >= 0.7:
        return "C"
    if score >= 0.6:
        return "D"
    return "F"


def lab3_ex2():
    s = input("Enter score: ").strip()
    try:
        score = float(s)
    except ValueError:
        print("Bad score")
        return
    print(computegrade(score))


def triangle_area(base: float, height: float) -> float:
    # Explanation: area of triangle = (base * height) / 2
    return (base * height) / 2


def lab3_ex3():
    base = float(input("Input the base: "))
    height = float(input("Input the height: "))
    print("area =", triangle_area(base, height))


def gcd(a: int, b: int) -> int:
    # Euclidean algorithm:
    # Keep replacing (a,b) by (b, a%b) until b becomes 0
    while b != 0:
        a, b = b, a % b
    return a


def lab3_ex4():
    a = int(input("a: "))
    b = int(input("b: "))
    print(f"GCD of {a} & {b} = {gcd(a, b)}")


def lcm(a: int, b: int) -> int:
    # Explanation:
    # lcm(a,b) = abs(a*b) // gcd(a,b)
    return abs(a * b) // gcd(a, b) if a and b else 0


def lab3_ex5():
    a = int(input("a: "))
    b = int(input("b: "))
    print("LCM =", lcm(a, b))


def lab3_ex6():
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))

    # If any two values are equal => sum becomes 0
    if a == b or a == c or b == c:
        print(0)
    else:
        print(a + b + c)


def lab3_ex7():
    a = int(input("a: "))
    b = int(input("b: "))
    s = a + b

    # If sum is between 15 and 20 inclusive => return 20
    if 15 <= s <= 20:
        print(20)
    else:
        print(s)


def lab3_ex8():
    a = int(input("a: "))
    b = int(input("b: "))
    # True if equal OR sum==5 OR diff==5
    print(a == b or (a + b) == 5 or abs(a - b) == 5)


def lab3_ex9():
    x = input("x: ")
    y = input("y: ")
    # Only add if both are integers
    try:
        xi = int(x)
        yi = int(y)
        print(xi + yi)
    except ValueError:
        print("Both inputs must be integers.")


# ============================================================
# Lab 4 (Exercises 1 → 7)
# Source: I2235 Lab4 :contentReference[oaicite:12]{index=12}
# ============================================================

def lab4_ex1():
    n = int(input("Input a number: "))
    total = n * (n + 1) / 2  # formula for sum 1..n
    print(f"Sum of the first {n} positive integers:", total)


def lab4_ex2():
    n = input("Input a number: ").strip()
    # Sum digits by iterating characters
    s = 0
    for ch in n:
        if ch.isdigit():
            s += int(ch)
    print("The sum of digits is", s)


def lab4_ex3():
    text = input("Enter a string: ")
    target = input("Enter character to count: ")
    count = 0
    for ch in text:
        if ch == target:
            count += 1
    print("Occurrences:", count)


def all_different(seq: List[int]) -> bool:
    # Explanation:
    # If converting to set keeps same length => all unique
    return len(seq) == len(set(seq))


def lab4_ex4():
    raw = input("Enter numbers separated by space: ").split()
    nums = [int(x) for x in raw]
    print(all_different(nums))


def lab4_ex5():
    n = int(input("Enter a number: "))

    # Repeat: n = n - sum_of_digits(n) until n is not positive
    while n > 0:
        digits_sum = sum(int(d) for d in str(n))
        n = n - digits_sum
        print(n)


def common_divisors_count(a: int, b: int) -> int:
    # Explanation:
    # Count integers d that divide both a and b
    g = gcd(a, b)  # any common divisor must divide gcd
    cnt = 0
    for d in range(1, g + 1):
        if g % d == 0:
            cnt += 1
    return cnt


def lab4_ex6():
    a = int(input("a: "))
    b = int(input("b: "))
    print(f"Number of common divisors of {a} and {b}:", common_divisors_count(a, b))


def is_palindrome_number(n: int) -> bool:
    s = str(n)
    return s == s[::-1]


def lab4_ex7():
    n = int(input("Enter a number: "))

    # Repeat reverse-and-add until palindrome
    while not is_palindrome_number(n):
        rev = int(str(n)[::-1])
        n = n + rev
        print(n)


# ============================================================
# Lab 5 (Exercises 1 → 3)
# Source: I2235 Lab5 :contentReference[oaicite:13]{index=13}
# ============================================================

def lab5_ex1():
    s = 'X-DSPAM-Confidence: 0.8475'
    pos = s.find(':')  # find index of colon
    num_str = s[pos + 1:].strip()  # slice after colon + strip spaces/newlines
    value = float(num_str)
    print(value)


def get_word_hint(secret_word: str, guess_word: str) -> str:
    """
    Returns hint string:
    - 'O' uppercase: correct letter in correct position
    - 'o' lowercase: correct letter but wrong position
    - 'x': letter not in secret word
    """
    # Normalize to uppercase to simplify comparisons (as required)
    secret = secret_word.upper()
    guess = guess_word.upper()

    # Build hint char-by-char
    hint = []
    for i in range(5):
        if guess[i] == secret[i]:
            hint.append('O')  # exact match
        elif guess[i] in secret:
            hint.append('o')  # exists elsewhere
        else:
            hint.append('x')  # not found
    return ''.join(hint)


def lab5_ex2():
    words = 'MITTS FLOAT BRICK LIKED DWARF COMMA GNASH ROOMS UNITE BEARS SPOOL ARMOR'.split()
    secret = random.choice(words)

    print("Guess the secret five-letter word:")
    tries = 6

    for _ in range(tries):
        guess = input("> ").strip()
        # Minimal validation: ensure 5 letters (not required, but helps)
        if len(guess) != 5:
            print("Please enter a 5-letter word.")
            continue

        hint = get_word_hint(secret, guess)
        print(hint)

        if hint == "OOOOO":
            print("You won!")
            return

    print(f"The secret word was {secret}. Better luck next time.")


def lab5_ex3():
    # diagStripe animation (50 wide) in an infinite loop
    width = 50
    while True:
        # phase 1: growing O from 0..49
        for o_count in range(0, width):
            dots = width - o_count
            print("O" * o_count + "." * dots)
            time.sleep(0.01)

        # phase 2: shifting dots in front 1..49
        for dot_front in range(1, width):
            o_count = width - dot_front
            print("." * dot_front + "O" * o_count)
            time.sleep(0.01)


# ============================================================
# Lab 6 (Exercises 1 → 3)
# Source: I2235 Lab6 :contentReference[oaicite:14]{index=14}
# ============================================================

def is_pangram(sentence: str) -> bool:
    # Explanation:
    # - Convert to lowercase
    # - Create set of letters in sentence
    # - Check if it contains all a..z
    alphabet = set(string.ascii_lowercase)
    return alphabet.issubset(set(sentence.lower()))


def lab6_ex1():
    s = input("Enter a sentence: ")
    if is_pangram(s):
        print("That sentence is a pangram.")
    else:
        print("That sentence is not a pangram.")


def get_end_coordinates(directions: List[str]) -> List[int]:
    # Coordinates start at (0,0)
    x, y = 0, 0
    for d in directions:
        d = d.upper()
        if d == 'N':
            y += 1
        elif d == 'S':
            y -= 1
        elif d == 'E':
            x += 1
        elif d == 'W':
            x -= 1
        # Ignore invalid directions silently
    return [x, y]


def lab6_ex2():
    directions = []
    while True:
        d = input("Enter direction (N/S/E/W) or blank to stop: ").strip()
        if d == "":
            break
        directions.append(d)

    print(get_end_coordinates(directions))


def combine_two_text_files(file1: str, file2: str, out_file: str) -> None:
    # Explanation:
    # - Read both files
    # - Write combined content into output file
    with open(file1, "r", encoding="utf-8") as f1:
        c1 = f1.read()
    with open(file2, "r", encoding="utf-8") as f2:
        c2 = f2.read()

    with open(out_file, "w", encoding="utf-8") as out:
        out.write(c1)
        out.write("\n")  # optional separator
        out.write(c2)


def lab6_ex3():
    f1 = input("First filename: ").strip()
    f2 = input("Second filename: ").strip()
    out = input("Output filename: ").strip()
    combine_two_text_files(f1, f2, out)
    print("Combined content written to:", out)


# ============================================================
# Lab 7 (Exercises 1 → 4)
# Source: I2235 Lab7 :contentReference[oaicite:15]{index=15}
# ============================================================

def lab7_ex1():
    filename = input("Enter a file name: ").strip()
    counts = {}

    with open(filename, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            # Start with "From " (note the space) as required
            if line.startswith("From "):
                parts = line.split()
                if len(parts) >= 3:
                    day = parts[2]  # third word is day-of-week
                    counts[day] = counts.get(day, 0) + 1

    print(counts)


def lab7_ex2():
    filename = input("Enter file name: ").strip()
    counts = {}

    with open(filename, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            if line.startswith("From "):
                email = line.split()[1]
                counts[email] = counts.get(email, 0) + 1

    print(counts)


def lab7_ex3():
    filename = input("Enter file name: ").strip()
    counts = {}

    with open(filename, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            if line.startswith("From "):
                email = line.split()[1]
                counts[email] = counts.get(email, 0) + 1

    # Find max sender using a "maximum loop" pattern:
    max_email = None
    max_count = None
    for email, c in counts.items():
        if max_count is None or c > max_count:
            max_email = email
            max_count = c

    print(max_email, max_count)


def lab7_ex4():
    filename = input("Enter file name: ").strip()
    counts = {}

    with open(filename, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            if line.startswith("From "):
                email = line.split()[1]
                domain = email.split("@")[1]  # split twice pattern
                counts[domain] = counts.get(domain, 0) + 1

    print(counts)


# ============================================================
# TD8 (Exercises 2 → 7 shown in PDF text)
# Source: TD8 :contentReference[oaicite:16]{index=16}
# ============================================================

def dictdiff(d1: Dict[Any, Any], d2: Dict[Any, Any]) -> Dict[Any, List[Any]]:
    """
    Returns a dict of differences:
    - For each key where values differ, result[key] = [d1_value_or_None, d2_value_or_None]
    - If no differences => {}
    """
    result = {}
    all_keys = set(d1.keys()) | set(d2.keys())

    for k in all_keys:
        v1 = d1.get(k, None)
        v2 = d2.get(k, None)
        if v1 != v2:
            result[k] = [v1, v2]

    return result


def td8_ex2_demo():
    # Just a demo runner for dictdiff
    d1 = {'a': 1, 'b': 2, 'c': 3}
    d2 = {'a': 1, 'b': 2, 'c': 4}
    print(dictdiff(d1, d2))


def odd_lower_even_upper(text: str) -> str:
    """
    Returns string where:
    - odd index characters -> lowercase
    - even index characters -> uppercase
    (Indexing starts at 0, so "even" means positions 0,2,4,...)
    """
    out = []
    for i, ch in enumerate(text):
        if i % 2 == 0:
            out.append(ch.upper())
        else:
            out.append(ch.lower())
    return ''.join(out)


def td8_ex3():
    t = input("Enter text: ")
    print(odd_lower_even_upper(t))


def clean_and_split(text: str, punctuation_to_remove: str) -> List[str]:
    """
    Splits string into words by:
    1) replacing punctuation with spaces
    2) split() on whitespace
    """
    cleaned = text
    for p in punctuation_to_remove:
        cleaned = cleaned.replace(p, ' ')
    return cleaned.split()


# ============================================================
# TD8 – Exercise 5
# Generate all numbers < 100 divisible by 3 in descending order
# ============================================================

def td8_ex5():
    # We want numbers < 100, divisible by 3, descending
    # range(start, stop, step) lets us go backwards
    result = [n for n in range(99, -1, -1) if n % 3 == 0]
    print(result)

    # Explanation:
    # - Start from 99 (largest < 100 divisible by 3)
    # - Step = -1 to go down
    # - Keep only numbers where n % 3 == 0


# ============================================================
# TD8 – Exercise 6
# Nested dictionary from a word
# Example: 'ant' -> {'a': {'n': {'t': None}}}
# ============================================================

def word_to_nested_dict(word: str):
    # Start from the end: innermost value is always None
    nested = None

    # Traverse word backwards
    for ch in reversed(word):
        nested = {ch: nested}

    return nested

def td8_ex6():
    word = input("Enter a word: ").strip()
    print(word_to_nested_dict(word))

    # Explanation:
    # - Build the structure from inside to outside
    # - Each character becomes a key pointing to the previous dict


# ============================================================
# TD8 – Exercise 7
# Nested dictionary for a list of words
# ============================================================

def words_to_nested_dict(words):
    root = {}

    for word in words:
        current = root
        for ch in word:
            # If key does not exist, create empty dict
            if ch not in current:
                current[ch] = {}
            current = current[ch]
        # Last character points to None
        current.clear()
        current.update({None: None})

    return root

def td8_ex7():
    words = input("Enter words separated by space: ").split()
    print(words_to_nested_dict(words))

    # Explanation:
    # - Shared prefixes share the same dictionary path
    # - This is similar to a trie structure


# ============================================================
# Dictionary & Sets – File Encryption
# Source: Dictionary & Sets Exercises :contentReference[oaicite:0]{index=0}
# ============================================================

def encrypt_file(input_file, output_file, codes):
    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()

    encrypted = ""
    for ch in text:
        # Replace character using dictionary if exists
        encrypted += codes.get(ch, ch)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(encrypted)

    # Explanation:
    # - Dictionary maps characters to symbols
    # - Characters not in dictionary stay unchanged


def decrypt_file(input_file, codes):
    # Reverse the dictionary (values -> keys)
    reverse_codes = {v: k for k, v in codes.items()}

    with open(input_file, "r", encoding="utf-8") as f:
        encrypted = f.read()

    decrypted = ""
    for ch in encrypted:
        decrypted += reverse_codes.get(ch, ch)

    print(decrypted)

    # Explanation:
    # - Reverse mapping allows decoding
    # - Print result instead of saving


# ============================================================
# Dictionary & Sets – Unique Words
# ============================================================

def unique_words():
    filename = input("Enter filename: ").strip()
    unique = set()

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            for word in line.split():
                unique.add(word.lower())

    print(unique)

    # Explanation:
    # - set automatically removes duplicates
    # - lower() avoids case-sensitive duplicates


# ============================================================
# Dictionary & Sets – Date Printer
# ============================================================

def date_printer():
    date = input("Enter date (mm/dd/yyyy): ").strip()
    month, day, year = date.split("/")

    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    month_name = months[int(month) - 1]
    print(f"{month_name} {int(day)}, {year}")

    # Explanation:
    # - Split input by '/'
    # - Convert month number to name using list index
# ============================================================
# Main menu to run all exercises


def _prompt_codes() -> Dict[str, str]:
    """
    Ask the user to enter character replacements (source target per line).
    Returns a dictionary suitable for encrypt_file/decrypt_file.
    """
    print("Enter character mappings in the format 'source target'. Leave blank to finish.")
    codes: Dict[str, str] = {}
    while True:
        raw = input("Mapping: ").strip()
        if raw == "":
            break
        parts = raw.split(None, 1)
        if len(parts) != 2:
            print("Please enter two values separated by a space.")
            continue
        src, dest = parts
        codes[src] = dest
    return codes


def encrypt_file_runner():
    """
    Wrapper that prompts for filenames and mappings, then calls encrypt_file.
    """
    input_file = input("Input file to encrypt: ").strip()
    output_file = input("Output file to write: ").strip()
    codes = _prompt_codes()
    if not codes:
        print("No mappings entered; the file will be copied unchanged.")
    encrypt_file(input_file, output_file, codes)
    print(f"Encrypted content written to {output_file}")


def decrypt_file_runner():
    """
    Wrapper that prompts for filename and mappings, then calls decrypt_file.
    """
    input_file = input("Encrypted file to read: ").strip()
    codes = _prompt_codes()
    if not codes:
        print("No mappings entered; the file will be printed unchanged.")
    decrypt_file(input_file, codes)


EXERCISES = [
    {"section": "Lab 1", "label": "Lab 1 - Exercise 1", "func": lab1_ex1_answer, "tags": ["lab1", "basics"]},
    {"section": "Lab 1", "label": "Lab 1 - Exercise 2", "func": lab1_ex2_answer, "tags": ["lab1", "float"]},
    {"section": "Lab 1", "label": "Lab 1 - Exercise 3", "func": lab1_ex3_answer, "tags": ["lab1", "types"]},
    {"section": "Lab 1", "label": "Lab 1 - Exercise 4", "func": lab1_ex4_answer, "tags": ["lab1", "syntax"]},
    {"section": "Lab 1", "label": "Lab 1 - Exercise 5", "func": lab1_ex5_answer, "tags": ["lab1", "types"]},
    {"section": "Lab 1", "label": "Lab 1 - Exercise 6", "func": lab1_ex6_answer, "tags": ["lab1", "types"]},
    {"section": "Lab 1", "label": "Lab 1 - Exercise 7", "func": lab1_ex7_answer, "tags": ["lab1", "math"]},
    {"section": "Lab 1", "label": "Lab 1 - Exercise 8", "func": lab1_ex8_answer, "tags": ["lab1", "strings"]},
    {"section": "Lab 1", "label": "Lab 1 - Exercise 9", "func": lab1_ex9_answer, "tags": ["lab1", "variables"]},
    {"section": "Lab 1", "label": "Lab 1 - Exercise 10", "func": lab1_ex10, "tags": ["lab1", "io"]},
    {"section": "Lab 1", "label": "Lab 1 - Exercise 11", "func": lab1_ex11, "tags": ["lab1", "io"]},
    {"section": "Lab 1", "label": "Lab 1 - Exercise 12", "func": lab1_ex12, "tags": ["lab1", "strings"]},
    {"section": "Lab 1", "label": "Lab 1 - Exercise 13", "func": lab1_ex13, "tags": ["lab1", "math"]},
    {"section": "Lab 1", "label": "Lab 1 - Exercise 14", "func": lab1_ex14, "tags": ["lab1", "strings"]},
    {"section": "Lab 1", "label": "Lab 1 - Exercise 15", "func": lab1_ex15, "tags": ["lab1", "math", "strings"]},
    {"section": "Lab 1", "label": "Lab 1 - Exercise 16", "func": lab1_ex16, "tags": ["lab1", "strings"]},
    {"section": "Lab 1", "label": "Lab 1 - Exercise 17", "func": lab1_ex17, "tags": ["lab1", "math"]},
    {"section": "Lab 2", "label": "Lab 2 - Exercise 1", "func": lab2_ex1, "tags": ["lab2", "math"]},
    {"section": "Lab 2", "label": "Lab 2 - Exercise 2", "func": lab2_ex2, "tags": ["lab2", "math"]},
    {"section": "Lab 2", "label": "Lab 2 - Exercise 3", "func": lab2_ex3, "tags": ["lab2", "math"]},
    {"section": "Lab 2", "label": "Lab 2 - Exercise 4", "func": lab2_ex4, "tags": ["lab2", "io"]},
    {"section": "Lab 2", "label": "Lab 2 - Exercise 5", "func": lab2_ex5, "tags": ["lab2", "conditions"]},
    {"section": "Lab 2", "label": "Lab 2 - Exercise 6", "func": lab2_ex6, "tags": ["lab2", "math"]},
    {"section": "Lab 2", "label": "Lab 2 - Exercise 7", "func": lab2_ex7, "tags": ["lab2", "math"]},
    {"section": "Lab 2", "label": "Lab 2 - Exercise 8", "func": lab2_ex8, "tags": ["lab2", "math"]},
    {"section": "Lab 2", "label": "Lab 2 - Exercise 9", "func": lab2_ex9, "tags": ["lab2", "math"]},
    {"section": "Lab 2", "label": "Lab 2 - Exercise 10", "func": lab2_ex10, "tags": ["lab2", "sets"]},
    {"section": "Lab 3", "label": "Lab 3 - Exercise 1 (answer)", "func": lab3_ex1_answer, "tags": ["lab3", "strings"]},
    {"section": "Lab 3", "label": "Lab 3 - Exercise 2", "func": lab3_ex2, "tags": ["lab3", "grades"]},
    {"section": "Lab 3", "label": "Lab 3 - Exercise 3", "func": lab3_ex3, "tags": ["lab3", "math"]},
    {"section": "Lab 3", "label": "Lab 3 - Exercise 4", "func": lab3_ex4, "tags": ["lab3", "math"]},
    {"section": "Lab 3", "label": "Lab 3 - Exercise 5", "func": lab3_ex5, "tags": ["lab3", "math"]},
    {"section": "Lab 3", "label": "Lab 3 - Exercise 6", "func": lab3_ex6, "tags": ["lab3", "math"]},
    {"section": "Lab 3", "label": "Lab 3 - Exercise 7", "func": lab3_ex7, "tags": ["lab3", "math"]},
    {"section": "Lab 3", "label": "Lab 3 - Exercise 8", "func": lab3_ex8, "tags": ["lab3", "conditions"]},
    {"section": "Lab 3", "label": "Lab 3 - Exercise 9", "func": lab3_ex9, "tags": ["lab3", "io"]},
    {"section": "Lab 4", "label": "Lab 4 - Exercise 1", "func": lab4_ex1, "tags": ["lab4", "math"]},
    {"section": "Lab 4", "label": "Lab 4 - Exercise 2", "func": lab4_ex2, "tags": ["lab4", "strings"]},
    {"section": "Lab 4", "label": "Lab 4 - Exercise 3", "func": lab4_ex3, "tags": ["lab4", "strings"]},
    {"section": "Lab 4", "label": "Lab 4 - Exercise 4", "func": lab4_ex4, "tags": ["lab4", "sets"]},
    {"section": "Lab 4", "label": "Lab 4 - Exercise 5", "func": lab4_ex5, "tags": ["lab4", "loops"]},
    {"section": "Lab 4", "label": "Lab 4 - Exercise 6", "func": lab4_ex6, "tags": ["lab4", "math"]},
    {"section": "Lab 4", "label": "Lab 4 - Exercise 7", "func": lab4_ex7, "tags": ["lab4", "math"]},
    {"section": "Lab 5", "label": "Lab 5 - Exercise 1", "func": lab5_ex1, "tags": ["lab5", "strings"]},
    {"section": "Lab 5", "label": "Lab 5 - Exercise 2", "func": lab5_ex2, "tags": ["lab5", "game"]},
    {"section": "Lab 5", "label": "Lab 5 - Exercise 3 (animation; Ctrl+C to stop)", "func": lab5_ex3, "tags": ["lab5", "animation", "long-running"]},
    {"section": "Lab 6", "label": "Lab 6 - Exercise 1", "func": lab6_ex1, "tags": ["lab6", "strings"]},
    {"section": "Lab 6", "label": "Lab 6 - Exercise 2", "func": lab6_ex2, "tags": ["lab6", "paths"]},
    {"section": "Lab 6", "label": "Lab 6 - Exercise 3", "func": lab6_ex3, "tags": ["lab6", "files"], "needs_file": True},
    {"section": "Lab 7", "label": "Lab 7 - Exercise 1", "func": lab7_ex1, "tags": ["lab7", "files"], "needs_file": True},
    {"section": "Lab 7", "label": "Lab 7 - Exercise 2", "func": lab7_ex2, "tags": ["lab7", "files"], "needs_file": True},
    {"section": "Lab 7", "label": "Lab 7 - Exercise 3", "func": lab7_ex3, "tags": ["lab7", "files"], "needs_file": True},
    {"section": "Lab 7", "label": "Lab 7 - Exercise 4", "func": lab7_ex4, "tags": ["lab7", "files"], "needs_file": True},
    {"section": "TD8", "label": "TD8 - Exercise 2 Demo", "func": td8_ex2_demo, "tags": ["td8", "dict"]},
    {"section": "TD8", "label": "TD8 - Exercise 3", "func": td8_ex3, "tags": ["td8", "strings"]},
    {"section": "TD8", "label": "TD8 - Exercise 5", "func": td8_ex5, "tags": ["td8", "math"]},
    {"section": "TD8", "label": "TD8 - Exercise 6", "func": td8_ex6, "tags": ["td8", "dict"]},
    {"section": "TD8", "label": "TD8 - Exercise 7", "func": td8_ex7, "tags": ["td8", "dict"]},
    {"section": "Dictionary & Sets", "label": "Dictionary & Sets - Encrypt File", "func": encrypt_file_runner, "tags": ["files", "dict", "crypto"], "needs_file": True},
    {"section": "Dictionary & Sets", "label": "Dictionary & Sets - Decrypt File", "func": decrypt_file_runner, "tags": ["files", "dict", "crypto"], "needs_file": True},
    {"section": "Dictionary & Sets", "label": "Dictionary & Sets - Unique Words", "func": unique_words, "tags": ["files", "sets"], "needs_file": True},
    {"section": "Dictionary & Sets", "label": "Dictionary & Sets - Date Printer", "func": date_printer, "tags": ["strings"]},
]

QUESTION_BANK = {
    "Lab 1 - Exercise 1": "Assign a=12 and b='good day', then print their values and types.",
    "Lab 1 - Exercise 2": "Interpret the scientific notation value -1.4e-3 and show its numeric value.",
    "Lab 1 - Exercise 3": "Classify a list of given literals as int or float when printed in Python.",
    "Lab 1 - Exercise 4": "Explain whether the statement '3 = y' is valid Python and why.",
    "Lab 1 - Exercise 5": "Show what happens if you assign float = 3 and why shadowing built-ins is bad.",
    "Lab 1 - Exercise 6": "Given x=3; x=3.0; x='3', determine the final type of x.",
    "Lab 1 - Exercise 7": "Convert 22.35e1 to int then back to float and display each value.",
    "Lab 1 - Exercise 8": "Predict the output of printing 'hello' and the variable x after reassignment.",
    "Lab 1 - Exercise 9": "Print the values of x=90 and z='hello' on one line.",
    "Lab 1 - Exercise 10": "Ask for name and age, then print a formatted introduction sentence.",
    "Lab 1 - Exercise 11": "Ask for name and birth year, estimate age using the current year, and print it.",
    "Lab 1 - Exercise 12": "Print the nursery rhyme 'Twinkle, twinkle, little star' with correct line breaks.",
    "Lab 1 - Exercise 13": "Read a circle radius r and compute its area.",
    "Lab 1 - Exercise 14": "Read first and last name, then output them in reverse order.",
    "Lab 1 - Exercise 15": "Given an integer n, compute n + nn + nnn using string repetition.",
    "Lab 1 - Exercise 16": "Print a multi-line string with quotes without extra escaping.",
    "Lab 1 - Exercise 17": "Compute the volume of a sphere with radius r=6.",
    "Lab 2 - Exercise 1": "Convert a temperature from Celsius to Fahrenheit.",
    "Lab 2 - Exercise 2": "Compute pay given hours worked and hourly rate.",
    "Lab 2 - Exercise 3": "Compute weekly pay with overtime (hours beyond 40 paid at 1.5x).",
    "Lab 2 - Exercise 4": "Repeat the pay calculation but guard against non-numeric input with try/except.",
    "Lab 2 - Exercise 5": "Read a score in [0.0,1.0] and print the corresponding letter grade or 'Bad score'.",
    "Lab 2 - Exercise 6": "Print the absolute difference from 17, doubled if the input is greater than 17.",
    "Lab 2 - Exercise 7": "Check if an integer is within 100 of either 1000 or 2000.",
    "Lab 2 - Exercise 8": "Sum three integers; if all are equal, print triple their sum.",
    "Lab 2 - Exercise 9": "State whether an input integer is even or odd.",
    "Lab 2 - Exercise 10": "Check whether an input letter is a vowel (True/False).",
    "Lab 3 - Exercise 1 (answer)": "Predict the output of a program that calls jane(); fred(); jane().",
    "Lab 3 - Exercise 2": "Prompt for a score, then use computegrade to print the letter grade or 'Bad score'.",
    "Lab 3 - Exercise 3": "Compute the area of a triangle from its base and height.",
    "Lab 3 - Exercise 4": "Read two integers and print their greatest common divisor (GCD).",
    "Lab 3 - Exercise 5": "Read two integers and print their least common multiple (LCM).",
    "Lab 3 - Exercise 6": "Sum three integers; if any two are equal, the result is 0.",
    "Lab 3 - Exercise 7": "Sum two integers, but if the sum is between 15 and 20 inclusive, print 20.",
    "Lab 3 - Exercise 8": "Given two integers, print True if they are equal, their sum is 5, or their difference is 5.",
    "Lab 3 - Exercise 9": "Read two values; if both are integers print their sum, else warn the user.",
    "Lab 4 - Exercise 1": "Compute the sum of the first n positive integers using the formula n*(n+1)/2.",
    "Lab 4 - Exercise 2": "Sum all digit characters inside an input number string.",
    "Lab 4 - Exercise 3": "Count how many times a target character appears in a given string.",
    "Lab 4 - Exercise 4": "Check whether a list of input integers contains all distinct values.",
    "Lab 4 - Exercise 5": "Starting from n, repeatedly subtract the sum of its digits and print each step until non-positive.",
    "Lab 4 - Exercise 6": "Count how many common divisors two integers share.",
    "Lab 4 - Exercise 7": "Repeat reverse-and-add on a number until a palindrome is reached, printing each intermediate value.",
    "Lab 5 - Exercise 1": "Extract the floating-point value from the string 'X-DSPAM-Confidence: 0.8475'.",
    "Lab 5 - Exercise 2": "Implement a five-letter word guessing game that returns O/o/x hints within six tries.",
    "Lab 5 - Exercise 3 (animation; Ctrl+C to stop)": "Produce an endless diagonal stripe ASCII animation; stop with Ctrl+C.",
    "Lab 6 - Exercise 1": "Check whether an input sentence is a pangram containing every letter a-z.",
    "Lab 6 - Exercise 2": "Read compass directions (N/S/E/W) until blank and output the final coordinates from origin.",
    "Lab 6 - Exercise 3": "Ask for two input filenames and an output filename, then write both files' contents into the output.",
    "Lab 7 - Exercise 1": "Read a mailbox file and count how many 'From ' lines occur for each weekday.",
    "Lab 7 - Exercise 2": "Read a mailbox file and count how many messages each sender email appears in.",
    "Lab 7 - Exercise 3": "Read a mailbox file and print the sender with the highest message count.",
    "Lab 7 - Exercise 4": "Read a mailbox file and count how many messages came from each email domain.",
    "TD8 - Exercise 2 Demo": "Show differences between two dictionaries using dictdiff, returning {key: [v1, v2]} for mismatches.",
    "TD8 - Exercise 3": "Return a string with even indices uppercased and odd indices lowercased.",
    "TD8 - Exercise 5": "List all numbers under 100 divisible by 3 in descending order.",
    "TD8 - Exercise 6": "Convert a word into nested dictionaries where each letter points to the next and ends with None.",
    "TD8 - Exercise 7": "Build a nested dictionary (trie-like) representing multiple words that share prefixes.",
    "Dictionary & Sets - Encrypt File": "Prompt for an input/output file and a character mapping, then write the encrypted text.",
    "Dictionary & Sets - Decrypt File": "Prompt for an encrypted file and a mapping, then decode and print the plaintext.",
    "Dictionary & Sets - Unique Words": "Read a file and print the set of unique lowercase words it contains.",
    "Dictionary & Sets - Date Printer": "Convert a date in mm/dd/yyyy format to 'Month day, year'.",
}

ALL_TAGS = sorted({tag for ex in EXERCISES for tag in ex.get("tags", [])})


def _flatten_menu():
    """Return a flat list of (section, label, function, tags, needs_file)."""
    entries = []
    for ex in EXERCISES:
        entries.append(
            (
                ex["section"],
                ex["label"],
                ex["func"],
                ex.get("tags", []),
                ex.get("needs_file", False),
            )
        )
    return entries


PREFS_PATH = Path(__file__).with_name("app_prefs.json")


def _load_prefs() -> Dict[str, Any]:
    defaults = {
        "geometry": "950x600",
        "search": "",
        "tag": "All",
        "needs_file_only": False,
        "last_label": None,
        "recent_files": [],
    }
    try:
        if PREFS_PATH.exists():
            with open(PREFS_PATH, "r", encoding="utf-8") as f:
                stored = json.load(f)
            defaults.update(stored)
    except Exception:
        pass
    return defaults


def _save_prefs(prefs: Dict[str, Any]):
    try:
        with open(PREFS_PATH, "w", encoding="utf-8") as f:
            json.dump(prefs, f, indent=2)
    except Exception:
        pass


def _print_menu(entries):
    """Console-friendly rendering of the menu."""
    print("\n=== Main Menu ===")
    current_section = None
    for idx, (section, label, _) in enumerate(entries, start=1):
        if section != current_section:
            print(f"\n{section}:")
            current_section = section
        print(f"  {idx}) {label}")
    print("  q) Quit")


def main():
    """Text-based menu runner."""
    entries = _flatten_menu()
    while True:
        _print_menu(entries)
        choice = input("Choose an option (or q to quit): ").strip().lower()
        if choice in {"q", "quit", "exit"}:
            break
        try:
            index = int(choice)
        except ValueError:
            print("Please enter a valid number or 'q' to quit.")
            continue
        if index < 1 or index > len(entries):
            print("Option out of range.")
            continue
        _, label, func, _, _ = entries[index - 1]
        print(f"\n--- Running {label} ---")
        try:
            func()
        except Exception as exc:
            print(f"Error while running {label}: {exc}")
        input("\nPress Enter to return to the menu...")


def _remember_file(ctx: "_AppContext", path: str):
    """Track recent files in prefs."""
    if not path:
        return
    recents = ctx.prefs.setdefault("recent_files", [])
    if path in recents:
        recents.remove(path)
    recents.insert(0, path)
    ctx.prefs["recent_files"] = recents[:5]


def _gui_input(prompt: str, ctx: "_AppContext") -> str:
    """
    Replacement for input() using a Tk dialog, executed on the Tk main thread.
    If the prompt looks like a file path request, opens a file picker first.
    """
    if simpledialog is None or ctx.root is None:
        return input(prompt)

    result: Dict[str, str] = {}
    done = threading.Event()
    prompt_lower = prompt.lower()

    def ask():
        chosen = None
        if filedialog and ("file" in prompt_lower or "filename" in prompt_lower):
            chosen = filedialog.askopenfilename(title=prompt)
        if chosen:
            _remember_file(ctx, chosen)
            result["value"] = chosen
            done.set()
            return
        initial = ""
        recents = ctx.prefs.get("recent_files", [])
        if recents and ("file" in prompt_lower or "filename" in prompt_lower):
            initial = recents[0]
        res = simpledialog.askstring("Input", prompt, parent=ctx.root, initialvalue=initial)
        result["value"] = "" if res is None else res
        if os.path.exists(result["value"]):
            _remember_file(ctx, result["value"])
        done.set()

    ctx.root.after(0, ask)
    done.wait()
    return result.get("value", "")


class _TextRedirect:
    """Redirect stdout/stderr to a queue (consumed by the UI thread)."""

    def __init__(self, out_queue: "queue.Queue[tuple]", tag: str):
        self.out_queue = out_queue
        self.tag = tag

    def write(self, msg: str):
        if msg:
            self.out_queue.put((msg, self.tag))

    def flush(self):
        pass


class _AppContext:
    """Hold shared GUI state so we can coordinate threads safely."""

    def __init__(self, root: "tk.Tk", entries: List[tuple], prefs: Optional[Dict[str, Any]] = None):
        self.root = root
        self.entries = entries
        self.filtered_entries = entries
        self.prefs = prefs or {}
        self.output_queue: "queue.Queue[tuple]" = queue.Queue()
        self.output_widget: Optional["tk.Text"] = None
        self.listbox: Optional["tk.Listbox"] = None
        self.runner_thread: Optional[threading.Thread] = None
        self.stop_event = threading.Event()
        self.status_label: Optional["ttk.Label"] = None
        self.header_label: Optional["ttk.Label"] = None
        self.display_map: Dict[int, int] = {}
        self.exiting = False


def _set_status(ctx: _AppContext, text: str):
    """Update status text on the UI thread."""
    if ctx.status_label is None:
        return
    ctx.root.after(0, lambda: ctx.status_label.config(text=text))


def _get_selected_entry(ctx: _AppContext, quiet: bool = False):
    """
    Resolve the currently selected exercise to an (index, section, label, func) tuple.
    Returns None after showing a message if the selection is invalid.
    """
    if ctx.listbox is None:
        return None
    selection = ctx.listbox.curselection()
    if not selection:
        if not quiet:
            messagebox.showinfo("No selection", "Please select an exercise first.")
        return None
    idx = selection[0]
    label_text = ctx.listbox.get(idx)
    if label_text.startswith("["):
        if not quiet:
            messagebox.showinfo("Invalid selection", "Please choose an exercise, not a section header.")
        return None
    if idx not in ctx.display_map:
        if not quiet:
            messagebox.showerror("Error", "Selection mapping failed.")
        return None
    entry_idx = ctx.display_map[idx]
    if entry_idx < 0 or entry_idx >= len(ctx.filtered_entries):
        if not quiet:
            messagebox.showerror("Error", "Selection is out of range.")
        return None
    return (entry_idx, *ctx.filtered_entries[entry_idx])


def _apply_filters(ctx: _AppContext, search_text: str, tag_filter: str, needs_file_only: bool):
    """Filter exercises by text, tag, and file requirement, then refresh the listbox."""
    search_lower = search_text.lower().strip()

    def matches(entry):
        section, label, _, tags, needs_file = entry
        if needs_file_only and not needs_file:
            return False
        if tag_filter and tag_filter != "All":
            if tag_filter not in tags:
                return False
        if search_lower:
            blob = f"{section} {label} {' '.join(tags)}".lower()
            return search_lower in blob
        return True

    ctx.filtered_entries = [e for e in ctx.entries if matches(e)]

    if ctx.listbox:
        ctx.listbox.delete(0, tk.END)
        ctx.display_map.clear()
        current_section = None
        list_index = 0
        for idx, (section, label, _, tags, needs_file) in enumerate(ctx.filtered_entries):
            if section != current_section:
                ctx.listbox.insert(tk.END, f"[{section}]")
                ctx.listbox.itemconfig(tk.END, fg="#a855f7")
                list_index += 1
                current_section = section
            suffix = " 🔒" if needs_file else ""
            ctx.listbox.insert(tk.END, f"{idx + 1}. {label}{suffix}")
            ctx.display_map[list_index] = idx
            list_index += 1


def _drain_output(ctx: _AppContext):
    """Pull text from the queue and append to the output widget (UI thread safe)."""
    if ctx.output_widget is None:
        return
    if ctx.exiting or not ctx.root.winfo_exists():
        return
    try:
        while True:
            msg, tag = ctx.output_queue.get_nowait()
            ctx.output_widget.insert(tk.END, msg, tag)
            ctx.output_widget.see(tk.END)
    except queue.Empty:
        pass
    ctx.root.after(50, lambda: _drain_output(ctx))


def _start_run(ctx: _AppContext):
    """Start the selected exercise in a background thread."""
    if ctx.listbox is None:
        return
    if ctx.runner_thread and ctx.runner_thread.is_alive():
        messagebox.showinfo("Busy", "An exercise is already running. Stop it first.")
        return

    resolved = _get_selected_entry(ctx)
    if resolved is None:
        return
    _, section, label, func, tags, needs_file = resolved
    ctx.prefs["last_label"] = label
    ctx.output_widget.delete("1.0", tk.END)
    ctx.output_queue.put((f"--- Running {label} ---\n\n", "stdout"))
    ctx.stop_event.clear()
    _set_status(ctx, f"Running: {label}")

    def run_func():
        original_input = builtins.input
        original_stdout = sys.stdout
        original_stderr = sys.stderr
        original_sleep = time.sleep
        builtins.input = lambda prompt="": _gui_input(prompt, ctx)
        sys.stdout = _TextRedirect(ctx.output_queue, "stdout")
        sys.stderr = _TextRedirect(ctx.output_queue, "stderr")

        def cooperative_sleep(seconds: float):
            """Sleep in small chunks so we can honor stop requests (helps lab5_ex3)."""
            remaining = seconds
            chunk = 0.05
            while remaining > 0:
                if ctx.stop_event.is_set():
                    raise KeyboardInterrupt("Stopped by user")
                actual = chunk if remaining > chunk else remaining
                original_sleep(actual)
                remaining -= actual
            if ctx.stop_event.is_set():
                raise KeyboardInterrupt("Stopped by user")

        time.sleep = cooperative_sleep

        start_time = time.time()
        try:
            func()
        except KeyboardInterrupt:
            ctx.output_queue.put(("\n[Stopped by user]\n", "stderr"))
        except Exception as exc:
            ctx.output_queue.put((f"\nError while running {label}: {exc}\n", "stderr"))
        finally:
            duration = time.time() - start_time
            ctx.output_queue.put((f"\nFinished in {duration:.2f}s\n", "stdout"))
            ctx.root.after(0, lambda: _set_status(ctx, f"Idle (last {duration:.2f}s)"))
            builtins.input = original_input
            sys.stdout = original_stdout
            sys.stderr = original_stderr
            time.sleep = original_sleep
            ctx.stop_event.clear()
            ctx.runner_thread = None

    ctx.runner_thread = threading.Thread(target=run_func, daemon=True)
    ctx.runner_thread.start()


def _stop_run(ctx: _AppContext):
    """Signal the running exercise to stop (cooperative)."""
    if ctx.runner_thread and ctx.runner_thread.is_alive():
        ctx.stop_event.set()
        _set_status(ctx, "Stopping...")
    else:
        messagebox.showinfo("Idle", "No exercise is currently running.")


def _force_stop(ctx: _AppContext):
    """Try a best-effort force stop by signalling and dropping the thread reference."""
    if ctx.runner_thread and ctx.runner_thread.is_alive():
        ctx.stop_event.set()
        _set_status(ctx, "Force-stopping...")

        def check():
            if ctx.runner_thread and ctx.runner_thread.is_alive():
                messagebox.showwarning(
                    "Force stop",
                    "The exercise is still running in the background. Close the app if it does not finish soon.",
                )
            ctx.runner_thread = None
            _set_status(ctx, "Idle")

        ctx.root.after(2500, check)
    else:
        messagebox.showinfo("Idle", "No exercise is currently running.")


def _show_code(ctx: _AppContext):
    """Display the source code of the selected exercise in a separate window."""
    resolved = _get_selected_entry(ctx)
    if resolved is None:
        return
    _, section, label, func, tags, needs_file = resolved
    try:
        main_source = inspect.getsource(func)
    except OSError as exc:
        messagebox.showerror("Error", f"Could not load source: {exc}")
        return

    def collect_helpers(target_func, visited=None):
        """Recursively collect helper functions used by target_func from this file."""
        visited = visited or set()
        helpers_local = []
        try:
            src = inspect.getsource(target_func)
        except OSError:
            return helpers_local

        # Find candidate identifiers; we resolve to functions defined in this file.
        identifiers = set(re.findall(r"\b([A-Za-z_][A-Za-z0-9_]*)\b", src))
        globals_dict = target_func.__globals__

        for name in sorted(identifiers):
            if name == target_func.__name__:
                continue
            if name.startswith("__"):
                continue
            if name in visited:
                continue
            candidate = globals_dict.get(name)
            if callable(candidate) and inspect.isfunction(candidate):
                try:
                    candidate_file = Path(inspect.getsourcefile(candidate) or "")
                    candidate_src = inspect.getsource(candidate)
                except OSError:
                    continue
                if candidate_file == Path(__file__):
                    visited.add(name)
                    helpers_local.append((name, candidate_src))
                    helpers_local.extend(collect_helpers(candidate, visited))
        return helpers_local

    helpers = collect_helpers(func)

    top = tk.Toplevel(ctx.root)
    top.title(f"Source: {label}")
    top.geometry("760x600")
    top.configure(bg="#0b1220")

    style = ttk.Style(top)
    style.theme_use("clam")
    style.configure("TLabel", background="#0b1220", foreground="#e2e8f0", font=("Segoe UI", 10))

    # Build an explanation header describing what this exercise is and how it works.
    doc = inspect.getdoc(func) or ""
    doc_lines = doc.splitlines()
    explanation_lines = [
        "# Explanation / context:",
        f"# Section: {section}",
        f"# Exercise: {label}",
        f"# Tags: {', '.join(tags) if tags else 'none'}",
        f"# Needs file input: {'Yes' if needs_file else 'No'}",
    ]
    question = QUESTION_BANK.get(label)
    if question:
        explanation_lines.append("# Question:")
        for line in question.splitlines():
            explanation_lines.append(f"#   {line}")
    if doc_lines:
        explanation_lines.append("# Docstring:")
        explanation_lines.extend([f"#   {line}" for line in doc_lines])
    explanation_lines.append("# Helper functions used in this exercise are shown below if detected.")
    explanation_header = "\n".join(explanation_lines) + "\n\n"

    display_parts = [explanation_header, "# Main function\n", main_source]
    for name, helper_src in helpers:
        display_parts.append(f"\n\n# Helper: {name}\n")
        display_parts.append(helper_src)
    display_source = "".join(display_parts)

    ttk.Label(top, text=label, style="TLabel").pack(anchor="w", padx=10, pady=6)

    text = tk.Text(
        top,
        wrap=tk.NONE,
        bg="#0b1220",
        fg="#e2e8f0",
        insertbackground="#38bdf8",
        highlightthickness=0,
        padx=10,
        pady=10,
        font=("Consolas", 10),
    )
    # Prepend explanation comments before the raw source to show the logic summary in the viewer.
    text.insert("1.0", display_source)
    text.tag_configure("kw", foreground="#38bdf8")
    text.tag_configure("comment", foreground="#94a3b8")
    text.tag_configure("string", foreground="#fbbf24")

    def highlight(pattern, tag):
        for match in re.finditer(pattern, display_source, flags=re.MULTILINE):
            start = f"1.0 + {match.start()} chars"
            end = f"1.0 + {match.end()} chars"
            text.tag_add(tag, start, end)

    highlight(r"#.*", "comment")
    highlight(r"(\".*?\"|\'.*?\')", "string")
    for kw in keyword.kwlist:
        highlight(rf"\\b{re.escape(kw)}\\b", "kw")

    text.config(state="disabled")

    xscroll = tk.Scrollbar(top, orient="horizontal", command=text.xview)
    yscroll = tk.Scrollbar(top, orient="vertical", command=text.yview)
    text.configure(xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)

    text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    yscroll.pack(side=tk.RIGHT, fill=tk.Y)
    xscroll.pack(side=tk.BOTTOM, fill=tk.X)


def _copy_output(ctx: _AppContext):
    """Copy output text to clipboard."""
    if ctx.output_widget is None:
        return
    text = ctx.output_widget.get("1.0", tk.END)
    ctx.root.clipboard_clear()
    ctx.root.clipboard_append(text)
    messagebox.showinfo("Copied", "Output copied to clipboard.")


def _save_output(ctx: _AppContext):
    """Save output to a user-selected file."""
    if filedialog is None or ctx.output_widget is None:
        return
    text = ctx.output_widget.get("1.0", tk.END)
    if not text.strip():
        messagebox.showinfo("Empty", "No output to save.")
        return
    target = filedialog.asksaveasfilename(
        title="Save output",
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
    )
    if not target:
        return
    with open(target, "w", encoding="utf-8") as f:
        f.write(text)
    messagebox.showinfo("Saved", f"Output saved to {target}")


def _sample_input(ctx: _AppContext):
    """Let user pick a file and store it as a recent helper (copied to clipboard)."""
    if filedialog is None:
        messagebox.showinfo("Unavailable", "File dialog is not available.")
        return
    chosen = filedialog.askopenfilename(title="Pick a sample file")
    if not chosen:
        return
    _remember_file(ctx, chosen)
    ctx.root.clipboard_clear()
    ctx.root.clipboard_append(chosen)
    messagebox.showinfo("Sample ready", f"File path copied to clipboard:\n{chosen}")


def launch_gui():
    """
    Start a Tkinter window with:
    - left: categorized list of exercises + Run/Stop buttons
    - right: live output area
    Runs exercises in a background thread to keep the UI responsive.
    """
    if tk is None:
        print("Tkinter is not available; falling back to console menu.")
        main()
        return

    prefs = _load_prefs()
    entries = _flatten_menu()
    root = tk.Tk()
    root.title("I2235 Labs & TD Exercises")
    root.geometry(str(prefs.get("geometry", "950x600")))
    root.configure(bg="#0b1220")

    style = ttk.Style(root)
    style.theme_use("clam")
    style.configure("TFrame", background="#0b1220")
    style.configure("TLabel", background="#0b1220", foreground="#e2e8f0", font=("Segoe UI", 10))
    style.configure("Header.TLabel", background="#0b1220", foreground="#38bdf8", font=("Segoe UI Semibold", 18))
    style.configure("Accent.TButton", font=("Segoe UI", 10, "bold"))
    style.map("Accent.TButton", background=[("active", "#0ea5e9")])

    header = ttk.Frame(root, padding=(15, 12))
    header.pack(fill=tk.X)
    ttk.Label(header, text="I2235 Exercises Launcher", style="Header.TLabel").pack(side=tk.LEFT)
    ttk.Label(header, text="Run labs & TDs with live output, stop any time (Ctrl+C).").pack(side=tk.LEFT, padx=14)

    content = ttk.Frame(root, padding=10)
    content.pack(fill=tk.BOTH, expand=True)

    left_frame = ttk.Frame(content, padding=10)
    left_frame.pack(side=tk.LEFT, fill=tk.Y)
    right_frame = ttk.Frame(content, padding=10)
    right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    ctx = _AppContext(root, entries, prefs)

    # Filters row
    filter_row = ttk.Frame(left_frame)
    filter_row.pack(fill=tk.X, pady=(0, 6))
    ttk.Label(filter_row, text="Search").pack(side=tk.LEFT)
    search_var = tk.StringVar(value=prefs.get("search", ""))
    search_entry = ttk.Entry(filter_row, textvariable=search_var, width=22)
    search_entry.pack(side=tk.LEFT, padx=(6, 6))
    ttk.Label(filter_row, text="Tag").pack(side=tk.LEFT, padx=(4, 2))
    tag_var = tk.StringVar(value=prefs.get("tag", "All"))
    tag_box = ttk.Combobox(filter_row, textvariable=tag_var, values=["All"] + ALL_TAGS, width=12, state="readonly")
    tag_box.pack(side=tk.LEFT)
    needs_file_var = tk.BooleanVar(value=bool(prefs.get("needs_file_only", False)))
    ttk.Checkbutton(filter_row, text="Needs file", variable=needs_file_var).pack(side=tk.LEFT, padx=(8, 0))

    ttk.Label(left_frame, text="Exercises").pack(anchor="w")
    listbox = tk.Listbox(
        left_frame,
        width=42,
        height=25,
        bg="#0b1220",
        fg="#e2e8f0",
        selectbackground="#38bdf8",
        highlightthickness=0,
        activestyle="none",
    )
    listbox.pack(fill=tk.Y, expand=True, pady=(6, 6))
    ctx.listbox = listbox

    def trigger_filter(*_):
        _apply_filters(ctx, search_var.get(), tag_var.get(), needs_file_var.get())

    search_entry.bind("<KeyRelease>", trigger_filter)
    tag_box.bind("<<ComboboxSelected>>", trigger_filter)
    needs_file_var.trace_add("write", lambda *_: trigger_filter())
    _apply_filters(ctx, search_var.get(), tag_var.get(), needs_file_var.get())

    def _restore_last_selection():
        last_label = prefs.get("last_label")
        if not last_label:
            return
        for list_idx, entry_idx in ctx.display_map.items():
            _, label, _, _, _ = ctx.filtered_entries[entry_idx]
            if label == last_label:
                listbox.select_clear(0, tk.END)
                listbox.select_set(list_idx)
                listbox.see(list_idx)
                break

    _restore_last_selection()

    btn_row = ttk.Frame(left_frame)
    btn_row.pack(fill=tk.X, pady=(4, 0))
    ttk.Button(btn_row, text="Run Selected", style="Accent.TButton", command=lambda: _start_run(ctx)).pack(fill=tk.X, pady=2)
    ttk.Button(btn_row, text="Show Code", command=lambda: _show_code(ctx)).pack(fill=tk.X, pady=2)
    ttk.Button(btn_row, text="Sample Input", command=lambda: _sample_input(ctx)).pack(fill=tk.X, pady=2)
    ttk.Button(btn_row, text="Stop (Ctrl+C)", command=lambda: _stop_run(ctx)).pack(fill=tk.X, pady=2)
    ttk.Button(btn_row, text="Force Stop", command=lambda: _force_stop(ctx)).pack(fill=tk.X, pady=2)

    status_row = ttk.Frame(left_frame, padding=(0, 6))
    status_row.pack(fill=tk.X)
    ttk.Label(status_row, text="Status:").pack(side=tk.LEFT)
    status_label = ttk.Label(status_row, text="Idle", foreground="#38bdf8")
    status_label.pack(side=tk.LEFT, padx=6)
    ctx.status_label = status_label

    out_header = ttk.Frame(right_frame)
    out_header.pack(fill=tk.X)
    ttk.Label(out_header, text="Output").pack(side=tk.LEFT)
    ttk.Button(out_header, text="Copy Output", command=lambda: _copy_output(ctx)).pack(side=tk.RIGHT, padx=4)
    ttk.Button(out_header, text="Save Output", command=lambda: _save_output(ctx)).pack(side=tk.RIGHT, padx=4)
    output = tk.Text(
        right_frame,
        wrap=tk.WORD,
        height=28,
        bg="#0b1220",
        fg="#e2e8f0",
        insertbackground="#38bdf8",
        highlightthickness=0,
        padx=8,
        pady=8,
    )
    output.pack(fill=tk.BOTH, expand=True, pady=(6, 0))
    output.configure(state="normal")
    output.tag_configure("stdout", foreground="#e2e8f0")
    output.tag_configure("stderr", foreground="#f87171")
    ctx.output_widget = output

    listbox.bind("<Double-Button-1>", lambda event: _start_run(ctx))
    root.bind("<Control-c>", lambda event: _stop_run(ctx))
    _drain_output(ctx)

    def _persist_and_quit():
        # Try to stop a running exercise before closing.
        if ctx.runner_thread and ctx.runner_thread.is_alive():
            ctx.stop_event.set()
            ctx.runner_thread.join(timeout=1.5)
        prefs["geometry"] = root.winfo_geometry()
        prefs["search"] = search_var.get()
        prefs["tag"] = tag_var.get()
        prefs["needs_file_only"] = bool(needs_file_var.get())
        res = _get_selected_entry(ctx, quiet=True)
        if res:
            _, _, label, _, _, _ = res
            prefs["last_label"] = label
        _save_prefs(prefs)
        ctx.exiting = True
        try:
            root.quit()
        finally:
            root.after(50, root.destroy)

    footer = ttk.Frame(root, padding=(10, 6))
    footer.pack(fill=tk.X)
    ttk.Button(footer, text="Quit", command=_persist_and_quit).pack(side=tk.RIGHT)
    root.protocol("WM_DELETE_WINDOW", _persist_and_quit)

    root.mainloop()


if __name__ == "__main__":
    launch_gui()
