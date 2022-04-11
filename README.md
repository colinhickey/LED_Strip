# LED Strip
Tools for drawing long exposure images with a NeoPixel LED strip

Basic Python that addresses LEDs on a 144 pixel strip and turns the LED the colour of the pixel in the image one row at a time.

Play with the update time per row to adjust the drawing time.

Suggested improvements:
- add image filename as an argument when the script is run, rather than hardcoding it in the script.
- use PIL to resize images to the required 144 pixel width and whatever height results so that any image can be used instead of requiring correctly sized image.

Example Input image:
(Note black background, and width of 144 pixels, but arbitrary length)

![TREX input image](trex.bmp "Example image to use with black background")

Example long exposure photo of the image being cast to LED strip:

![T-Rex end result photo](DSC_4721.jpg "End result example, long expsure photo")
