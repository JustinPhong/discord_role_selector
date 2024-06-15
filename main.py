import discord
import os

# Constants
MESSAGE_ID = 1148650450514608139
ROLES = {
    'dota2': 'dota2',
    'csgo': 'csgo2',
    'twitch': 'nia',
    'palworld': 'Palworld'
}

intents = discord.Intents.all()
intents.message_content = True
my_secret = os.environ.get('TOKEN')
client = discord.Client(intents=intents)


def get_role_by_emoji(guild, emoji_name):
    return discord.utils.get(guild.roles, name=ROLES.get(emoji_name))


@client.event
async def on_raw_reaction_add(payload):
    if payload.message_id == MESSAGE_ID:
        guild = client.get_guild(payload.guild_id)
        member = guild.get_member(payload.user_id)
        role = get_role_by_emoji(guild, payload.emoji.name)

        if role and member:
            await member.add_roles(role)


@client.event
async def on_raw_reaction_remove(payload):
    if payload.message_id == MESSAGE_ID:
        guild = client.get_guild(payload.guild_id)
        member = guild.get_member(payload.user_id)
        role = get_role_by_emoji(guild, payload.emoji.name)

        if role and member:
            await member.remove_roles(role)

client.run(my_secret)
