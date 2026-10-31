# to demonstrate set membership testing and methods 
set_data = {100, 200, 300}
print("Set:", set_data)
print("200 in set?", 200 in set_data)
print("400 not in set?", 400 not in set_data)
set_data.add(400)
print("After add:", set_data)
set_data.remove(100)
print("After remove:", set_data)
set_data.discard(99)
print("After discard:", set_data)