import random

d=0
p=0

while True:
	r=input("press r to roll, q to quit")

	if r == 'r':
		d=random.randint(1,6)
		print("you got:",d)
		if d ==6:
			print("congragulations you can play now")
			break
		else:
			print("roll again, till you get 6.")

while True:
	r=input("press r to roll q to quit:")

	if r=='r':
		d= random.randint(1,6)
		print("you got :",d)

		p=p+d
		if p>100:
			p= p-d
			print("wait till you get",100,p,"orless")

		print("your new position is:",p)

		if p ==100:
			print("you won!")
			exit()
		elif p==8:
			p=37
			print("wow, a ladder. Go to ,",p)

		elif p ==11:
			p=2
			print("sorry you got a snake. go to:",p)

		elif p==13:
			p=34
			print("wow you got a ladder, go to :",p)

		elif p==25:
			p=4
			print("sorry you got a snake, go to:",p)

		elif p==38:
			p=9
			print("sorry you got a snake. go to:",p)

		elif p==40:
			p=68
			print("wow you got a ladder, go to :",p)

		elif p==52:
			p=81
			print("wow you got a ladder, go to :",p)

		elif p==65:
			p=46
			print("sorry you got a snake, go to:",p)

		elif p==76:
			p=97
			print("wow you got a ladder, go to :",p)

		elif p==89:
			p=70
			print("sorry you got a snake, go to:",p)

		elif p==93:
			p=64
			print("sorry you got a snake, go to:",p)

	elif r=='q':
		print("bye!")
		exit()

