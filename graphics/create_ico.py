from PIL import Image

filename = 'filename1.png'
try:
    fh = Image.open(filename)
    fh.thumbnail((16, 16))
    fh.save('filename2.ico')

except FileNotFoundError:
    print("File not found")