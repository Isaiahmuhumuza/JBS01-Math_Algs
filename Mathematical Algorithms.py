import tkinter as tk
from tkinter import *

root = tk.Tk()

var = tk.IntVar()

root.geometry("500x500")
root.title("Mathematical Algorithms")
label = tk.Label(root, text = "Choose what you want to solve", font=('Arial', 16))
firstEntry = tk.Frame(root)
secondEntry = tk.Frame(root)

label.pack()

def calc():
    try:

        base = int(textBox.get())    
        baseTwo = int(textboxTwo.get())

# Factorial

        if var.get() == 1:
            nfac = 1
            for i in range(1, base + 1):
                nfac =nfac*i
            result = "Answer: " + str(nfac)
            solution.pack()
            solution.delete("1.0", "end")
            solution.insert("1.0", str(result))

# Fibonacci Sequence

        if var.get() == 2:
            def fibonacci(x):
                if x == 1:
                    return 0
                else:
                    first = 0
                    second = 1

                    for i in range(1, x, 1):
                        fib = first + second
                        first = second
                        second = fib
                    return fib
                
            if base == 0:
                x = "Invalid input"
            elif base == 1:
                x = (f"The {str(base)} st  fibonacci number   is  {str(fibonacci(base))}")
            elif base == 2:
                x = (f"The {str(base)} nd  fibonacci number   is  {str(fibonacci(base))}")

            elif base == 3:
                x = (f"The {str(base)} rd  fibonacci number   is  {str(fibonacci(base))}")
            elif base != 0:
                x = (f"The {str(base)} th  fibonacci number   is  {str(fibonacci(base))}")

            solution.pack()
            solution.delete("1.0", "end")
            solution.insert("1.0", str(x))

#Prime numbers

        if var.get() == 3:

            def isPrime(num):
                if num <= 1:
                    return False
                for i in range(2, num): #Checks if there is a value divisible to num within the range
                    if num % i == 0:
                        return False
                return True

            def generatePrimes(limit):
                number = 2
                primes = []
                while len(primes) < limit:
                    if isPrime(number):
                        primes.append(number)   # Append the number to the prime obejct(0) and stops when it reachs the limit(y)
                    number += 1
                return primes

            y = (f"The first {base} prime numbers are {str(generatePrimes(base))}")

            solution.pack()
            solution.delete("1.0", "end")
            solution.insert("1.0", str(y))

# Multiples

        if var.get() == 4:

            def isMultiple(value):
                if value % base == 0:
                    return True
                
            def generateMultiples(limit):
                start = base + 1
                multiples = []
                while len(multiples) < limit:
                    if isMultiple(start):
                        multiples.append(start)
                    start += 1
                return multiples

            z = (f" The first {baseTwo} multiples of {base} are {generateMultiples(baseTwo)}")

            solution.pack()
            solution.delete("1.0", "end")
            solution.insert("1.0", str(z))

    except ValueError:

        solution.pack()
        solution.delete("1.0", "end")
        solution.insert("1.0", "Invalid input")

def sel():

    selection = ""

    if var.get() == 1:
        selection += "Factorial of n"
        textboxTwo.pack_forget()
        multipleLabel.pack_forget()

    elif var.get() == 2:
        selection += "The nth Fibonacci number"
        textboxTwo.pack_forget()
        multipleLabel.pack_forget()

    elif var.get() == 3:
        selection += "The first n prime numbers"
        textboxTwo.pack_forget()
        multipleLabel.pack_forget()

    elif var.get() == 4:
        selection += "The first n multiples of n"
        multipleLabel.pack(side="left")
        textboxTwo.pack(side="left")

    label.config(text = selection)
    entryLabel.pack(side="left")
    textBox.pack(side="left")
    button.pack()

radioOne = Radiobutton(root, text="Factorial of n", font=('Arial', 12), variable=var,  value=1, command=sel)
radioOne.pack( anchor = W )
radioTwo = Radiobutton(root, text="The nth Fibonacci number", font=('Arial', 12), variable=var, value=2, command=sel)
radioTwo.pack( anchor = W )
radioThree = Radiobutton(root, text="The first n prime numbers", font=('Arial', 12), variable=var, value=3, command=sel)
radioThree.pack( anchor = W )
radioFour = Radiobutton(root, text="The The first n multiples of n", font=('Arial', 12), variable=var, value=4, command=sel)
radioFour.pack( anchor = W )

firstEntry.pack()
secondEntry.pack()


#Pack widgets

entryLabel = tk.Label(firstEntry, text = "Number: ", font=('Arial', 16))
textBox = tk.Entry(firstEntry, font=('Arial', 14))

multipleLabel = tk.Label(secondEntry, text = "Number of multiples: ", font=('Arial', 16))
textboxTwo = tk.Entry(secondEntry, font=('Arial', 14))

button = tk.Button(root, text = "Calculate", font=('Arial', 14), command=calc)

solution = tk.Text(root, height=1, width=65)

root.mainloop()