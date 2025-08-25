fruits = ["apple", "banana", "cherry"]
print("Original list:", fruits)

# 1. append() - Add an item to the end
fruits.append("orange")
print("\nAfter append('orange'):", fruits)

# 2. insert() - Insert item at a specified index
fruits.insert(1, "blueberry")
print("\nAfter insert(1, 'blueberry'):", fruits)

# 3. extend() - Add elements from another list
fruits.extend(["mango", "pineapple"])
print("\nAfter extend(['mango', 'pineapple']):", fruits)

# 4. remove() - Remove first occurrence of a value
fruits.remove("banana")
print("\nAfter remove('banana'):", fruits)

# 5. pop() - Remove and return item at index (default last)
popped = fruits.pop()
print("\nAfter pop():", fruits)
print("Popped item:", popped)

popped_index_2 = fruits.pop(2)
print("\nAfter pop(2):", fruits)
print("Popped item at index 2:", popped_index_2)

# 6. clear() - Remove all items
temp_list = fruits.copy()  
temp_list.clear()
print("\nAfter clear():", temp_list)

# 7. index() - Get index of first occurrence of a value
index_apple = fruits.index("apple")
print("\nIndex of 'apple':", index_apple)

# 8. count() - Count occurrences of a value
fruits.append("apple")
count_apple = fruits.count("apple")
print("\nCount of 'apple':", count_apple)

# 9. sort() - Sort the list (in-place)
numbers = [3, 1, 4, 2, 5]
print("\nOriginal numbers list:", numbers)
numbers.sort()
print("After sort():", numbers)

# 10. reverse() - Reverse the list (in-place)
numbers.reverse()
print("After reverse():", numbers)

# 11. copy() - Returns a shallow copy of the list
numbers_copy = numbers.copy()
print("\nCopy of numbers list:", numbers_copy)
