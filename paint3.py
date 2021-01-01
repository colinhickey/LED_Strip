import time
import board
import neopixel
from PIL import Image

image = Image.open("trex.bmp") ##improve this by passing image as arg
image_rgb = image.convert("RGB")
width = image_rgb.width
height = image_rgb.height

##in future add image resize to 144/neopixel length

pixel_pin = board.D18
num_pixels = 144
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.4, auto_write=False, pixel_order=ORDER
)

pixels.fill((255, 0, 0))
pixels.show()
time.sleep(1)
pixels.fill((0,255,0))
pixels.show()
time.sleep(1)
pixels.fill((0,0,255))
pixels.show()
time.sleep(1)

for y in range (height):
	for x in range(width):
		pixels[x] = image_rgb.getpixel((x, y))
#		print(x, y, image_rgb.getpixel((x, y))
	pixels.show()
	time.sleep(0.01)

pixels.fill((0,0,0))
pixels.show()
