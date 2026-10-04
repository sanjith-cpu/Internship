first_name = input("Enter your first intial: ")
last_name = input("Enter your last initial: ")
food = "Tofu"
email = "hello123@gmail.com"
age = 18
quantity = 12
num_of_students = 30
price = 10.99
gpa = 4.2
distance = 9.10
is_student = False
for_sale = True
print(f"Hello {first_name} {last_name}")
print(f"You like {food}")
print(f"Your email is {email}")
print(f"Your age is {age} years old")
print(f"You are buying {quantity} items")
print(f"There are {num_of_students} students")
print(f"The price is ${price}")
print(f"The GPA is {gpa}")
print(f"The distance is {distance} km")
if is_student:
    print("You are a student")
else:
    print("You are not a student")

if for_sale:
    print("That item is for sale")
else:
    print("The item is not for sale")
