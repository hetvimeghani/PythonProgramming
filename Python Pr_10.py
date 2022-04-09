#Hetvi Meghani - D21CE171
import img2pdf
from PIL import Image
import os
img_path = 'J:/4 sem/Python/Result.png'

pdf_path = 'J:/4 sem/Python/Result.pdf'

image = Image.open(img_path)

pdf_bytes = img2pdf.convert(image.filename)

file = open(pdf_path, "wb")

file.write(pdf_bytes)

image.close()

file.close()

print("SUCCESSFULLY MADE PDF FILE.")
