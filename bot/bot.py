import discord
import json
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

intents = discord.Intents.default()
client = discord.Client(intents=intents)

def load_planning():
    with open("./data/planning.json", "r") as f:
        return json.load(f)

def build_embed(sessions: list) -> discord.Embed:
    from datetime import date
    DAYS = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']

    embed = discord.Embed(color=0x5865F2)

    # Trier par date croissante
    sessions_sorted = sorted(sessions, key=lambda s: s['date'])

    for s in sessions_sorted:
        d = date.fromisoformat(s['date'])
        day_name = DAYS[d.weekday()]
        embed.add_field(
            name=f"{day_name} {d.strftime('%d/%m')}",
            value=f"{s['jeu']} à {s['heure']}",
            inline=False
        )

    return embed

@client.event
async def on_ready():
    print(f"✅ Bot connecté : {client.user}")

async def send_planning(sessions: list = None):
    data = load_planning()
    sessions = sessions or data["sessions"]
    if not sessions:
        return

    channel = client.get_channel(CHANNEL_ID)
    if channel:
        embed = build_embed(sessions)
        await channel.send(
            content="**🎮 PLANNING DE LA SEMAINE 🎮**",
            embed=embed
        )

def run():
    client.run(TOKEN)

if __name__ == "__main__":
    client.run(TOKEN)