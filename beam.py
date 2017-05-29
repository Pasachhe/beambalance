import math

class beam:
    def centroid(self):
        return 1 / 3 * (self.x0 + self.x1 + self.x2), 1 / 3 * (self.y0 + self.y1 + self.y2)

    def __init__(self, canvas, x, y, width, height, turnspeed):
        self._d = {'Left':1, 'Right':-1}

        self.canvas = canvas
        self.width = width
        self.height = height
        self.speed = 0
        self.turnspeed = turnspeed
       

        self.x0, self.y0 = x, y

        self.bearing = -math.pi / 2

        self.x1 = self.x0 + self.width / 2
        self.y1 = self.y0 - self.height

        self.x2 = self.x0 + self.width
        self.y2 = self.y0

        #flake ko coordinates

        self.x3= self.x0 - self.width * 2.5
        self.y3= self.y0

        #3 ra 4 ko bich ma hune plate haru

        self.x31= self.x0 - self.width * 3.5
        self.y31= self.y0

        self.x32= self.x0 - self.width * 3.5
        self.y32= self.y0 - self.height * 0.25

        self.x33= self.x0 - self.width * 1.5
        self.y33= self.y0 - self.height * 0.25

        self.x34= self.x0 - self.width * 1.5
        self.y34= self.y0

        #next plate

        self.x35= self.x0 + self.width * 5 / 2
        self.y35= self.y0

        self.x36= self.x0 + self.width * 5 / 2
        self.y36= self.y0 - self.height * 0.25

        self.x37= self.x0 + self.width * 4.5
        self.y37= self.y0 - self.height /4

        self.x38= self.x0 + self.width * 4.5
        self.y38= self.y0




        

        self.x4= self.x0 + self.width * 3.5
        self.y4= self.y0

        self.x5= self.x0 + self.width * 3.5
        self.y5= self.y0 + self.height / 2
        
        self.x6= self.x0 - self.width * 2.5
        self.y6= self.y0 + self.height / 2


        #base ko coordinates

        self.x7= self.x0 + self.width * 0.5
        self.y7= self.y0

        self.x8= self.x0 - self.width
        self.y8= self.y0 + self.height * 1.5

        self.x9= self.x0 - self.width * 3.5
        self.y9= self.y0 + self.height * 1.5

        self.x10= self.x0 - self.width * 3.5
        self.y10= self.y0 + self.height * 2.5

        self.x11= self.x0 + self.width * 4.5
        self.y11= self.y0 + self.height * 2.5

        self.x12= self.x0 + self.width * 4.5
        self.y12= self.y0 + self.height * 1.5

        self.x13= self.x0 + self.width * 2
        self.y13= self.y0 + self.height * 1.5

        #saman ko coordinates

        self.x41= self.x0 - self.width * 3.25
        self.y41= self.y0 - self.height / 4
        
        self.x42= self.x0 - self.width * 3.25
        self.y42= self.y0 - self.height * 2

        self.x43= self.x0 - self.width * 1.75
        self.y43= self.y0 - self.height * 2

        self.x44= self.x0 - self.width * 1.75
        self.y44= self.y0 - self.height / 4

        #weight ko coordinate
        self.x51= self.x0 + self.width * 3
        self.y51= self.y0 - self.height / 4
        
        self.x52= self.x0 + self.width * 3
        self.y52= self.y0 - self.height * 0.75

        self.x53= self.x0 + self.width * 4
        self.y53= self.y0 - self.height * 0.75

        self.x54= self.x0 + self.width * 4
        self.y54= self.y0 - self.height / 4

        


        self.x, self.y = self.centroid()
        #self.beam = self.canvas.create_polygon((self.x41, self.y41,self.x42, self.y42,self.x43, self.y43,self.x44, self.y44),outline="green",width=5)
        self.beam = self.canvas.create_polygon((self.x7, self.y7, self.x8, self.y8, self.x9, self.y9, self.x10, self.y10,self.x11, self.y11, self.x12, self.y12,self.x13, self.y13 ), outline="red", width=3)
        self.beam = self.canvas.create_polygon((self.x0, self.y0, self.x1, self.y1, self.x2, self.y2), outline="white", width=3)
        self.beam = self.canvas.create_polygon((self.x2, self.y2, self.x35, self.y35, self.x36, self.y36, self.x51, self.y51, self.x52, self.y52, self.x53, self.y53, self.x54, self.y54, self.x51, self.y51, self.x37, self.y37, self.x38, self.y38, self.x4, self.y4, self.x5, self.y5, self.x6, self.y6 , self.x3, self.y3, self.x31, self.y31, self.x32, self.y32, self.x41, self.y41, self.x42, self.y42, self.x43, self.y43, self.x44, self.y44, self.x41, self.y41, self.x33, self.y33, self.x34, self.y34), outline="yellow",width=3)

    def changeCoords(self):
        self.canvas.coords(self.beam, self.x0, self.y0, self.x1, self.y1, self.x2, self.y2, self.x35, self.y35, self.x36, self.y36, self.x51, self.y51, self.x52, self.y52, self.x53, self.y53, self.x54, self.y54, self.x51, self.y51, self.x37, self.y37, self.x38, self.y38, self.x4, self.y4, self.x5, self.y5, self.x6, self.y6, self.x3, self.y3, self.x31, self.y31, self.x32, self.y32,self.x41, self.y41, self.x42, self.y42, self.x43, self.y43, self.x44, self.y44, self.x41, self.y41, self.x33, self.y33, self.x34, self.y34)
        #self.canvas.coords(self.beam, self.x41, self.y41, self.x42, self.y42, self.x43, self.y43, self.x44, self.y44)
        
    def rotate(self, event=None):
        t = self._d[event.keysym] * self.turnspeed * math.pi / 180
        # the trig functions generally take radians as their arguments rather than degrees; pi/180 radians is equal to 1 degree

        self.bearing -= t

        def _rot(x, y):
            x -= self.x
            y -= self.y
            _x = x * math.cos(t) + y * math.sin(t)
            _y = -x * math.sin(t) + y * math.cos(t)
            return _x + self.x, _y + self.y

        self.x0, self.y0 = _rot(self.x0, self.y0)
        self.x1, self.y1 = _rot(self.x1, self.y1)
        self.x2, self.y2 = _rot(self.x2, self.y2)
        self.x3, self.y3 = _rot(self.x3, self.y3)
        self.x31, self.y31 = _rot(self.x31, self.y31)
        self.x32, self.y32 = _rot(self.x32, self.y32)

        self.x41, self.y41 = _rot(self.x41, self.y41)
        self.x42, self.y42 = _rot(self.x42, self.y42)
        self.x43, self.y43 = _rot(self.x43, self.y43)
        self.x44, self.y44 = _rot(self.x44, self.y44)
        
        self.x33, self.y33 = _rot(self.x33, self.y33)
        self.x34, self.y34 = _rot(self.x34, self.y34)
        self.x35, self.y35 = _rot(self.x35, self.y35)
        self.x36, self.y36 = _rot(self.x36, self.y36)

        self.x51, self.y51 = _rot(self.x51, self.y51)
        self.x52, self.y52 = _rot(self.x52, self.y52)
        self.x53, self.y53 = _rot(self.x53, self.y53)
        self.x54, self.y54 = _rot(self.x54, self.y54)

        
        self.x37, self.y37 = _rot(self.x37, self.y37)
        self.x38, self.y38 = _rot(self.x38, self.y38)
        self.x4, self.y4 = _rot(self.x4, self.y4)
        self.x5, self.y5 = _rot(self.x5, self.y5)
        self.x6, self.y6 = _rot(self.x6, self.y6)
        
        self.x, self.y = self.centroid()

        self.changeCoords()


