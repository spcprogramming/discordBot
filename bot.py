import discord
import asyncio
import json

import bot_token
import reminder

def pred(msg):
    return msg.author == msg.author and msg.channel == msg.channel

client = discord.Client()

@client.event
async def on_ready():
    print("Now active")
    await client.change_presence(activity=discord.Game(name="here"))

@client.event
async def on_message(message):

    # ignore bot
    if message.author == client.user:
        return

    # reminder functions
    if "!reminderadd" in message.content:
        if message.content == "!reminderadd":
            new_reminder = reminder.Reminder()

            # get reminder title
            await message.channel.send("What is the title of the reminder?")
            try:
                msg = await client.wait_for('message', author=messsage.author, timeout=60.0)
            except asyncio.TimeoutError:
                await message.channel.send("You took too long to give a title...")
            else:
                new_reminder.title = msg.content

            # get date
            await message.channel.send("What is the date that " + new_reminder.title + " will take place? MM/DD/YY format.")
            try:
                msg = await client.wait_for('message', check=(msg.author==message.author), timeout = 60.0)
            except asyncio.TimeoutError:
                await message.channel.send("You took too long to give a date...")
            else:
                new_reminder.date = msg.content

            # get time
            await message.channel.send("When will " + new_reminder.title + " take place on " + new_reminder.date + "? 24 hour format (HH:MM)")
            try:
                msg = await client.wait_for('message', check=(msg.author==message.author), timeout = 60.0)
            except asyncio.TimeoutError:
                await message.channel.send("You took too long to give a time...")
            else:
                new_reminder.time = msg.content

            # get description
            await message.channel.send("Can you give a brief description of the event?")
            try:
                msg = await client.wait_for('message', check=(msg.author==message.author), timeout = 60.0)
            except asyncio.TimeoutError:
                await message.channel.send("You took too long to give a description...")
            else:
                new_reminder.description = msg.content

            # converting object to json for saving
            print(reminder.convert(new_reminder))
            reminder.save(reminder.convert(new_reminder))

            await message.channel.send("Reminder saved!\n> Title: " + new_reminder.title + "\n> Date: " + new_reminder.date + "\n> Time: " + new_reminder.time + "\n> Description: " + new_reminder.description)

client.run(bot_token.read())
