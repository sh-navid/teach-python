from unicodedata import decimal


print("Strip:", "  Hello  ".lstrip())


print("Partition:", "Hello World".partition("W"))


print("Casefold:", "ß".casefold())


print("Join:", ",".join(["A", "B"]))


print("Split + Join:", ",".join("Hello-World".split("-")))


print("RJust:", "Hello-World".rjust(40))


print("EndsWith:", "Hello-World".endswith("World"))


print("StartsWith:", "Hello-World".startswith("Me"))


print("ZFill:", "Test".zfill(20))


a = "eol"
b = "30!"
s = "Hello-World"
print("Translate + MakeTrans:", s.translate(s.maketrans(a, b)))


print("Format:", "{} my {}".format("Hello", "World"))


print("FormatMap:", "{key1} my {key2}".format_map({"key1": "Test", "key2": "Mind"}))


print("ExpandTab:", "Hello\tWorld".expandtabs(16))


print("Encode:", "Hello".encode(), type("Hello".encode()))


###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


print("Concatenation:", "Hello" + "World")


print("Reverse:", "Hello World"[::-1])


print("Loop (Char Array):")
for ch in "Hello":
    print(ch, end=" - ")
print()


print("Slice:", "Hello World"[2:5])


###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

TAB = 14
print(
    "\n\n\n\tisalnum\tisnumeric\tisdigit\tisdecimal\tisalpha\tisascii".expandtabs(TAB)
)


def check_numeric(inp: str):
    print(
        "{}\t{}\t{}\t{}\t{}\t{}\t{}".format(
            inp,
            inp.isalnum(),
            inp.isnumeric(),
            inp.isdigit(),
            inp.isdecimal(),
            inp.isalpha(),
            inp.isascii(),
        ).expandtabs(TAB)
    )


check_numeric("2")
check_numeric("2.1")
check_numeric("2e10")
check_numeric("ↁ")  # Roman Number
check_numeric("⅔")  # Fraction
check_numeric("2²")  # Superscript
check_numeric("\u00B2")
check_numeric("A")
check_numeric("ب")