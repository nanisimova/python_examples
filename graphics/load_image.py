from PIL import Image
import requests

url = 'http://some-domain-name-1.com/image-name.png'

try:
    resp = requests.get(url, stream=True).raw
except requests.exceptions.RequestException as err:
    print(err)
    exit()

try:
    img = Image.open(resp)
except IOError as err:
    print(err)
    exit()

img.save('image.png', 'png')
img.show()