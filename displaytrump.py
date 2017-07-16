from papirus import Papirus
from papirus import PapirusImage
from papirus import PapirusText

screen = Papirus()
image = PapirusImage()
text = PapirusText()

screen.update()

image.write('/home/pi/papirus/epapertrump.bmp')

#text.write("hello")


