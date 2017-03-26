if 3 > 2:
	print('It Works!')
if 5 > 2:
	print('5 is indeed greater than 2')
else:
	print('5 is not greater than 2')
name = 'Tess'
if name == 'Rim':
	print('Hey Rim!')
elif name == 'Tess':
	print('Hey Tess!')
else:
	print('Hey anonymous!')
volume = 90
if volume < 20:
	print("It's kinda quiet.")
elif 20 <= volume < 40:
	print("It's nice for background music")
elif 40 <= volume < 60:
	print("Perfect, I can hear all the details")
elif 60 <= volume < 80:
	print("Nice for parties")
elif 80 <= volume < 100:
	print("A bit loud!")
else:
	print('My ears are hurting! :(')

def hi():
	print("hi there!")
	print("love you!")
	print("bye!")

hi()

def sum_the_numbers(a, b, c):
	print(a + b + c)

sum_the_numbers(3, 4, 5)

def hi(name):
	if name == 'Tess':
		print('Hi Tess!')
	elif name == 'Rim':
		print('Hi Rim')
	else:
		print('Hi Stranger!')

hi('Rim')



