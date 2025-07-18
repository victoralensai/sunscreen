from fastapi import FastAPI
from src.meteo import Meteo
from config import settings

app = FastAPI(
    title="Sunscreen Advisor API",
    description="This API tells you if you should put sunscreen today based on UV index.",
    version="0.1.0",
    contact={
        "name": "Victor Jean",
        "url": "https://vctor.me",
        "email": "hello@vctor.me",
    },
)


@app.get("/")
async def root():
    return {"message": "Should I put sunscreen on today?"}

@app.get("/uv/current")
async def get_current_uv(location:str):
    meteo = Meteo(settings.api_key, location)
    return {"uv_index": meteo.get_weather_uv()}

@app.get("/uv/forecast")
async def get_forecast_uv(location:str):
    meteo = Meteo(settings.api_key, location)
    return {"forecast_uv": meteo.get_forecast_uv()}

@app.get("/sunscreen/now")
async def should_i_put_sunscreen_now(location:str):
    meteo = Meteo(settings.api_key, location)
    return {"should_put_sunscreen": meteo.should_i_put_sunscreen_right_now()}

@app.get("/uv/max-today")
async def get_max_uv_today(location:str):
    meteo = Meteo(settings.api_key, location)
    return {"max_uv": meteo.get_max_uv_today()}

@app.get("/sunscreen/hours")
async def get_sunscreen_hours(location:str):
    meteo = Meteo(settings.api_key, location)
    return {"sunscreen_hours": meteo.hours_above_uv_threshold()}
