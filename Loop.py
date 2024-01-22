# while loop
number1 = input("enter the range: ")
number1 = int(number1)
i = 1

while i <= number1:
    print(i * "*")
    i += 1

# for loop
number2 = input("enter new range: ")
number2 = int(number2)
for i in range(number2):
    print(i)
    print(i + 1)

print("new update")

x = range(5, 20, 3)
for i in x:
    print(i)

data = "I love data science"
for x in range(len(data)):
    print(data[x])
