print ( )
from flask import Flask, request, render_template, session
import re
import random
app = Flask(__name__)


@app.route("/",methods=['GET', 'POST'] )
def main():
    randomcolourr2 = lambda: random.randint(0, 255)
    displaycolu2 = ('#%02X%02X%02X' % (randomcolourr2(), randomcolourr2(), randomcolourr2()))


    color = "FFFFFF"
    new_color = request.form.get('color', '')
    if re.search(r'^[0-9A-F]{6}$', new_color):
        color = new_color
	
    print(new_color, displaycolu2)
    return render_template('main.html', color=color, displaycolu2=displaycolu2)


# Function to convert decimal to binary
def decimal_to_binary(dec):
	decimal = int(dec)

	# Prints equivalent decimal
	print(decimal, " in Binary : ", bin(decimal))

# Function to convert decimal to octal
def decimal_to_octal(dec):
	decimal = int(dec)

	# Prints equivalent decimal
	print(decimal, "in Octal : ", oct(decimal))

# Function to convert decimal to hexadecimal
def decimal_to_hexadecimal(dec):
	decimal = int(dec)

	# Prints equivalent decimal
	print(decimal, " in Hexadecimal : ", hex(decimal))

# Driver program
dec = 32
decimal_to_binary(dec)
decimal_to_octal(dec)
decimal_to_hexadecimal(dec)



if __name__ == '__main__':
    app.run(debug=True)
