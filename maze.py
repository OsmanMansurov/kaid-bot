import discord
import random
from discord.ext import commands
from read import dictionary

client = commands.Bot(command_prefix = '!')


@client.event
async def on_ready():
    print("Bot is ready.")

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command(aliases=["8ball"])
async def _8ball(ctx, *, question):
    choices = ["It is Certain.", "It is decidedly so.", "Without a doubt.",
              "Yes definitely.", "You may rely on it.", "As I see it, yes.",
              "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.",
              "Reply hazy, try again.", "Ask again later.", "Better not tell you now.",
              "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.",
              "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful"]
    await ctx.send(f"Question: {question}\nAnswer: {random.choice(choices)}")

@client.command()
async def stats(ctx, pokemon):
    stats = dictionary[pokemon]
    await ctx.send(f"HP: {stats[0]}\nAttack: {stats[1]}\nDefense: {stats[2]}\nSp. Attack: {stats[3]}\nSp. Defense: {stats[4]}\nSpeed: {stats[5]}\nStat Total: {sum(stats)}")

client.run('ODc1NzU1MDY1NzYyMjc1MzI4.YRaIdg.ocIabDpeCikJh9soUOwTedjEdxI')
