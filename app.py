import base64
import io

from PIL import Image
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models import ImageTextSearchModel, ImageModel

from clip_image_text_search import image_text_search
from captions_generator import generate_captions


app = FastAPI(title="Image & Text Contextual Comparison API", version="0.1.0", docs_url="/docs")
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


def spilt_source(source: str) -> list[str]:
    sources = source.split(',')
    sources = [source.strip() for source in sources]
    return sources


def base64_to_image(base64_string: str):
    imgdata = base64.b64decode(base64_string)
    image = Image.open(io.BytesIO(imgdata))
    return image


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/image_text_search")
def image_text_search_api(image_text_search_model: ImageTextSearchModel):
    text = image_text_search_model.text + ", unknown"
    texts = spilt_source(text)
    image = base64_to_image(image_text_search_model.image)
    results = image_text_search(image, texts)
    results["suggested_captions"] = []
    if max(results, key=results.get) == "unknown":
        cap1 = generate_captions(image)
        results["suggested_captions"].append(cap1)

    results.pop("unknown")
    return results


@app.post("/generate_captions")
def generate_captions_api(image_model: ImageModel):
    image = base64_to_image(image_model.image)
    return generate_captions(image)


