# a Python program that uses keys, values, items, get, update and pop on a sample dictionary
data = {"a": 25, "b": 20, "c": 35}
print("Keys:", data.keys())
print("Values:", data.values())
print("Items:", data.items())
print("get b:", data.get("b"))
print("get z:", data.get("z"))
data.update({"b": 40, "d": 45})
print("After update:", data)
removed = data.pop("a")
print("Removed:", removed)
print("After pop:", data)