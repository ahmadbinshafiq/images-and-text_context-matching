import base64
import io

from PIL import Image
from images import cat_and_dog


def base64_to_image(base64_string: str):
    imgdata = base64.b64decode(base64_string)
    image = Image.open(io.BytesIO(imgdata))
    return image


image = base64_to_image(cat_and_dog)
print(image.size)
image.save('cat_and_dog_output.png')


