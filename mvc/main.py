from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List
from starlette.requests import Request

app = FastAPI()

templates = Jinja2Templates(directory="templates")

class UserModel:
    def __init__(self):
        self.users = []

    def add_user(self, user: str):
        self.users.append(user)

    def get_users(self) -> List[str]:
        return self.users
    
user_model = UserModel()

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    users = user_model.get_users()
    return templates.TemplateResponse("index.html", {"request": request, "users": users})

@app.post("/add")
async def add_user(name: str = Form(...)):
    user_model.add_user(name)
    return RedirectResponse(url="/", status_code=393)