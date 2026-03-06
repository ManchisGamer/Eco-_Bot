import discord
from discord.ext import commands

from configuration import TOKEN
from bot_logic import dar_tip, dar_reto, dar_dato
from quiz_logic import hacer_pregunta

intents = discord.Intents.default()

bot = commands.Bot(command_prefix="!", intents=intents)

puntos = {}

@bot.event
async def on_ready():
    print("EcoBot está conectado")

@bot.command()
async def tip(ctx):
    await ctx.send(dar_tip())

@bot.command()
async def reto(ctx):
    await ctx.send(dar_reto())

@bot.command()
async def dato(ctx):
    await ctx.send(dar_dato())

@bot.command()
async def quiz(ctx):

    pregunta, respuesta = hacer_pregunta()

    await ctx.send(pregunta)

    def check(m):
        return m.author == ctx.author

    msg = await bot.wait_for("message", check=check)

    if msg.content.lower() == respuesta:

        puntos[ctx.author.id] = puntos.get(ctx.author.id, 0) + 10

        await ctx.send("¡Correcto! +10 puntos 🌱")

    else:
        await ctx.send("Incorrecto. La respuesta era: " + respuesta)

@bot.command()
async def puntos_usuario(ctx):

    user_points = puntos.get(ctx.author.id, 0)

    await ctx.send("Tienes " + str(user_points) + " puntos")

bot.run(TOKEN)