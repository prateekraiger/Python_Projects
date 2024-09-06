import random
import string

def generate_password(length=12,upcase=True,lwcase=True,digit=True,special=True):
	character=''
	if upcase:
		character+=string.ascii_uppercase
	if lwcase:
		character+=string.ascii_lowercase
	if digit:
		character+=string.digits
	if special:
		character+=string.punctuation
	if not character:
		print("ERROR!!! : At least one character type should be selected")
		return None

	password=''.join(random.choice(character) for _ in range(length))
	return password

print("Welcome to the PAssWord GEneRator")
print("You can customize your passwored be selecting the characters types to includes")

pass_length=int(input("Enter the length of the password : "))

inc_upcase=input("Include uppercase letters ? (y/n) : ").lower()=='y'
inc_lwcase=input("Include lowercase letters ? (y/n) : ").lower()=='y'
inc_digit=input("Include digits ? (y/n) : ").lower()=='y'
inc_special=input("Include special characters ? (y/n) : ").lower()=='y'

gen_password= generate_password(
	length=pass_length,
	upcase=inc_upcase,
	lwcase=inc_lwcase,
	digit=inc_digit,
	special=inc_special
)

if gen_password:
	print("Your  password is : ",gen_password)
else:
	print("No password generated. Please Try again")