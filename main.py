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

# Mantener vivo el bot
from keep_alive import keep_alive



# VARIABLES

#id servers
onevone= 321359579571027968
myServerID = 491976410563608586

# inic dc
intents = discord.Intents.all()
serverId = myServerID


# connection with dicord

class aclient(discord.Client):
    # poner los intents y constructor
    def __init__(self):
        super().__init__(intents=intents)
        self.synced = False

    # al iniciar
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
  # iniciar el servidor para mantenerlo vivo
  keep_alive()
  # iniciar el bot con el TOKEN
  client.run(os.environ['TOKEN'])


  
# CLASSES https://www.youtube.com/watch?v=kNUuYEWGOxA&t=63s&ab_channel=CodeWithSwastik

# elementos
# fuego > planta > agua > fuego
# order: fuego, agua, planta

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

class MyView(View):

  @discord.ui.button(emoji="⚔️")
  async def atk_callback(self, interaction, button):
    await interaction.response.send_message("Has atacado.")
    #print("ataque")
  
  @discord.ui.button(emoji="🛡️")
  async def def_callbackk(self, interaction, button):
    await interaction.response.send_message("Te has defendido.")
    #print("defensa")



# hay que mirar como manejar diferentes personas usandolo en paralelo
# mirar el dueño y en que canal lo esta haciendo o algo asi
# https://stackoverflow.com/questions/63705538/how-to-handle-multiple-users-using-same-command-discord-py

#clase dueño para saber quien tiene el bot
class Duenio:

    user = None

    def __init__(self):
        pass
    
# MAIN 

def main():

  # Mirar lo de meter un field dentro del embed
  # Crear clases myBtn por ejemplo MyButtonAtk y meter dentro las callback
  # O Hacerlo por view y meterle dentro los MyButton

  @tree.command(name="boton",
                description="boton",
                guild=discord.Object(id=serverId))
  async def boton(interaction: discord.Integration):

    # crea una view para enviarla en el mensaje
    view = MyView()

    # crea el embed donde pondra la imagen
    em = discord.Embed(title="titulo", description='descripcion', color=0xAE0808)
    # añadir footer (puedes poner texto e img)
    em.set_footer(text=f'footer')
    # convierte en un archivo para dc
    f = discord.File("img/img.png", filename="img.png") 
    # pega la img
    em.set_image(url="attachment://img.png")

    await interaction.response.send_message(view=view, file=f, embed=em)

  
  @tree.command(name="create_character",
                description="Crear el personaje del jugador",
                guild=discord.Object(id=serverId))
  async def create_character(interaction: discord.Integration, name: str):

    # create a new character
    character = Character(name = name, )


  run()


if __name__ == "__main__":
    main()
