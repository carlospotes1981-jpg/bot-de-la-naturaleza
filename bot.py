import discord
from bot_login import gen_pass
from discord.ext import commands
import os
import random
from bot_login import get_duck_image_url
from bot_login import get_dog_image_url

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send("Hi!")

@bot.command()
async def bye(ctx):
    await ctx.send("😉")

@bot.command()
async def temas(ctx):
    
    await ctx.send(
            "¡Hola! Selecciona uno de estos tres temas:\n\n"
            "1. Reducir el consumo de energía\n"
            "2. Reciclar y reutilizar materiales\n"
            "3. Usar medios de transporte sostenibles\n\n"
            "Escribe 1, 2 o 3.")
    
    def verificar(mensaje):
        return mensaje.author == ctx.author and mensaje.channel == ctx.channel

    respuesta = await bot.wait_for("message", check=verificar)

    if respuesta.content == "1":
        await ctx.send(
            "🌎 REDUCIR EL CONSUMO DE ENERGÍA\n\n"
            "Puedes ayudar al planeta apagando las luces "
            "que no utilizas, desconectando cargadores "
            "y aprovechando la luz natural."
        )

    elif respuesta.content == "2":
        await ctx.send(
            "♻️ RECICLAR Y REUTILIZAR MATERIALES\n\n"
            "Separa los residuos, reutiliza envases "
            "y evita los plásticos de un solo uso."
        )

    elif respuesta.content == "3":
        await ctx.send(
            "🚲 TRANSPORTE SOSTENIBLE\n\n"
            "Camina, utiliza bicicleta o transporte público "
            "para reducir las emisiones contaminantes."
        )

    else:
        await ctx.send("Opción incorrecta. Escribe 1, 2 o 3.")
    
bot.run("")
