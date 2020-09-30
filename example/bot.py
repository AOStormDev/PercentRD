from PercentRD.Percent import Random as RD
import discord

client = discord.Client()

@client.event
async def on_message(message):
    if message.content.startswith("!도박"):
        if str(RD(34)) == "a":
            await message.channel.send("도박에 당첨되셨습니다!")
        else:
            await message.channel.send("도박에 떨어지셨습니다..")

@client.run("Your Token")