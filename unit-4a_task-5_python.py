# a Python program that prints keys, values and items of a subject-marks dictionary using loops
scores = {"maths": 90, "science": 85, "english": 98}
print("Keys:")
for key in scores:
    print(key)
print("Values:")
for value in scores.values():
    print(value)
print("Items:")
for key, value in scores.items():
    print(key, "→", value)