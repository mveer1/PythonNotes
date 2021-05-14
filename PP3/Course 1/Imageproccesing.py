#In order to manipulate an image, we need to be able to access individual pixels. This capability is provided by a module called image, provided in ActiveCode 1. The image module defines two classes: Image and Pixel.

#If you want to explore image processing on your own outside of the browser you can install the cImage module from http://pypi.org.

#Each Pixel object has three attributes: the red intensity, the green intensity, and the blue intensity. A pixel provides three methods that allow us to ask for the intensity values. They are called getRed, getGreen, and getBlue. In addition, we can ask a pixel to change an intensity value using its setRed, setGreen, and setBlue methods.

Pixel(20,100,50)  #Create a new pixel with 20 red, 100 green, and 50 blue.
getRed() example r = p.getRed()  #Return the red component intensity. #samefor b g
setRed() example p.setRed(100)  #Set the red component intensity to 100. #samefor b g

#heres a example
import image
p = image.Pixel(45, 76, 200)
print(p.getRed())
p.setRed(66)
print(p.getRed())
p.setBlue(p.getGreen())
print(p.getGreen(), p.getBlue())

#that was all about, pixels.  now image objects

Image(filename) img = image.Image(“cy.png”)     Create an Image object from the file cy.png.

EmptyImage() img = image.EmptyImage(100,200)     Create an Image object that has all “White” pixels

getWidth() w = img.getWidth()   Return the width of the image in pixels.

getHeight() h = img.getHeight()    Return the height of the image in pixels.

getPixel(col,row)  p = img.getPixel(35,86)    Return the pixel at column 35, row 86.

setPixel(col,row,p)   img.setPixel(100,50,mp)    Set the pixel at column 100, row 50 to be mp.

#a simple example
import image
img = image.Image("luther.jpg")
print(img.getWidth())
print(img.getHeight())
p = img.getPixel(45, 55)  #refer above notes if you forget
print(p.getRed(), p.getGreen(), p.getBlue())


#make a negative, of a Image
import image
img = image.Image("luther.jpg")
win = image.ImageWin(img.getWidth(), img.getHeight())       #opens a windoe, or better decribes a window object
img.draw(win)          #opens a window with the image
img.setDelay(1,15)   # setDelay(0) turns off animation, 15 is slowest, 1 is fastest, first argument for col, second for row
win.exitonclick()
for row in range(img.getHeight()):
    for col in range(img.getWidth()):
        p = img.getPixel(col, row)
        newred = 255 - p.getRed()
        newgreen = 255 - p.getGreen()
        newblue = 255 - p.getBlue()

        newpixel = image.Pixel(newred, newgreen, newblue)
        img.setPixel(col, row, newpixel)
img.draw(win)
win.exitonclick()

#For example, you can create a gray scale pixel by averaging the red, green and blue intensities and then using that value for all intensities.
#From the gray scale you can create black white by setting a threshold and selecting to either insert a white pixel for a black pixel into the empty image.
#You can also do some complex arithmetic and create interesting effects, such as Sepia Tone
