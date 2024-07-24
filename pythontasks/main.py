from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Setup Jinja2 templates
templates = Jinja2Templates(directory="templates")

# Example data (list of dictionaries)
items = [
    {"name": "Item 1", "description": "Description for Item 1"},
    {"name": "Item 2", "description": "Description for Item 2"},
    {"name": "Item 3", "description": "Description for Item 3"}
]

# Define route to render HTML page
@app.get("/", response_class=HTMLResponse)
async def read_items(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "items": items})
