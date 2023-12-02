#task_1
massiv = [1, 2, 3]
i = 0
for x in massiv:
    i += x
print(f"Sum of number: {i}")


#task_2
x = int(input("enter a number: "))
massiv = [4, 4, 2, 6, 7, 8, 8, 8,]

def count(massiv , x):
    i = 0

    for num in massiv:
        if num == x:
            i += 1

    return i


print(count (massiv, x))


#task_3
num1 = int(input("enter number: "))
num2 = int(input("enter number again: "))
if num1 == num2:
    num3 = num2 ** 2
    print("True")
    print(f"{num2}-ning kvadrati {num3}")
else:
    print("False")