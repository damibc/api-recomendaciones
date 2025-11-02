from fastapi import FastAPI
from .anime_service import AnimeService

app = FastAPI()
service = AnimeService()

@app.get("/version")
def version():
    return {"version": service.get_version()}

@app.post("/train")
def train():
    result = service.train()
    return {"status": result}

@app.get("/recommend/{user_id}")
def recommend(user_id):
    recomendaciones = service.get_recommendations(user_id)
    return {"user_id": user_id, "recomendaciones": recomendaciones}