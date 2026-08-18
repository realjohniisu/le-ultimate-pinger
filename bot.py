import discord
from discord import app_commands
import os

class MyClient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()

client = MyClient()


@client.tree.command(name="axleping", description="ping Axle")
async def axleping(interaction: discord.Interaction):
    await interaction.response.send_message("Pinging Axle...", ephemeral=True)

    for _ in range(15):
        msg = await interaction.channel.send("<@1307916015589392455>")
        await msg.delete()


@client.tree.command(name="elginping", description="ping Elgin")
async def elginping(interaction: discord.Interaction):
    await interaction.response.send_message("Pinging Elgin...", ephemeral=True)

    for _ in range(15):
        msg = await interaction.channel.send("<@1536205184223416431>")
        await msg.delete()


@client.tree.command(name="jadenping", description="ping le big J")
async def jadenping(interaction: discord.Interaction):
    await interaction.response.send_message("Pinging Jaden...", ephemeral=True)

    for _ in range(15):
        msg = await interaction.channel.send("<@1489822967222243339>")
        await msg.delete()


@client.tree.command(name="noahping", description="ping Noah")
async def noahping(interaction: discord.Interaction):
    await interaction.response.send_message("Pinging Noah...", ephemeral=True)

    for _ in range(15):
        msg = await interaction.channel.send("<@974872649400463442>")
        await msg.delete()


@client.tree.command(name="robertping", description="ping Robert")
async def robertping(interaction: discord.Interaction):
    await interaction.response.send_message("Pinging Robert...", ephemeral=True)

    for _ in range(15):
        msg = await interaction.channel.send("<@1538994823371952238>")
        await msg.delete()


client.run(os.environ["DISCORD_TOKEN"])