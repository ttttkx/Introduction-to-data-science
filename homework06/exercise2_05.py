import os
from PIL import Image

infile = "C:\\Users\\tong\\Pictures\\Camera Roll\\R-C (5).jpg"
outfile = "C:\\Users\\tong\\Pictures\\Camera Roll\\R-C (5)-gray.jpg"

img = Image.open(infile).convert('L')
out = img.resize((256,256),Image.LANCZOS)

out.save(outfile)
