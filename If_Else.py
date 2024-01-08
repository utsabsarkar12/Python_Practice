age = input("Enter your age: ")

if int(age) >= 18:
    print("you are an adult")
    print("you can vote")
elif int(age) < 18 and int(age) > 8:
    print("you are in school")
else:
    print("you are child")

print("thank you")
