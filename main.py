from initial import * 
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, JSONResponse
from typing import List
import json
from pydantic import BaseModel

f = open('./productsWImage.json', 'r')
json_product = json.loads(f.read() )


app = FastAPI()

image_urls = [
    "https://example.com/image1.jpg",
    "https://example.com/image2.jpg",
    "https://example.com/image3.jpg",
    # Add more image URLs as needed
]

class ProductId(BaseModel):
    productId: str

# Replace this with your actual data or logic to fetch images from the trained model
# For simplicity, a list of image URLs is used here.


# Serve static files (HTML, CSS, JS)
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def read_root():
    return """
    <html>
        <head>
            <title>Image Viewer</title>
            <link rel="stylesheet" type="text/css" href="/static/style.css">
            <script defer src="/static/script.js"></script>
        </head>
        <body>
            <div id="image-container">
                <!-- Images will be dynamically loaded here using JavaScript -->
            </div>
        </body>
    </html> 
    """


@app.get("/api/images", response_class=JSONResponse)
async def get_images():
    newProduct = []
    for product in json_product:
        newProduct.append(product["images"])
 
    return json_product
@app.post("/api/product", response_class=JSONResponse )
async def post_product(productId: ProductId ):
    topKProduct = recommend( productId, 5 )
    recommended_product = []

    for product in topKProduct:
        for p in json_product:
            if p['_id'] == product:
                recommended_product.append( p ) 
    
    return recommended_product 
