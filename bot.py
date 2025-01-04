import discord
from discord.ext import commands
from Dado import Dado

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
bot = commands.Bot(command_prefix='!', intents=intents)(intents=intents)

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.command()
async def Dado(ctx):
    await ctx.send(Dado())
    
bot.run("MTMyNDU2NDYzMDY4ODg5NDk4Nw.GGrxMW.fVLoQVBFh0QpLQsjPTXVNyEYe_pP3D3I_kUYWo")

