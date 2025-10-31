from fastapi import FastAPI
from .anime_dao import AnimeDAO

app = FastAPI()
dao = AnimeDAO()

@app.get("/version")
def version():
    return {"version": dao.get_version()}

@app.post("/train")
def train():
    result = dao.train()
    return {"status": result}

@app.get("/recommend/{user_id}")
def recommend(user_id):
    recomendaciones = dao.get_recommendations(user_id)
    return {"user_id": user_id, "recomendaciones": recomendaciones}