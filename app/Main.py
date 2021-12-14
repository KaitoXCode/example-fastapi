from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from .router import posts, user, auth, vote
from .config import settings


print(settings.database_password)

#  this command is no longer needed, as alembic has been incorporated into programme
#  models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(posts.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")  # Activate API
def message1():
    return {"message": "Welcome to my API!"}


# CRUD (based application)
# C = create [POST(/posts (@app.post("/posts"))]
# R = read [GET(/posts (@app.post("/posts"));
#               /posts/:id (@app.post("/posts/{id}"))]
# U = Update [PUT/PATCH(/posts/:id (@app.post("/posts/{id}"))]
# D = Delete [DELETE(/posts/:id (@app.post("/posts/{id}"))]
