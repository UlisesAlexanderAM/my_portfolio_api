import fastapi
from app.config import database
from app.routers import skills

database.Base.metadata.create_all(bind=database.engine)

app = fastapi.FastAPI(title="Job hunting helper")
app.include_router(router=skills.router_skills)
