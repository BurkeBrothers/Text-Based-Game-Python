#accessing lists
ages = [14, 15]
age = []
#print(type(age))
#print(type(age[0]))
choice = int(input("enter an age: "))
age.append(ages[choice])
print("age added: ", ages[choice])