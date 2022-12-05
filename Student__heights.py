numbers1 = input("Enter the list of students heights :  ")
numbers = numbers1.split(" ")

j = 0 
sum = 0
for i in numbers:

    sum += int(numbers[j])
    j += 1
print(f"number of students: {j}")
print(f"average of student heights is {sum/j}")

