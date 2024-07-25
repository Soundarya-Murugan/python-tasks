from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Setup Jinja2 templates
templates = Jinja2Templates(directory="templates")

# Example data (list of dictionaries)
items = [
    {"name": "Coffee", "description": "Coffee is a beverage brewed from roasted coffee beans."},
    {"name": "Tea", "description": "tea, beverage produced by steeping in freshly boiled water the young leaves and leaf buds of the tea plant, Camellia sinensis."},
    {"name": "Milk", "description": "Milk is an emulsion or colloid of butterfat globules within a water-based fluid that contains dissolved carbohydrates and protein aggregates with minerals."}
]

# Define route to render HTML page
@app.get("/", response_class=HTMLResponse)
async def read_items(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "items": items})
