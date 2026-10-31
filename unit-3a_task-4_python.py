#to remove duplicate elements from a list
# Example solution: remove duplicates from a list
list_data = [2, 4, 5, 7, 3, 5, 3, 7]
unique = []
for item in list_data:
    if item not in unique:
        unique.append(item)
print("Original:", list_data)
print("Without duplicates:", unique)