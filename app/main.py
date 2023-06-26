import fastapi
from app.routers import skills

app = fastapi.FastAPI(title="Job hunting helper")
app.include_router(router=skills.router_skills)
