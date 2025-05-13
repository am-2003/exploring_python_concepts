def task1():
    name = "Adi"
    age = 21
    height = 5.9

    print(f"Hey there, my name is {name}! I'm {age} years old and {height} feet tall.")
    print()

def task2():
    num1 = 15
    num2 = 4

    sum_result = num1 + num2
    difference = num1 - num2
    product = num1 * num2
    division = num1 / num2

    print(f"The sum of {num1} and {num2} is: {sum_result}")
    print(f"When we subtract {num2} from {num1}, we get: {difference}")
    print(f"Multiplying {num1} and {num2} gives us: {product}")
    print(f"And if we divide {num1} by {num2}, we get: {division:.2f}")
    print()

def task3():
    print("Welcome to the Number Checker!")
    
    try:
        number = float(input("Please enter a number: "))
        if number > 0:
            print("This number is positive. Awesome!")
        elif number < 0:
            print("This number is negative. Better luck next time!")
        else:
            print("Zero it is. A perfect balance!")
    except ValueError:
        print("Oops! That's not a valid number. Please try again!")

def main():
    print("Task 1")
    task1()
    
    print("Task 2")
    task2()
    
    print("Task 3")
    task3()

if __name__ == "__main__":
    main() 