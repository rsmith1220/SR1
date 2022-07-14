#Rebecca Smith
#Seccion 20

from gl import Renderer, color
import random

w=500
h=500

rend= Renderer(w,h)

rend.glCreateWindow(w,h)

#cuadrado en rectangulo en un rectangulo con cuadrados en las esquinas
rend.glViewport(int(w/4),int(h/4),int(w/2),int(h/2))

rend.glClearColor(0,0.5,0.5)
rend.glClear()
rend.glClearViewport(color(0.5,0,0.5)) 
rend.glPoint_vp(0,0)
rend.glPoint_vp(1,1)
rend.glPoint_vp(-1,-1)




rend.glFinish("output.bmp")