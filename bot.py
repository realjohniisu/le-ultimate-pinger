import discord
from discord import app_commands

class MyClient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()

client = MyClient()

@client.tree.command(name="jadenping", description="ping le big J")
async def jadenping(interaction: discord.Interaction):
    await interaction.response.send_message("Starting...", ephemeral=True)

    for _ in range(15):
        msg = await interaction.channel.send("<@1489822967222243339>")
        await msg.delete()

import os

client.run(os.environ["DISCORD_TOKEN"])