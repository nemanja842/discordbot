import discord
from benckalkulator import kalkulator
from giphy import get_gif

class DiscordBot:
    def __init__(self, token):
        self.token = token

        intents = discord.Intents.default()
        intents.message_content = True

        self.client = discord.Client(intents=intents)

        
        @self.client.event
        async def on_ready():
            print(f"Logged in as {self.client.user}")

        @self.client.event
        async def on_message(message):
            if message.author == self.client.user:
                return  

            if message.content.startswith("!bench"):
                gif_url = get_gif("bench press")  

                if gif_url:
                    await message.channel.send(gif_url)
                else:
                    await message.channel.send("Nema dostupnih GIF-ova.")

            if message.content.startswith("!pomagaj"):
                await message.channel.send("Ovaj bot je iskljucivo namenjen za bench press, i smeju da ga koriste ljudi koji bencuju vise od 100 kila--------------KOMANDE : !bench   !pomagaj  !1rpm")
            if message.content.startswith(f"!1rpm"): 
                
                parts = message.content.split()
                
                if len(parts) != 3:
                    await message.channel.send("!1rpm komanda se koristi u formatu "
                    " !1rpm (reps) (tezina)---- "
                    "primer:  !rpm 4 90 " )
                    return
                
                try:
                    
                    reps = int(parts[1])
                    weight = float(parts[2])
                    
                    kalkulatorovde = kalkulator(reps, weight)


                    one_rpm = kalkulatorovde.calculate_1rpm()
                    
                    one_rpm = int(one_rpm)
                    one_rpm = round(one_rpm, 2)
                    await message.channel.send(f"Procena tvog 1RM-a je {one_rpm} kg")
                except:
                    await message.channel.send("Molim te unesi validne brojeve za težinu i ponavljanja.")
    def run(self):
        self.client.run(self.token)  

