import json
import os
import sys
from contextlib import asynccontextmanager
from datetime import date, timedelta

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from dotenv import load_dotenv

load_dotenv()

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from bot.bot import send_planning, client, TOKEN

PLANNING_PATH = "./data/planning.json"
scheduler = AsyncIOScheduler(timezone="Europe/Paris")


def load_planning():
    with open(PLANNING_PATH, "r") as f:
        return json.load(f)


def save_planning(data):
    with open(PLANNING_PATH, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


async def auto_send():
    data = load_planning()
    today = date.today()
    in7 = today + timedelta(days=7)
    sessions = [
        s for s in data["sessions"]
        if today <= date.fromisoformat(s["date"]) <= in7
    ]
    print(f"⏰ Envoi automatique — {len(sessions)} session(s)")
    await send_planning(sessions)


@asynccontextmanager
async def lifespan(app: FastAPI):
    import asyncio
    asyncio.create_task(client.start(TOKEN))
    scheduler.add_job(auto_send, "cron", hour=20, minute=0)
    scheduler.start()
    yield
    scheduler.shutdown()


app = FastAPI(lifespan=lifespan)
app.mount("/static", StaticFiles(directory="web/public"), name="static")


class Planning(BaseModel):
    sessions: list
    games: list = []


@app.get("/")
def index():
    return FileResponse("web/public/index.html")


@app.get("/api/planning")
def get_planning():
    return load_planning()


@app.post("/api/planning")
def post_planning(data: Planning):
    save_planning(data.dict())
    return {"success": True}


@app.post("/api/send-discord")
async def send_discord():
    from datetime import date, timedelta
    data = load_planning()
    today = date.today()
    # Lundi de la semaine courante
    monday = today - timedelta(days=today.weekday())
    sunday = monday + timedelta(days=6)
    sessions = [
        s for s in data["sessions"]
        if monday <= date.fromisoformat(s["date"]) <= sunday
    ]
    await send_planning(sessions)
    return {"success": True}