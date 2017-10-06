def drawSquare(side):
	for x in range(0, side):
		print ("*"*side)
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

def drawXSquare(side):
	############################################################################
	# TODO: Implement this code segment                                        #
    ############################################################################
    pass
	############################################################################
	# END CODE HERE					                                           #
	############################################################################

def drawClockwiseSpiral(side):
	top, left, down, right = 0, 0, 0, 0;

	matrix = [[0 for a in range(side)] for b in range(side)]

	x = top * 2
	y = left * 2

	while True:
	
		# go right
		current = y
		if(current > side - (right * 2)):
			matrix[x][y] = "*"
			break;
		while (y < side - (right * 2) - 1):
			matrix[x][y] = "*"
			y+=1;
		top+=1

		# go down
		current = x
		if(current > side - (down * 2)):
			matrix[x][y] = "*"
			break;
		while (x < side - (down * 2) - 1):
			matrix[x][y] = "*"
			x+=1;
		right+=1

		# go left
		current = y
		if(current < 0 + (left * 2)):
			matrix[x][y] = "*"
			break;
		while (y > 0 + (left * 2)):
			matrix[x][y] = "*"
			y-=1;
		down+=1
		print(x, y)
		print(left)

		# go up
		current = x
		if(current < 0 + (top * 2)):
			matrix[x][y] = "*"
			break;
		while (x > 0 + (top * 2)):
			matrix[x][y] = "*"
			x-=1;
		left+=1

	for x in range(0, side):
		for y in range(0, side):
			print(matrix[x][y], end="")
		print()

def drawCounterClockwiseSpiral(side):
	############################################################################
	# TODO: Implement this code segment                                        #
    ############################################################################
    pass            
	############################################################################
	# END CODE HERE					                                           #
	############################################################################

def drawZigzag(length, oscillation):
	############################################################################
	# TODO: Implement this code segment                                        #
    ############################################################################
    pass            
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
		print("[5] - X-Square")
		print("[6] - Clockwise Spiral")
		print("[7] - Counter-Clockwise Spiral")
		print("[8] - Zigzag")
		print("[9] - Exit")
		try:
			resp = int(input("Response: "))
			if resp >= 1 and resp <= 9:
				break
			else:
				print("Response must be from 1 to 9")
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
		side = int(input("Enter side length: "))
		drawXSquare(side)
	elif resp == 6:
		side = int(input("Enter side length: "))
		drawClockwiseSpiral(side)
	elif resp == 7:
		side = int(input("Enter side length: "))
		drawCounterClockwiseSpiral(side)
	elif resp == 8:
		length = int(input("Enter length: "))
		oscillation = int(input("Enter oscillation: "))
		drawZigzag(length, oscillation)
	elif resp == 9:
		break
