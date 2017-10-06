def drawSquare(side):
	for x in range(0, side):
		print ("*"*side)
	pass
	############################################################################
	# END CODE HERE					                                           #
	############################################################################

def drawRectangle(length,width):
	############################################################################
	# TODO: Implement this code segment                                        #
	############################################################################
	for l in range(length):
		print("*" * width)
	############################################################################
	# END CODE HERE					                                           #
	############################################################################

def drawRightTriangle(height):
        size = 1
        while(size <= height):
                print("*"*size);
                size+=1

def drawDiamond(height):
	############################################################################
	# TODO: Implement this code segment                                        #
        ############################################################################
        height = int(height)
        x = ' '
        y = '*'
        z = int(height/2)-1
        for i in range(1 ,height,2):
                print(x * z + y * (i))
                z-=1
        z+=1
        for a in range(i,0,-2):
                print(x * z + y * (a))
                z+=1
                
	############################################################################
	# END CODE HERE					                                           #
	############################################################################

print("----------------------------Shape Printer----------------------------")
while True:
	resp = 0
	while True:
		print("Which shape do you want to draw?")
		print("[1] - Square")
		print("[2] - Rectangle")
		print("[3] - Right Triangle")
		print("[4] - Diamond")
		print("[5] - Exit")
		try:
			resp = int(input("Response: "))
			if resp >= 1 and resp <= 5:
				break
			else:
				print("Response must be from 1 to 5")
		except ValueError:
			print("Input must be a number")

	if resp == 1:
		side = int(input("Enter side length: "))
		drawSquare(side)
	elif resp == 2:
		length = int(input("Enter length: "))
		width = int(input("Enter width: "))
		drawRectangle(length,width)
	elif resp == 3:
		height = int(input("Enter height: "))
		drawRightTriangle(height)
	elif resp == 4:
		height = int(input("Enter height: "))
		drawDiamond(height)
	elif resp == 5:
		break
