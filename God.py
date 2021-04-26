# bot.py
import os # for importing env vars for the bot to use
from twitchio.ext import commands
import random
import Classes.User

bot = commands.Bot(
    # set up the bot
    irc_token=os.environ['TMI_TOKEN'],
    client_id=os.environ['CLIENT_ID'],
    nick=os.environ['BOT_NICK'],
    prefix=os.environ['BOT_PREFIX'],
    initial_channels=[os.environ['CHANNEL']]
)

@bot.event
async def event_ready():
    'Called once when the bot goes online.'
    print("God has cumed!")
    ws = bot._ws  # this is only needed to send messages within event_ready
    await ws.send_privmsg(os.environ['CHANNEL'], f"God has landed!")


@bot.event
async def event_message(ctx):
    'Runs every time a message is sent in chat.'

    # make sure the bot ignores itself and the streamer
    if ctx.author.name.lower() != os.environ['BOT_NICK'].lower():
        await bot.handle_commands(ctx)

    if 'hello' in ctx.content.lower():
        await ctx.channel.send(f"Hi, @{ctx.author.name}!")

    if 'good bot' in ctx.content.lower():
    	await ctx.channel.send(f"Thank you @{ctx.author.name}!")


@bot.command(name='yesno')
async def yesno(ctx):
	print(ctx.author.id)
	await ctx.send(random.choice(["Yes","No"]))

@bot.command(name='play')
async def yesno(ctx):
	print(ctx.author.id)
	User(ctx.author.id,ctx.author.name)
	await ctx.send("Registered")

if __name__ == "__main__":
    bot.run()