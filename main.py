import requests
import random
import asyncio
import aiohttp
import json
from discord import Game
from discord.ext.commands import Bot

BOT_PREFIX = ("?", "!")
TOKEN="NTM3MjQ0ODE1MjE4MzExMTY4.DyiuBg.5DCKL7rhdbX-FJrNHnXkNvC3FYI"  # Get at discordapp.com/developers/applications/me

client = Bot(command_prefix=BOT_PREFIX)

@client.command(name='8ball',
                description="Answers a yes/no question.",
                brief="Answers from the beyond.",
                aliases=['eight_ball', 'eightball', '8-ball'],
                pass_context=True)
async def eight_ball(context):
    possible_responses = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'Definitely',
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)

@client.command()
async def squared(number):
    squared_value = int(number) * int(number)
    await client.say(str(number) + " squared is " + str(squared_value))

  
@client.command(pass_context=True)
async def cumlig(context):
  sentence = "CUMLIG, "+context.message.author.mention+"!"
  await client.say(sentence) 

@client.command(name='play',pass_context=True)
async def sps(context,answer):
  if answer=='scissors':
    await client.say('stone')
    await client.say('You lost, '+context.message.author.mention)
  elif answer=='paper':
    await client.say('scissors')
    await client.say('You lost, '+context.message.author.mention)
  elif answer=='stone':
    await client.say('paper')
    await client.say('You lost, '+context.message.author.mention)
    
    
@client.command(pass_context=True)
async def cumleeg(context,answer):
  list_of_options=['scissors','paper','stone']
  bots_answer=random.choice(list_of_options)
  if answer=='scissors' and bots_answer=='paper':
    await client.say(bots_answer.upper())
    await client.say('ARGGHH YOU BEAT ME, '+context.message.author.mention)

  elif answer=='paper' and bots_answer=='stone':
    await client.say(bots_answer.upper())
    await client.say('ARGGHH YOU BEAT ME, '+context.message.author.mention)

  elif answer=='stone' and bots_answer=='scissors':
    await client.say(bots_answer.upper())
    await client.say('ARGGHH YOU BEAT ME, '+context.message.author.mention)

  elif answer==bots_answer:
   await client.say(bots_answer.upper())
   await client.say('ITS A TIE, '+context.message.author.mention)

  elif answer=='scissors' and bots_answer=='stone':
    await client.say(bots_answer.upper())
    await client.say('HAHAHAHA GARBAGE, '+context.message.author.mention)

  elif answer=='paper' and bots_answer=='scissors':
    await client.say(bots_answer.upper())
    await client.say('HAHAHAHA GARBAGE, '+context.message.author.mention)

  elif answer=='stone' and bots_answer=='paper':
    await client.say(bots_answer.upper())
    await client.say('HAHAHAHA GARBAGE, '+context.message.author.mention)
  
  else:
    await client.say("please input only scissors, paper or stone")





client.run("NTM3MjQ0ODE1MjE4MzExMTY4.DyiuBg.5DCKL7rhdbX-FJrNHnXkNvC3FYI")

