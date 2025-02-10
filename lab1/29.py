# Исходная строка
text = "hello world 123"

# 1. capitalize()
print(text.capitalize())  # "Hello world 123"

# 2. casefold()
print(text.casefold())  # "hello world 123"

# 3. center()
print(text.center(20, "-"))  # "--hello world 123--"

# 4. count()
print(text.count("o"))  # 2

# 5. encode()
encoded = text.encode()
print(encoded)  # b'hello world 123'

# 6. endswith()
print(text.endswith("123"))  # True

# 7. expandtabs()
tab_text = "Hello\tWorld"
print(tab_text.expandtabs(4))  # "Hello   World"

# 8. find()
print(text.find("world"))  # 6

# 9. format()
formatted = "I have {} apples".format(5)
print(formatted)  # "I have 5 apples"

# 10. format_map()
print("My name is {name}".format_map({"name": "Alice"}))  # "My name is Alice"

# 11. index()
print(text.index("world"))  # 6

# 12. isalnum()
print("abc123".isalnum())  # True

# 13. isalpha()
print("hello".isalpha())  # True

# 14. isascii()
print("hello".isascii())  # True

# 15. isdecimal()
print("123".isdecimal())  # True

# 16. isdigit()
print("123".isdigit())  # True

# 17. isidentifier()
print("variable".isidentifier())  # True

# 18. islower()
print(text.islower())  # True

# 19. isnumeric()
print("123".isnumeric())  # True

# 20. isprintable()
print("hello".isprintable())  # True

# 21. isspace()
print("   ".isspace())  # True

# 22. istitle()
print("Hello World".istitle())  # True

# 23. isupper()
print(text.isupper())  # False

# 24. join()
print("-".join(["hello", "world"]))  # "hello-world"

# 25. ljust()
print(text.ljust(20, "-"))  # "hello world 123----"

# 26. lower()
print(text.lower())  # "hello world 123"

# 27. lstrip()
print("   hello".lstrip())  # "hello"

# 28. maketrans()
trans = str.maketrans("h", "H")
print(text.translate(trans))  # "Hello world 123"

# 29. partition()
print(text.partition("world"))  # ('hello ', 'world', ' 123')

# 30. replace()
print(text.replace("world", "Python"))  # "hello Python 123"

# 31. rfind()
print(text.rfind("o"))  # 7

# 32. rindex()
print(text.rindex("o"))  # 7

# 33. rjust()
print(text.rjust(20, "-"))  # "----hello world 123"

# 34. rpartition()
print(text.rpartition("o"))  # ('hello w', 'o', 'rld 123')

# 35. rsplit()
print(text.rsplit(" ", 1))  # ['hello world', '123']

# 36. rstrip()
print("hello   ".rstrip())  # "hello"

# 37. split()
print(text.split())  # ['hello', 'world', '123']

# 38. splitlines()
multi_line_text = "hello\nworld\n123"
print(multi_line_text.splitlines())  # ['hello', 'world', '123']

# 39. startswith()
print(text.startswith("hello"))  # True

# 40. strip()
print("   hello   ".strip())  # "hello"

# 41. swapcase()
print(text.swapcase())  # "HELLO WORLD 123"

# 42. title()
print("hello world".title())  # "Hello World"

# 43. translate()
# We can reuse maketrans example here
print(text.translate(trans))  # "Hello world 123"

# 44. upper()
print(text.upper())  # "HELLO WORLD 123"

# 45. zfill()
print("42".zfill(5))  # "00042"
