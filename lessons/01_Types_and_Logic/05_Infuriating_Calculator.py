"""
Infuriating Calculator

Let's write a calculator that's really hard to use, not because we want it to be
hard, but just because we haven't learned how to make it easy yet.

Ask the user for three things: 

1. A number
2. A second number
3. A math operation (add, subtract, multiply, divide)
4. Use if-elif-else statements to provide the desired math operation on the
   numbers and display the result.

If the user enters an unknown operation, display an error message. ( use
messagebox.showerror() 

For the number, you can ask for a float or an integer with
simpledialog.askfloat() or simpledialog.askinteger(), and for the math operation
you can ask for a string with simpledialog.askstring().

"""

# Import the required modules
from tkinter import messagebox, simpledialog, Tk # import required modules

# Create a window object
window = Tk()     # Create a window object
 

# Hide the window, hint: use the withdraw method
window.withdraw()

# Ask the user for the first number   
number1 = simpledialog.askinteger('Pick a Number', "Pick a Number")

# Ask the user for the second number
number2 = simpledialog.askinteger('Pick a Number', "Pick another Number")

# Ask the user for the math operation
mathOperation = simpledialog.askstring('Pick a Math Operation', "Pick a Math Operation")
# Use if-elif-else statements to provide the desired math operation on the numbers and display the result.
if mathOperation == "addition":
   messagebox.showinfo('Your Operation', str(number1) + " + " + str(number2) + " = " + str(number1 + number2))
elif mathOperation == "subtraction":
   messagebox.showinfo('Your Operation', str(number1) - " - " + str(number2) + " = " + str(number1 - number2))
elif mathOperation == "multiplication":
   messagebox.showinfo('Your Operation', str(number1) + " * " + str(number2) + " = " + str(number1 * number2))
elif mathOperation == "division": 
   messagebox.showinfo('Your Operation', str(number1) + " / " + str(number2) + " = " + str(number1 / number2))
else:
   messagebox.showerror()
# If the user enters an unknown operation, display an error message. ( use messagebox.showerror()

# Keep the window open
