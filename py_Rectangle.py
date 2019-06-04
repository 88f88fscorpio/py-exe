from Rectangle import Rectangle

def main():
    length1=int(input())
    length2=int(input())
    width1=int(input())
    width2=int(input())

    rectangle1=Rectangle(length1,width1)
    rectangle2=Rectangle(length2,width2)

    print(rectangle1.getArea()," ",rectangle1.getPerimeter())
    print(rectangle2.getArea()," ",rectangle2.getPerimeter())

    rectangle2.setLength(50)
    rectangle2.setWidth(25)

    print(rectangle2.getArea()," ",rectangle2.getPerimeter())

main()