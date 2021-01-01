from PIL import Image
im = Image.open("mona_lisa_144x255.bmp")
im2 = im.rotate(90)
im2.save("1.bmp")
