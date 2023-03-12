import base64

import requests


TEXT = "cat, dog, person drinking tea"
IMAGE = "cat_and_dog_output.png"


def image_to_base64(image_path: str):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return encoded_string


if __name__ == "__main__":
    data = {
        "image": image_to_base64(IMAGE),
        "text": TEXT
    }
    response = requests.post("http://localhost:8000/image_text_search", json=data)
    # get all keys
    keys = response.json().keys()
    for key in keys:
        if key != "suggested_captions":
            print(key, response.json()[key])
    print("\nSuggested Captions: ")
    for caption in response.json()["suggested_captions"]:
        print(caption)

