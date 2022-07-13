#Rebecca Smith
#Seccion 20

from gl import Renderer, color
import random

w=500
h=500

rend= Renderer(w,h)

rend.glCreateWindow(w,h)

#cuadrado en rectangulo en un rectangulo
rend.glViewport(int(w/4),int(h/4),int(w/2),int(h/2))

rend.glClearColor(0,0.5,0.5)
rend.glClear()
rend.glClearViewport(color(0.5,0,0.5)) 
rend.glPoint_vp(0,0)
rend.glPoint_vp(1,1)
rend.glPoint_vp(-1,-1)


#hace un punto
''' rend.glClearColor(0,0.5,0) #backgorund
rend.glColor(1,1,0) #dot colors
rend.glClear()

rend.glPoint(100,100) '''


#hace una linea hecha de pixeles
''' for i in range (512):
    rend.glPoint(i,i) '''


#hace una imaagen que parece TV static
''' for x in range(w):
    for y in range(h):
        if random.random() < 0.4:
            rend.glPoint(x,y,color(0,0,0))
        else:
            rend.glPoint(x,y,color(1,1,1)) '''

#hace una imagen que parece TV static pero con colores random
''' for x in range(w):
    for y in range(h):
        pixelColor = color(random.random(),random.random(),random.random())
        rend.glPoint(x,y,pixelColor) '''

#graficar una pendiente
''' for x in range(w):
    slope = 1
    y = slope * x 
    rend.glPoint(x,y) '''

#starfield 🚀
''' for x in range(w):
    for y in range(h):
        if random.random() > 0.99:
            size = random.randrange(0,3)

            brightness = random.random()/2 +0.5
            starColor = color(brightness,brightness,brightness)


            if size == 0:
                rend.glPoint(x,y,starColor)
            elif size == 1:
                rend.glPoint(x,y,starColor)
                rend.glPoint(x+1,y,starColor)
                rend.glPoint(x+1,y+1,starColor)
                rend.glPoint(x,y+1,starColor)
            elif size == 2:
                rend.glPoint(x,y,starColor)
                rend.glPoint(x,y+1,starColor)
                rend.glPoint(x,y-1,starColor)
                rend.glPoint(x+1,y,starColor)
                rend.glPoint(x-1,y,starColor)
 '''




rend.glFinish("output.bmp")