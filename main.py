# Dependencies

# python3 -m pip install -U git+https://github.com/Rapptz/discord.py

# tutorial buena pinta completo: https://www.youtube.com/playlist?list=PLYeOw6sTSy6ZGyygcbta7GcpI8a5-Cooc

# DATABASE:
# Example: https://youtu.be/4EIy0bw7s-s


# IMPORTS

import os 
import re

import discord
from discord import app_commands
from discord.ui import Button, View

# Keep the bot alive
from keep_alive import keep_alive



# VARIABLES

#id servers
onevone= 321359579571027968
myServerID = 491976410563608586

# inic dc
intents = discord.Intents.all()
serverId = myServerID


# connection with Dicord

class aclient(discord.Client):
    # discord bot intents and constructor
    def __init__(self):
        super().__init__(intents=intents)
        self.synced = False

    # at the beginning
    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync(guild=discord.Object(id=serverId))
            self.synced = True
        print(f'We have logged in as {self.user}.')


client = aclient()
tree = app_commands.CommandTree(client)



# FUNCS

def run():
  # start the server to keep alive the bot
  keep_alive()
  # start the bot with the token
  client.run(os.environ['TOKEN'])


  
# CLASSES https://www.youtube.com/watch?v=kNUuYEWGOxA&t=63s&ab_channel=CodeWithSwastik

# elementos
# fire > grass > water > fire
# order: fire, water, grass

class Resistencia:

  def __init__(self, res_fire, res_water, res_grass):
    self.res_fire = res_fire
    self.res_water = res_water
    self.res_grass = res_grass
    
# Entities (Enemy, Boss, Character)
class Entity:
  def __init__(self, name, hp=100, ap=10, dp=10, res = Resistencia(10,10,10), elem ='fuego',
               img_path="img/img.png", filename= "img.png"):
    self.name = name
    self.hp = hp
    self.ap = ap
    self.dp = dp
    self.res = res
    self.elem = elem
    self.img_path = img_path
    self.filename = filename


class Enemy(Entity):
  def __init__(self, name, hp, ap, dp, res, elem, img_path, filename, new):
    super().__init__(self, name, hp, ap, dp, res, elem, img_path, filename)
    self.new = new

class Boss(Entity):
  def __init__(self, name, hp, ap, dp, res, elem, img_path, filename, new):
    super().__init__(self, name, hp, ap, dp, res, elem, img_path, filename)
    self.new = new

class Character(Entity):
  def __init__(self, name, hp, ap, dp, res, elem, img_path, filename, weapon_left,
               weapon_right, armor_head, armor_chest,  armor_gloves, armor_shoes):
    super().__init__(self, name, hp, ap, dp, res, elem, img_path, filename)
    self.weapon_left = weapon_left
    self.weapon_right = weapon_right
    self.armor_head = armor_head
    self.armor_chest = armor_chest
    self.armor_gloves = armor_gloves
    self.armor_shoes = armor_shoes
    

# Items (Weapon, Armor) (Passive)
class Item():
  def __init__(self, name, elem):
    self.name = name
    self.elem = elem

class Weapon(Item):
  def __init__(self, name, elem, ap, dp):
    super().__init__(name, elem)
    self.ap = ap
    self.dp = dp

class Armor(Item):
  def __init__(self, name, elem, ap, dp, res):
    super().__init__(name, elem)
    self.ap = ap
    self.dp = dp
    self.res = res


# lo de passivas no se como implementarlo (preguntar a ñef)
# post que hablan de esto:
# https://www.reddit.com/r/gamedev/comments/676i72/best_way_to_implement_unique_passive_abilities_on/
# https://forum.unity.com/threads/how-to-implement-a-active-passive-skill-system-in-a-2d-sprite-game.234963/
# multiplicadores, o habilidades unicas (checar ejemplos de pasivas en otros juegos) (ejemplo: cada vez que recibes daño devuelves un x%)
class Passive():
  def __init__(self, name, desc, ap, dp):
    self.name = name
    self.desc = desc
    self.ap = ap
    self.dp = dp

    
# crear clase user para guardar el dinero y cosas ascii
# se podria hacer una tienda rollo para comprar cosas
# clase ataques (daño base, elem)

# inherit from discord.ui.View to manage button interactions
class MyView(View):

  # attack interaction
  @discord.ui.button(emoji="⚔️")
  async def atk_callback(self, interaction, button):
    await interaction.response.send_message("Has atacado.")
    #print("ataque")

  # defense interaction
  @discord.ui.button(emoji="🛡️")
  async def def_callbackk(self, interaction, button):
    await interaction.response.send_message("Te has defendido.")
    #print("defensa")



# hay que mirar como manejar diferentes personas usandolo en paralelo
# mirar el dueño y en que canal lo esta haciendo o algo asi
# https://stackoverflow.com/questions/63705538/how-to-handle-multiple-users-using-same-command-discord-py

#Owner class to know who has the bot in each time
class Owner:

    user = None

    def __init__(self):
        pass

      
# MAIN 

def main():

  # test command to see if the buttons r working
  @tree.command(name="boton",
                description="boton",
                guild=discord.Object(id=serverId))
  async def boton(interaction: discord.Integration):

    # create a myView to manage button interactions
    view = MyView()

    # create the embed where the image and the info of the monster will go
    em = discord.Embed(title="titulo", description='descripcion', color=0xAE0808)
    # add footer (text or imgs)
    em.set_footer(text=f'footer')
    # convert the img to a discord file
    f = discord.File("img/img.png", filename="img.png") 
    # attach the img
    em.set_image(url="attachment://img.png")

    await interaction.response.send_message(view=view, file=f, embed=em)

    
  # create a character for a user (TODO save in a db)
  @tree.command(name="create_character",
                description="Crear el personaje del jugador",
                guild=discord.Object(id=serverId))
  async def create_character(interaction: discord.Integration, name: str):

    # create a new character
    #character = Character(name = name, )
    print('a')

  
  run()


if __name__ == "__main__":
    main()
