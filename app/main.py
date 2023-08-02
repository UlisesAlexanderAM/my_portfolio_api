import fastapi
from app.database import database
from app.routers import skills


app = fastapi.FastAPI(title="Job hunting helper")
app.include_router(router=skills.router_skills)


@app.get("/")
def hello_world():
    return "Hello world"
