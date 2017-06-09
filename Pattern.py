from graphics import *
import math

def main():
    size, colourList = getInput()
    window = drawFullPatchwork(size, colourList)
    colourChanger(window, size, colourList)
    
    
def getInput():
    validColours = ["red", "green", "blue", "orange", "brown", "pink"]
    validwindowdowSize = ["5", "7", "9"]
    colourList = []
    counter = 0
    
    while counter < 1:
        size = input("please enter the patchwork size either 5, 7 or 9: ")
        if size in validwindowdowSize:
            size = int(size)
            counter = counter + 1
        else: 
            print("The size can ONLY be the digits 5, 7 or 9: ")
        
    print("This program requires 3 different colours to create the patchwork")
    while len(colourList) < 3:
        colour = input("Please enter a colour : ")
        if colour.isalpha() and colour in validColours and colour \
                                                    not in colourList:
            colourList.append(colour)
        else:
            print("error valid colours are red, green, blue, orange, ",\
                       "brown and pink. Please use each colour only once")
    return(size, colourList)
            
            
def drawTriangles(window,vertices,fill):
    triangle = Polygon(vertices) 
    triangle.setFill(fill)
    triangle.setOutline("")
    triangle.draw(window)
    
    
def trianglePatch(window, topLeftX, topLeftY, fill):
    anchorPointX = topLeftX -10
    for i in range(5):
        anchorPointY = topLeftY + (20 * i)
        
        for j in range(6):
            anchorPointX = topLeftX-10 
            if i % 2 != 0:# if i is odd offset
                pass
                anchorPointX = anchorPointX + (20*j)
                if j == 5:
                    pass
                else:
                    # right handed right angle triangle
                    left = Point(anchorPointX+10, anchorPointY)
                    right = Point(anchorPointX + 20, anchorPointY)
                    bottom = Point(anchorPointX + 10, anchorPointY + 20)
                    vertices = [left, right, bottom]
                    drawTriangles(window,vertices,fill)
                if j == 0 : 
                    pass
                else:
                    # left handed right angle triangle
                    left = Point(anchorPointX, anchorPointY)
                    right = Point(anchorPointX+10, anchorPointY)
                    bottom = Point(anchorPointX + 10, anchorPointY + 20)
                    vertices = [left, right, bottom]
                    drawTriangles(window,vertices,fill)
            else:
                if j == 5:
                    pass
                else:
                    anchorPointX = topLeftX + (20*j)
                    # equilateral triangle
                    left = Point(anchorPointX, anchorPointY)
                    right = Point(anchorPointX + 20, anchorPointY)
                    bottom = Point(anchorPointX + 10, anchorPointY + 20)
                    vertices = [left, right, bottom]
                    drawTriangles(window,vertices,fill)
                    
                    
def linesPatch(window, topLeftX, topLeftY, colour): 
        end = Point(topLeftX + 100, topLeftY + 100)
        for x in range(topLeftX,110 + topLeftX, 10):
            line = Line(Point(x,topLeftY), end)
            end.move(-10,0)
            line.setOutline(colour)
            line.draw(window)
            
        end = Point(topLeftX + 100, topLeftY + 100)
        for y in range(topLeftY,110 + topLeftY, 10):
            line = Line(Point(topLeftX,y), end)
            end.move(0,-10)
            line.setOutline(colour)
            line.draw(window)
            
            
def drawTrianglePatch(window, rows, coulombs, anchorPointX, anchorPointY,
                                                    colourList, section): 
    for i in range(rows):
        topLeftY = anchorPointY + 100*i
        for j in range(coulombs):
            topLeftX = anchorPointX + 100*j
            if section == "right":
                colourChoice = 2
            else:
                colourChoice = colourChoser(colourList, topLeftX, 
                                             topLeftY, coulombs, i)
            trianglePatch(window, topLeftX, topLeftY, colourList[colourChoice])
                
                
def drawLinesPatch(window, rows, coulombs, colourList): 
    for i in range(rows+1):
        topLeftY = rows*100 + 100*i
        for j in range(coulombs):
            topLeftX = 0 + 100*j         
            colourChoice = colourChoser(colourList, topLeftX, 
                                        topLeftY, coulombs, i)
            linesPatch(window, topLeftX, topLeftY, colourList[colourChoice])
            
            
def drawFullPatchwork(size, colourList):
    window =  GraphWin("Patchwork", size*100, size*100)
    # loop controls and the top of the patturn
    coulombs = size 
    rows = int(size - size*0.45)
    anchorPointX = 0  
    anchorPointY = 0 
    
    # draw the patchwork for the lower left of the screen 
    coulombs = coulombs - rows
    drawLinesPatch(window, rows, coulombs, colourList)
    
    # draw the patchwork for the top section of the screen
    coulombs = size
    section = "top"
    drawTrianglePatch(window, rows, coulombs, anchorPointX, anchorPointY,
                                                        colourList,section)
    
    # draw the patchwork for the lower right section of the screen
    anchorPointY = rows*100
    rows = int(size - size*0.45) + 1
    coulombs = coulombs - rows
    anchorPointX = rows * 100
    section = "right"
    drawTrianglePatch(window, rows, coulombs, anchorPointX, anchorPointY,
                                                      colourList, section) 
    return(window)
    
    
def colourChoser(colourList, topLeftX, topLeftY, coulombs, i):
    colourChoice = 1
    if topLeftX < (coulombs*100 - (100*i))-100:
        colourChoice  = 0
    elif topLeftX > (coulombs*100 - (100*i))-100:
        colourChoice  = 2
    else:
        colourChoice  = 1
    return (colourChoice)
        
        
def redrawer(mouseX, mouseY, listX, window, size, colourList, section):
    simulatedI = int(math.floor(mouseY/100))
    listX.append(mouseX)
    clickCount = listX.count(mouseX)
    if clickCount >= 3:
        for i in range(clickCount):
            listX.remove(mouseX)
            clickCount = 0
            
    startColour = colourChoser(colourList, mouseX, mouseY, size, simulatedI)
    finalColour = startColour + clickCount
    if finalColour == 4:
        finalColour = 1
    elif finalColour == 3:
        finalColour = 0
    if section == "left":
        linesPatch(window, mouseX, mouseY, colourList[finalColour])
    else:
        trianglePatch(window, mouseX, mouseY, colourList[finalColour])
        
        
def colourChanger(window, size, colourList):
    previousClickX = [[]for i in range(size)]
    
    while not window.isClosed():
        mouseClickPoint = window.getMouse()
        mouseX = mouseClickPoint.getX()
        mouseY = mouseClickPoint.getY()
        
        if mouseX >=100*size or mouseY >= size*100:
            print("oops! Thats off the grid! Try again a little closer in")  
            
        elif  mouseY <= int(size -(size*0.45))*100:
            mouseX = int(mouseX/100)*100
            mouseY = int(mouseY/100)*100 
            section = "top"
            listLocation = int(mouseY/100)
            listX = previousClickX[listLocation]
            redrawer(mouseX, mouseY, listX, window, size, colourList, section)
            
        elif mouseY >= int(size -(size*0.45))*100 \
                        and mouseX >=int(size+1 -(size*0.45))*100 :
            mouseX = int(mouseX/100)*100
            mouseY = int(mouseY/100)*100
            section = "right"
            listLocation = int(mouseY/100)
            listX = previousClickX[listLocation]
            redrawer(mouseX, mouseY, listX, window, size, colourList, section)
            
        else:
            mouseX = int(mouseX/100)*100
            mouseY = int(mouseY/100)*100
            section = "left"
            listLocation = int(mouseY/100)
            listX = previousClickX[listLocation]
            redrawer(mouseX, mouseY, listX, window, size, colourList, section)
main()