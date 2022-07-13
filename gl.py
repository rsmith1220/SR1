#Rebecca Smith
#Seccion 20


import struct

def char(c):
    #ocupa 1 byte
    return struct.pack('=c'. c.encode('ascii'))


def word(w):
    #ocupa 2 bytes
    return struct.pack('=h', w)

def dword(d):
    #ocupa 4 bytes
    return struct.pack('=l',d)


def color(r,g,b): #una funcion que va a crear un color
    return bytes([int(b*255),
                int(g*255),
                int(r*255)])


class Renderer(object):#de que size va a ser la imagen
    def __init__(self, width, height): #este es el gl init

        self.width=width
        self.height=height

        self.clearColor = color(0,0,0)
        self.currColor = color(1,1,1)

        self.glViewport(0,0,self.width,self.height)

        self.glClear()

    def glViewport(self, posX, posY, width, height):
        self.vpX = posX
        self.vpY = posY
        self.vpWidth = width
        self.vpHeight = height

    def glClearColor(self,r,g,b): #color de fondo de la imagen
        self.clearColor = color(r,g,b)

    def glColor(self,r,g,b):
        self.currColor=color(r,g,b)

    def glClear(self): #borrar todos los pixeles de fondo
        self.pixels=[[self.clearColor for y in range (self.height)]for x in range(self.width)]


    def glClearViewport(self, clr = None): #window coordinates
            for x in range(self.vpX,self.vpX + self.vpWidth):
                for y in range(self.vpY,self.vpY + self.vpHeight):
                    self.glPoint(x,y,clr)

    def glPoint(self,x,y,clr=None):
        if (0 <= x < self.width) and(0<= y < self.height):
            self.pixels[x][y]=clr or self.currColor

    def glCreateWindow(self, width, height):
        self.width = width
        self.height = height
        self.glClear()


    def glPoint_vp(self, ndcX,ndcY, clr=None): #NDC
        x=(ndcX+1)*(self.vpWidth/2)+self.vpX
        y=(ndcY+1)*(self.vpHeight/2)+self.vpY

        x= int(x)
        y=int(y)

        self.glPoint(x,y,clr)

    def glFinish(self, filename):
        with open(filename, "wb") as file:
            #se crea el heder / encabezado de la imagen
            file.write(bytes('B'.encode('ascii')))
            file.write(bytes('M'.encode('ascii')))
            file.write(dword(14 + 40 +(self.width * self.height * 3)))#size del archivo / cantidad de bytes que va a ser el archivo
            file.write(dword(0))
            file.write(dword(14 + 40))

            #informacion del header
            file.write(dword(40))
            file.write(dword(self.width))
            file.write(dword(self.height))
            file.write(word(1))
            file.write(word(24))
            file.write(dword(0))
            file.write(dword(self.width * self.height * 3))
            file.write(dword(0))
            file.write(dword(0))
            file.write(dword(0))
            file.write(dword(0))

            #color table
            for y in range (self.height):
                for x in range(self.width):
                    file.write(self.pixels[x][y])