length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))

area = length * width
perimeter = 2 * (length + width)

print("Area of rectangle:", area)
print("Perimeter of rectangle:", perimeter)

print("Addition:", length + width)
print("Subtraction:", length - width)
print("Division:", length / width)
print("Modulus:", length % width)
print("Power:", length ** 2)


def compare_numbers(a, b):
    if a > b:
        print(a, "is larger than", b)
    elif a < b:
        print(a, "is smaller than", b)
    else:
        print("Both numbers are equal")

    print("a == b:", a == b)
    print("a != b:", a != b)
    print("a >= b:", a >= b)
    print("a <= b:", a <= b)


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

compare_numbers(num1, num2)


number = int(input("Enter a number: "))


if number >= 10 and number <= 50:
    print("Number is within the range 10 to 50")
else:
    print("Number is outside the range")

if number < 0 or number > 100:
    print("Number is invalid")
else:
    print("Number is valid")

is_even = number % 2 == 0

if not is_even:
    print("Number is odd")
else:
    print("Number is even")


text = input("Enter a word: ")

if text == "Python":
    print("String matches the pattern")
else:
    print("String does not match")

x = 10   

print("Initial value:", x)

x += 5  
print("After += :", x)

x -= 3   
print("After -= :", x)

x *= 2 
print("After *= :", x)

x /= 4  
print("After /= :", x)

x %= 3  
print("After %= :", x)

x **= 2  
print("After **= :", x)

list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]

print("list1 is list2:", list1 is list2)
print("list1 is list3:", list1 is list3)
print("list1 is not list3:", list1 is not list3)


numbers = [10, 20, 30, 40]

print("20 in numbers:", 20 in numbers)
print("50 not in numbers:", 50 not in numbers)


text = "Python Programming"

print("'Python' in text:", "Python" in text)
print("'Java' not in text:", "Java" not in text)