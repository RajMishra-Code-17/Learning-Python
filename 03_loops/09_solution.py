items = ["apple", "banana", "orange", "apple", "mango"]

unique_item = set()

for item in items:
    if item in unique_item:
        print("Duplicate item: ", item)
        break
    unique_item.add(item)

# for the more concept clarity
# items = ["apple", "banana", "orange", "apple", "mango"]
# unique_item = set()

# for item in items:
#     if item in unique_item:
#         print("duplicte: ", item)
#         break
#     unique_item.add(item)