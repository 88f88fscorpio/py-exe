class Rectangle:
    def __init__(self,length=1,width=1):
        self.__length=length
        self.__width=width

    def setLength(self,nlength):
        self.__length=nlength

    def setWidth(self,nwidth):
        self.__width=nwidth

    def getLength(self):
        return self.__length
    
    def getWidth(self):
        return self.__width

    def getArea(self):
        return self.__length*self.__width

    def getPerimeter(self):
        return 2*(self.__length+self.__width)

