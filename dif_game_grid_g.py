# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 17:22:28 2026

@author: Kamila Dudzińska

Supporting module with grid for an image.

Library: pillow

Pillow - library used for opening, manipulating and saving image file formats.
Allows resizing, cropping and adding geometric shapes onto graphic. 
        
"""

from PIL import Image, ImageDraw, ImageFont

# loading
picture_path = 'images/dif.png'    
out_path = "output_grid.png"
STEP = 50                     # odstęp siatki w pikselach

# opening
img = Image.open(picture_path).convert("RGBA")
w, h = img.size

draw = ImageDraw.Draw(img)

# font 
try:
    font = ImageFont.truetype("arial.ttf", 16)
except:
    font = ImageFont.load_default()

# vertical lines and description
for x in range(0, w + 1, STEP):
    # linia pionowa
    draw.line([(x, 0), (x, h)], fill=(255, 255, 255, 160), width=1)
    label = f"x = {x}"
    draw.text((x + 2, 2), f"x={x}", fill=(255, 255, 255, 180), font=font)

# horizontal lines and description
for y in range(0, h + 1, STEP):
    # linia pozioma
    draw.line([(0, y), (w, y)], fill=(255, 255, 2500, 160), width=1)
    label = f"y = {y}"
    draw.text((2, y + 2), label, fill=(255, 255, 255, 180), font=font)

# save image
img.save(out_path)
print("Zapisano plik:", out_path)
