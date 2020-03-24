from Kennedy import Kennedy
from Carpenter import Carpenter
import turtle

def main():
        # get user input
        print("Ellipse center point")
        x = int(input("x: "))
        y = int(input("y: "))
        print("Ellipse Property")
        a = int(input("x radius: "))
        b = int(input("y radius: "))
        print('Center point is (',x,',',y,')')
        print('Most top point is (',x+a,',0)')
        print('Most right point is (0,',y+b,')')

        # translation to origin
        x, y, tx, ty = transToOrigin(x, y)

        # kennedy
        k = Kennedy(a, b)
        k.midpoint()
        # carpenter
        c = Carpenter(a, b)
        c.midpoint()

        # mirror x and y
        k.negResult()
        c.negResult()

        # translation back to (x,y) point
        k.xResult, k.yResult = transback(k.xResult, k.yResult, tx, ty)
        k.xNegResult, k.yNegResult = transback(k.xNegResult, k.yNegResult, tx, ty)
        c.xResult, c.yResult = transback(c.xResult, c.yResult, tx, ty)
        c.xNegResult, c.yNegResult = transback(c.xNegResult, c.yNegResult, tx, ty)

        print("Kennedy")
        print("quadrant 1") # (x,y)
        printPoint(k.xResult, k.yResult)
        print("")
        print("quadrant 2") # (-x,y)
        printPoint(k.xNegResult, k.yResult)
        print("")
        print("quadrant 3") # (-x,-y)
        printPoint(k.xNegResult, k.yNegResult)
        print("")
        print("quadrant 4") # (x,-y)
        printPoint(k.xResult, k.yNegResult)
        print("")

        print("Carpenter")
        print("quadrant 1")  # (x,y)
        printPoint(c.xResult, c.yResult)
        print("")
        print("quadrant 2")  # (-x,y)
        printPoint(c.xNegResult, c.yResult)
        print("")
        print("quadrant 3")  # (-x,-y)
        printPoint(c.xNegResult, c.yNegResult)
        print("")
        print("quadrant 4")  # (x,-y)
        printPoint(c.xResult, c.yNegResult)
        print("")

        # setup for drawing graph
        turtle.setup()
        turtle.penup()
        turtle.hideturtle()

        # kennedy
        draw(k.xResult, k.yResult,"blue")
        draw(k.xNegResult, k.yResult,"blue")
        draw(k.xNegResult, k.yNegResult, "blue")
        draw(k.xResult, k.yNegResult, "blue")

        # carpenter
        draw(c.xResult, c.yResult, "red")
        draw(c.xNegResult, c.yResult, "red")
        draw(c.xNegResult, c.yNegResult, "red")
        draw(c.xResult, c.yNegResult, "red")

        turtle.done()

# translate center point to origin
def transToOrigin(x, y):
    tx = -x
    ty = -y
    x = x + tx
    y = y + ty
    return x, y, tx, ty

# translate from origin to the center point
def transback(x, y, tx, ty):
    i = 0
    j = 0
    for i in range(len(x)):
        temp = x[i]
        x[i] = temp - tx
    for j in range(len(y)):
        temp = y[j]
        y[j] = temp - ty
    return x, y

# show the result in (x,y) format
def printPoint(x, y):
    i = 0
    for i in range(len(x)):
        print('(',x[i],',',y[i],')',end = ' ')

# draw graph
def draw(x,y,color):
    i = 0
    for i in range(len(x)):
        # scaling the point
        tempx = x[i] * 10
        tempy = y[i] * 10
        turtle.goto(tempx,tempy)
        turtle.dot(8,color)

if __name__ == "__main__":
    main()
