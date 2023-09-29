# get number of elements
num = int(input("Enter number of elements: "))

# initialize sum and extreme values
sum = 0
max = -float('inf')
min = float('inf')

# loop to get user input and calculate sum, min and max
for i in range(num):
    val = float(input("Enter number: "))
    sum += val
    if val > max:
        max = val
    if val < min:
        min = val

# calculate average
avg = sum/num

# print output
print("Average =", avg)
print("Maximum =", max)
print("Minimum =", min)
