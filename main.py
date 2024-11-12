import discord
from discord.ext import commands
from openpyxl import Workbook
from datetime import datetime, timedelta
import pytz

TOKEN = 'Token do seu bot'
canal_presenca = 'ID do canal de presença'
limite_tempo = 'Tempo limite para marcar presença em minutos'

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)
wb = Workbook()
ws = wb.active
ws.append(['Nome', 'Data', 'Hora'])

@bot.event
async def on_ready():
    print('Bot online')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.channel.id == canal_presenca:
        horario = pytz.timezone('America/Sao_Paulo').localize(datetime.now())
        horario_limite = message.created_at + timedelta(minutes=limite_tempo)

        if horario <= horario_limite:
            ws.append([message.author.display_name, horario.strftime('%d/%m/%Y'), horario.strftime('%H:%M:%S')])
            wb.save('Presenca.xlsx')
            await message.channel.send(f'{message.author.mention}, presença registrada com sucesso!')
        else:
            await message.channel.send(f'{message.author.mention}, você ultrapassou o limite de tempo para marcar presença!')

bot.run(TOKEN)