# Original code from:
# http://code.activestate.com/recipes/578590-mandelbrot-fractal-using-tkinter/

# import the libraries you'll need
import tkinter
from tkinter import *

# recursive mandelbrot function gives us the number of iterations to escape
def mandelbrot(z, c, count):
	z = z*z+c
	count = count+1
	if abs(z)>=2 or count > 200:
		return count 
	else:
		return mandelbrot(z, c, count)	


# variables we will use throughout the program
WIDTH = 640 # width and height of our picture in pixels
HEIGHT = 640
xmin = 0.2750244140625000000  # the zoom we want to see 
xmax = 0.2782470703125000000
ymin = -0.009082031249999956 
ymax = -0.005859374999999955
maxIt = 255 # max iterations; corresponds to color

# create a new Tkinter window
window1 = Tk()

# create a canvas, and place it in the window
canvas1 = Canvas(window1, width = WIDTH, height = HEIGHT, bg = "#000000")

# set up the canvas so it can hold a picture
img = PhotoImage(width = WIDTH, height = HEIGHT)
canvas1.create_image((0, 0), image = img, state = "normal", anchor = tkinter.NW)

# loop through all the pixels in the image
for row in range(HEIGHT):
    for col in range(WIDTH):
    	# calculate C for each pixel
        c = complex(((((xmax-xmin)/WIDTH)*col+xmin)),((((ymax-ymin)/HEIGHT)*row+ymin)))
        # set z to 0
        z = complex(0.0,0.0)

        # execute the mandelbrot calculation
        r = mandelbrot(z,c,0)

        # use the mandelbrot result to create a color
        rd = hex(255%r)[2:].zfill(2)
        gr = hex(150%r)[2:].zfill(2)
        bl = hex(200%r)[2:].zfill(2)

        # update the pixel at the current position to hold
        # the color we created with the mandelbrot result
        img.put("#" + rd + gr + bl, (col, row))

# update the canvas and display our drawing
canvas1.pack()

# variables we will use throughout the program
xmin = -0.06436482179262383  # the zoom we want to see 
xmax = -0.06333884273211150
ymin = 0.664795215523597900
ymax = 0.665821194584110200

# create a new Tkinter window
window2 = Toplevel()

# create a canvas, and place it in the window
canvas2 = Canvas(window2, width = WIDTH, height = HEIGHT, bg = "#000000")

# set up the canvas so it can hold a picture
img2 = PhotoImage(width = WIDTH, height = HEIGHT)
canvas2.create_image((0, 0), image = img2, state = "normal", anchor = tkinter.NW)

# loop through all the pixels in the image
for row in range(HEIGHT):
    for col in range(WIDTH):
    	# calculate C for each pixel
        c = complex(((((xmax-xmin)/WIDTH)*col+xmin)),((((ymax-ymin)/HEIGHT)*row+ymin)))
        # set z to 0
        z = complex(0.0,0.0)

        # execute the mandelbrot calculation
        r = mandelbrot(z,c,0)

        # use the mandelbrot result to create a color
        rd = hex(0)[2:].zfill(2)
        gr = hex(abs(100-r))[2:].zfill(2)
        bl = hex((300*r)%5)[2:].zfill(2)

        # update the pixel at the current position to hold
        # the color we created with the mandelbrot result
        img2.put("#" + rd + gr + bl, (col, row))

# update the canvas and display our drawing
canvas2.pack()

# variables we will use throughout the program
xmin = -0.75439956665039070  # the zoom we want to see 
xmax = -0.75276557922363290
ymin = -0.04768409729003910
ymax = -0.04605010986328129

# create a new Tkinter window
window3 = Toplevel()

# create a canvas, and place it in the window
canvas3 = Canvas(window3, width = WIDTH, height = HEIGHT, bg = "#000000")

# set up the canvas so it can hold a picture
img3 = PhotoImage(width = WIDTH, height = HEIGHT)
canvas3.create_image((0, 0), image = img3, state = "normal", anchor = tkinter.NW)

# loop through all the pixels in the image
for row in range(HEIGHT):
    for col in range(WIDTH):
    	# calculate C for each pixel
        c = complex(((((xmax-xmin)/WIDTH)*col+xmin)),((((ymax-ymin)/HEIGHT)*row+ymin)))
        # set z to 0
        z = complex(0.0,0.0)

        # execute the mandelbrot calculation
        r = mandelbrot(z,c,0)

        # use the mandelbrot result to create a color
        rd = hex(175%r)[2:].zfill(2)
        gr = hex(200%r)[2:].zfill(2)
        bl = hex(125%r)[2:].zfill(2)

        # update the pixel at the current position to hold
        # the color we created with the mandelbrot result
        img3.put("#" + rd + gr + bl, (col, row))

# update the canvas and display our drawing
canvas3.pack()
mainloop()






