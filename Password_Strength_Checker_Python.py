special_characters = "@#$%^&*!?"
upper_ = lower_ = special_ = number_ = length_ = 0
i = 0
print("You can use this special characters : @#$%^&*!?")

password = input("Please enter your password : ")

while i < len(password) :
	ch = password[i]
	if ch.isupper() :
		upper_ = 1
	if ch.islower() :
		lower_ = 1
	if ch.isdigit() :
		number_ = 1
	if ch in special_characters :
		special_ = 1
		
	i +=1
		
if len(password)>7 :
	length_ = 1

sum = upper_ + lower_ + special_ + number_ + length_
print(f"Your password strength is {sum}")
if sum < 5 :
	print("To improve your password :")
if lower_ == 0 :
	print("At least add a lowercase character.")
if upper_ == 0 :
	print("At least add a uppercase character.")
if number_ == 0 :
	print("At least add a number.")
if special_ ==0 :
	print("At least add a special character.")
if len(password) < 8 :
	print("Your password better be at least 8 characters.")
