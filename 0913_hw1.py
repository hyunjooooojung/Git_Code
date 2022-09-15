class Area:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    #가로의 길이 width를 받는 메소드
    def set_width(self, width):
        self.width = width

    #세로의 길이 height를 받는 메소드
    def set_height(self, height):
        self.height = height

    #사각형의 넓이를 구하는 메소드
    def square(self):
        return self.width * self.height
    
    #삼각형의 넓이를 구하는 메소드
    def triangle(self):
        return (self.width * self.height) / 2

    #원의 넓이를 구하는 메소드(원의 지름 = width)
    def circle(self):
        return ((self.width/2)**2 * 3.14)


        
area = Area(10, 20)

print(area.square()) # 사각형의 넓이
print(area.triangle()) # 삼각형의 넓이
print(area.circle()) # 원의 넓이

