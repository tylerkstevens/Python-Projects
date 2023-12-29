# welcome_script.py

def welcome(name):
	return f"Hello, {name}! Welcome to Python scripting."

if __name__ == "__main__":
	user_name = input("Tyler Stevens: ")
	message = welcome(user_name)
	print(message)

# end of script