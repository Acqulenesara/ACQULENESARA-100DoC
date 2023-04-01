my_array = [1, 2, 3, 4, 5]
num_list = input("Enter numbers separated by commas to add to the array: ")
numbers = num_list.split(",")
for num in numbers:
    my_array.append(int(num))
print("Updated array:", my_array)
