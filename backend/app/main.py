from fastapi import FastAPI
from app.api.routes import router
from fastapi.middleware.cors import CORSMiddleware

# create the instance of fastapi app
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# the base path
@app.get("/")
def root():
    return {"message": "Welcome to the Spanish Word API!"}

# include the routes
app.include_router(router)