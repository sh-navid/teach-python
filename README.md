# Python Instructor

- **Disclaimer:** _The content of this repository is only for testing and training and is provided at the discretion of the author; So it may not be suitable for production or other conditions._
- [Install and Run](/lessons/python/installation/README.md) Python.
- [Examples](/lessons/python/examples/README.md)
- [Homeworks](/README-PYTHON-HOMEWORKS.md)

## Headings
1. [Introduction](introduction/README.md)
1. [Syntax](syntax/README.md)
1. [Variables](concepts/variables/README.md)
1. <details>
   <summary><strong>String</strong></summary>

   - [Strings](/lessons/python/concepts/string)
   - [`encode, decode`](/lessons/python/concepts/string/encode-string.py)
   - [`strip, lstrip, rstrip`](/lessons/python/concepts/string/trim-string.py)
   - [`join, concatenation`](/lessons/python/concepts/string/concat-string.py)
   - [`endswith, startswith, find, rfind, index, rindex`](/lessons/python/concepts/string/search-string.py)
   - [`translate, maketrans, format, format_map`](/lessons/python/concepts/string/format-string.py)
   - [`partition, rpartition, splitlines, split, slice`](/lessons/python/concepts/string/split-string.py)
   - [`(title, capitalize), (lower, upper, swapcase, casefold), (center, ljust, rjust)`](/lessons/python/concepts/string/audit-string.py)
   - [`in, (istitle, islower, isupper), isspace, isprintable, isidentifier, (isascii, isalpha), (isalnum, isnumeric, isdecimal, isdigit)`](/lessons/python/concepts/string/check-string.py)
   - [`zfill, count, replace, len, expandtabs, multi-line, loop-over-characters, reverse`](/lessons/python/concepts/string/other-string-functions.py)
   - [Scape Chars `\t \f \" \n \r \b \oct \hex`](/lessons/python/concepts/string/scape-chars.py)
   </details>
2. [Random](/lessons/python/concepts/random/general-random-functions.py)
   - `random(), randint(), shuffle(), choice()`
3. <details>
      <summary><strong>Operators</strong></summary>

      - [Operators](/lessons/python/concepts/operators)
      1. [Arithmetic](/lessons/python/concepts/operators/arithmetic-operators.py) `+ -` ,...
      2. [Assignment](/lessons/python/concepts/operators/assignment-operators.py) `= += -=` ,...
      3. [Comparison](/lessons/python/concepts/operators/comparison-operators.py) `== != >=` ,...
      4. [Logical](/lessons/python/concepts/operators/logical-operators.py) `and, or, not`
      5. [Identity](/lessons/python/concepts/operators/identity-operators.py) `is, is not`
      6. [Membership](/lessons/python/concepts/operators/membership-operators.py) `in, not in`
      7. [Bitwise](/lessons/python/concepts/operators/bitwise-operators.py) `& | ^ ~ << >>`
      </details>
4. Debugging (break point)
5. <details>
      <summary><strong>List</strong></summary>
      
      - Ordered, Changeable, Indexed, Allow Duplicate
      - [`access, assign, iterate, list(), .append(), .insert(), .remove(), del, .pop(), .copy(), .extend(), .clear(), len(), .count(), slice, join, unpack, in, .index(), .reverse(), .sort()`](/lessons/python/concepts/collections/list-access.py)
      </details>
6. <details>
      <summary><strong>Tuple</strong></summary>
      
      - Ordered, Unchangeable, Indexed, Allow Duplicate
      - Tuples are **unchangeable**, or **immutable** so you cannot add or remove items from it
      - [`access, tuple with one item, tuple(), iterate, del completely, len(), .count(), slice, join, unpack, in, .index()`](/lessons/python/concepts/collections/tuple-access.py)
      </details>
7. <details>
      <summary><strong>Set</strong></summary>
      
      - Unordered, Unchangeable (By index, But you can add/remove), Unindexed, No Duplicate
      - [`access, len(), set(), in, .add(), .update(), (.remove(), .discard(), .pop(), del), .copy(), .clear(), (.union(), intersection, difference, symmetric_difference), (disjoint, subset, superset)`](/lessons/python/concepts/collections/set-access.py)
      - [`frozenset()`](/lessons/python/concepts/collections/set-frozen.py)
      </details>
8. <details>
      <summary><strong>Dictionary</strong></summary>
      
      - Ordered, Changeable, Key Value, No Duplicate
      - [`access, assign, .update(), dict(), .keys(), .values(), .items(), zip(), len(), .pop(), .popitem(), del, .clear(), .copy(), .fromkeys(), .setdefault())`](/lessons/python/concepts/collections/dict-access.py)
      </details>
9.  <details>
      <summary><strong>DataTypes</strong></summary>
      
      - Numbers: [`Integer, Float, Complex`](/lessons/python/concepts/data-types/data-type-number.py)
      - Sequence: [`String`](/lessons/python/concepts/data-types/data-type-string.py), [`Range`](/lessons/python/concepts/data-types/data-type-range.py), [`List`](/lessons/python/concepts/collections/list-access.py), [`Tuple`](/lessons/python/concepts/collections/tuple-access.py), `Bytes`, `ByteArray`
      - Set: [`Set`](/lessons/python/concepts/collections/set-access.py), [`FrozenSet`](/lessons/python/concepts/collections/set-frozen.py)
      - Map: [`Dictionary`](/lessons/python/concepts/collections/dict-access.py)
      - Nothing: `None`
      - Boolean: [`Boolean`](/lessons/python/concepts/boolean/boolean-concept.py)
      - Binary: [`Bytes, ByteArray, MemoryView`](/lessons/python/concepts/data-types/data-type-bytes.py)
      - `bytes` is immutable; however `bytearray` is mutable
      </details>
10. Module
11. Conversion, TypeCasting
12. Input
13. <details>
      <summary><strong>Keywords</strong></summary>

      - [if, elif, else](/lessons/python/concepts/keywords/keywords-if-elif.py)
      - [for](/lessons/python/concepts/keywords/keywords-for.py)
      - [while, continue, break](/lessons/python/concepts/keywords/keywords-while.py)
      - [try, except, finally](/lessons/python/concepts/keywords/keywords-try-except.py)
      - [and, or, not, in, is](/lessons/python/concepts/keywords/keywords-and-or-not-in-is.py)
      - [import, from, as](/lessons/python/concepts/keywords/keywords-import.py)
      - [class, def, lambda, pass, return, del](/lessons/python/concepts/keywords/keywords-class-def-lambda-pass-ret-del.py)
      - [global, nonlocal](/lessons/python/concepts/keywords/keywords-scope.py)
      - [assert](/lessons/python/concepts/keywords/keywords-assert.py) <sub>[Optonal]</sub>, [raise](/lessons/python/concepts/keywords/keywords-raise.py) <sub>[Optonal]</sub>
      - [with](/lessons/python/concepts/keywords/keywords-with.py) <sub>[Optonal]</sub>
      - [yield](/lessons/python/concepts/keywords/keywords-yield.py) <sub>[Optonal]</sub>
      </details>
15. [Comperhension](/lessons/python/concepts/collections/comperhension.py)
16. Scope, Globals, Locals
    - [`locals(), globals()`](/lessons/python/concepts/variables/scope.py)
17. [Read File, Write File](/lessons/python/examples/sample/file/read-write-file.py), [Pickle](/lessons/python/examples/sample/file/read-write-pickle.py)
18. Math
19. [Date, Time](/lessons/python/concepts/date-time/date-time.py)
14. [Function, Method, Lambda](/lessons/python/concepts/object-oriented/types-of-methods.py)
20. [OOP](/lessons/python/concepts/object-oriented/README.md)
    - Class, Object
    - Constructor
    - ToString, Representation
    - Methods
      - Object Method
      - Static Method
      - Class Method
    - Inheritance
    - Override
    - Overload
      - [Function Overloading](/lessons/python/concepts/object-oriented/function-overloading.py)
          -  Python does not support function overloading
      - [Operator Overloading](/lessons/python/concepts/operators/operator-overload.py) <sub>[OPTIONAL]</sub>
    - Getter, Setter ???
    - [Enum](/lessons/python/concepts/enum/color-enum.py)
1. [Eval, Exec](/lessons/python/concepts/advanced/eval-exec.py)
1. [`*argv`, `**kwargs`](/lessons/python/concepts/advanced/argv-kwargs.py)
----
1. [Test](concepts/test/README.md)
1. [Generator](/lessons/python/concepts/advanced/simple-generator.py)
1. [Assertion](/lessons/python/concepts/advanced/simple-assertion.py)
1. [PIP](/lessons/python/installation/README-PIP.md)
1. [Decorator](/lessons/python/concepts/advanced/simple-decorator.py)


### Optional
1. VENV
7. Exception
   1. Custom Exception
   2. Types of Errors
10. Meta
    1. Meta Classes
    2. Meta Programming
12. Iterator
    - [Iterator, Iterable](/lessons/python/concepts/advanced/simple-iterator.py)
    - [Custom Iterator](/lessons/python/concepts/advanced/custom-iterator.py)
13. Closure
14. [Descriptor](/lessons/python/concepts/advanced/simple-descriptor.py)
15. [Reflection](/lessons/python/concepts/advanced/simple-reflection.py)
16. [Context Manager](/lessons/python/concepts/keywords/keywords-with.py)
17. Regular Expression
18. Socket [`client`](/lessons/python/examples/sample/socket/simple-socket-client.py), [`server`](/lessons/python/examples/sample/socket/simple-socket-server.py)
19. Data
    1.  SQL, NoSQL, ORM (SQLAlchemy)
    2.  JSON, CSV, XML, OWL, ...
20. Serialization, Deserialization


---
### New Cource (Temp)
- [NumPy](/lessons/python/modules/numpy/README.md)
- [Test](concepts/test/README.md)
- Class
- Reflection
---


### Advanced
1. Dependency Injection
2. Inversion of Control
3. Message Passing
4. Multi Threading
5. Multi Processing
6. Semaphore, Lock, Mutex

## Modules, Packages, Libs, ...
- [**Tkinter**](/lessons/python/modules/tkinter/README.md)
- [**Turtle**](/lessons/python/modules/turtle/README.md)
- [**NumPy**](/lessons/python/modules/numpy/README.md)
- [**Pandas**](/lessons/python/modules/pandas/README.md)
- Matplotlib
- PyQT
- Kivy
- [**DJango**](/lessons/python/modules/django/README.md)
- [**Flask**](/lessons/python/modules/flask/README.md)
- Scrapy
- Selenium
- BeautifulSoup
- [**OpenCV**](/lessons/python/modules/opencv/README.md)
- Pillow
- **PyGame** ([1](/lessons/python/examples/sample/game_engine/simple-2d-game-part1.py),[2](/lessons/python/examples/sample/game_engine/simple-2d-game-part2.py),[3](/lessons/python/examples/sample/game_engine/simple-2d-game-part3.py),[4](/lessons/python/examples/sample/game_engine/simple-2d-game-part4.py))
- Open3D
- TF
- PyTorch
- Keras
- Scikit-learn
- SciPy
- Seaborn
- PyAutoGUI

## More
- [**AI**](lessons/ai/README.md)
- [**Web**](lessons/frontend/README.md)
- [**Linux** <sub>(Basic Concepts)</sub>](lessons/linux/README.md)
- [**Network** <sub>(Basic Concepts)</sub>](lessons/network/README.md)
- [**Security** <sub>(Basic Concepts)</sub>](lessons/security/README.md)
- [**SQL**](lessons/sql/README.md)