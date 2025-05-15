from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
router = APIRouter()

@router.get("/", response_class=HTMLResponse)
async def read_home(request: Request):
    return templates.TemplateResponse("Niña.html", {"request": request})
@router.get("/Html", response_class=HTMLResponse)
async def pure_html():
    html_content="""
    <html>
        <head>
        <title>Niñagorda</title>
        </head>
        <body>
        <h1>Look ma! HTML!</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)