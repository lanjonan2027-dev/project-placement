from rembg import remove
from PIL import Image

input = Image.open("")

putput = remove(input)
output.save("output.png")