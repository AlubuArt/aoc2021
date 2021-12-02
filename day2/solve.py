file =  open("input.txt")
lines = file.readlines()

# part one
def navigate():
    positionX = 0
    positionY = 0
    for line in lines:
        newLine = line.split(" ")
        direction, value = newLine[0], int(newLine[1])
        if direction == "forward":
            positionX += value
        elif direction == "down":
            positionY += value
        else:
            positionY -= value
    print(positionX * positionY)

navigate()
     
#part two
def navigateAim():
    positionX = 0
    positionY = 0
    aim = 0

    for line in lines:
        newLine = line.split(" ")
        direction, value = newLine[0], int(newLine[1])
        if direction == "forward":
            positionX += value
            positionY += aim * value
        elif direction == "down":
            aim += value
        else:
            aim -= value 

    print(positionX * positionY) 

navigateAim()