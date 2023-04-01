my_array=input("enter numbers separated by commas to square and get sum: ")
values=my_array.split(",")
sum=0
for val in values:
    sum=sum+int(val)**2
print("the sum of squares of values is",sum)
