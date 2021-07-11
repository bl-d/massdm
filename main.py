import discord
import os
import colorama
from colorama import init, Fore, Back, Style

client = discord.Client()

print(f"\n {Fore.RED}╦╔═╦═╗╔═╗═╗ ╦  ╔╦╗╔═╗╔═╗╔═╗╔╦╗╔╦╗ \n ╠╩╗╠╦╝╔═╝╔╩╦╝ {Fore.RESET} ║║║╠═╣╚═╗╚═╗ ║║║║║ \n ╩ ╩╩╚═╚═╝╩ ╚═  ╩ ╩╩ ╩╚═╝╚═╝═╩╝╩ ╩")

token = input('Enter your token:\n')
message = input('Message to send:\n')
krzx = input("Press enter to start mass dming . . .")

os.system(f'title [Massdm]- {client.user}')

@client.event
async def on_connect():
    for user in client.user.friends:
        if user.id != 818623172412178473:#replace user id with an id u dont wanna dm.
          try:
              await user.send(f"{user.mention} {message}")
              print(Style.BRIGHT + Fore.GREEN + f"Sent dm to {user.name} | Message - {message}")
              os.system(f'title [Massdm] - Sent dm to {user.name}')
          except:
              print(Style.BRIGHT + Fore.RED + f"Failed to dm {user.name}")
              os.system(f"title [Massdm] - Failed to dm {user.name}")


client.run(token, bot=False)
