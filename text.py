import random

while True:
	d=input("press r to keep rolling")

	if d=='r':
		print(random.randint(1,6))

	elif d=='q':
		print("bye!")
		exit()

print("end!")