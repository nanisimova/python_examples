from PIL import Image

img = Image.open("abstract.png")
wmark = Image.open("logo.png")

# Red, Green, Blue, Alpha
marked = Image.new('RGBA', (300, 218), (0, 0, 0, 0)) # 300 - width img, 218 - height img
marked.paste(img, (0, 0)) # (0, 0) - position
marked.paste(wmark, (0, 0), mask=wmark)

marked.save("marked.png")
marked.show()