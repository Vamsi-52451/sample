text =  "Hello, Python!"

print("Original string:", repr(text))

# 1. strip() — remove leading and trailing whitespace
print("strip():", repr(text.strip()))  

# 2. lower() — convert to lowercase
print("lower():", text.lower())        

# 3. upper() — convert to uppercase
print("upper():", text.upper())        

# 4. replace() — replace substring
print("replace('Python', 'World'):", text.replace("Python", "World")) 

# 5. split() — split into list by whitespace (default)
print("split():", text.split())        

# 6. find() — find substring, returns index or -1 if not found
print("find('Python'):", text.find("Python"))  

# 7. startswith() — check if string starts with substring
print("startswith('  He'):", text.startswith("  He"))  

# 8. endswith() — check if string ends with substring
print("endswith('!  '):", text.endswith("!  "))        

# 9. join() — join list elements into a string
words = ["Python", "is", "awesome"]
print("join():", " ".join(words))  

# 10. count() — count occurrences of substring
print("count('o'):", text.count("o"))  # 2
