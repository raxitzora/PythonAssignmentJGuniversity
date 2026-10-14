'''
5. Create a tuple and perform the following methods: Add items(), Check item in a
tuple(), len(), Access items()'''

# Demonstrate Tuple Methods

languages = ("C++", "Java", "PHP")

# 1. Add items to a tuple
languages = ("React",) + languages + ("Java",)
print("After adding elements:", languages)

# 2. Check item in tuple
if "React" in languages:
    print("React is in the tuple")
else:
    print("React is not in the tuple")

# 3. Find length of tuple
print("Length of the tuple:", len(languages))

# 4. Access items
print("First item:", languages[0])
print("Second item:", languages[1])
print("Last item:", languages[-1])