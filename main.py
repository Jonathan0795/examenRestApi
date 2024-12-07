import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from models import alumno_model

from router import estudiante_router
from database import engine

app = FastAPI()
load_dotenv()

alumno_model.Base.metadata.create_all(engine)
app.include_router(estudiante_router.router)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["Authorization", "Content-Type"],
)


async def main():
    config = uvicorn.Config("main:app", log_level="info")
    server = uvicorn.Server(config)
    await server.serve()
