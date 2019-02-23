import random
l=["rock","paper","scissor"]
k=input("press r for rock, p for paper,and s for scissor")

c=random.choice(l)
print("computer gets ,",c)

if k==c:
	print("its a tie")
elif k=="rock" and c=="paper":
	print("paper cathes the scissor,computer wins")
elif k=="rock" and c=="scissor":
	print("rock breaks the scissor, you win")
elif k=="paper" and c=="rock":
	print("paper cathes the rock, you win")
elif k=="paper" and c=="scissor":
	print("scissor cuts the paper, computer wins")
elif k=="scissor" and c=="paper":
	print("scissor cuts the paper, computer wins")
else:
	print("rock breaks the scissor, computer wins")