import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!',intents=discord.Intents.all())

historias = {
'A': """
Aterrizar en el Planeta:\n
Aterrizas en el planeta y descubres una antigua civilización alienígena.\n
¿Decides establecer contacto pacífico o investigar más agresivamente?\n
Escribe `!decision A1` para establecer contacto pacífico \n
`!decision A2` para investigar agresivamente.
""",

'A1': """
Establecer Contacto Pacífico:\n
La civilización alienígena acepta tu presencia y te comparte conocimientos avanzados, ofreciéndote ayuda para regresar a casa.\n
Final A - Coexistencia Próspera:\n
Establecer contacto pacífico con la civilización alienígena lleva a una alianza fructífera que beneficia a ambos lados.
""",

'A2': """
Investigar Agresivamente:\n 
La civilización alienígena se siente amenazada y contraataca. Tu nave sufre daños, pero logras escapar, perdiendo la oportunidad de aprender más.\n
Final B - Escape Heroico:\n
Al investigar agresivamente, tu escape exitoso después del contraataque alienígena se convierte en una historia de valentía.
    """ 
}

@bot.event
async def on_ready():
    print(f'I am ready! Logged in as {bot.user}')

@bot.event
async def on_member_join(member):
    canal_bienvenida = member.guild.system_channel  # Obtener el canal de bienvenida del servidor
    if canal_bienvenida:
        bienvenida_mensaje = (
            f"Bienvenido {member.mention} al juego interactivo de Discord!\n"
            "Te encuentras a bordo de la nave 'Galáctica', listo para embarcarte en una emocionante aventura espacial.\n"
            "Escribe `!comenzar` para comenzar tu viaje."
        )
        await canal_bienvenida.send(bienvenida_mensaje)


@bot.command(name='comenzar')
async def comenzar_juego(ctx):
    message = """
Aventura Espacial: "La Odisea Estelar"\n
Eres el capitán de la nave "Galáctica", encargado de explorar la misteriosa nebulosa de Cygnus. 
Mientras te acercas, una distorsión temporal sacude tu nave, 
y te encuentras en un sistema solar desconocido y aparentemente abandonado.\n
Detectas un rastro de energía proveniente de un planeta cercano.\n
¿Decides aterrizar para investigar o seguir explorando el sistema solar?\n
Escribe `!decision A` para aterrizar en el planeta \n
`!decision B` para seguir explorando el sistema solar.\n
"""
    await ctx.send(f"{message}")
    

@bot.command(name='decision')
async def historia(ctx, *args):
    if len(args) == 0:
        await ctx.send('--Debes ingresar una letra--')
    else:
        letra = args[0].upper()
        await ctx.send(historias[letra])


@bot.command(name='clear')
async def borrar_chat(ctx, cantidad: int):
    await ctx.channel.purge(limit=cantidad + 1)  # El +1 es para incluir el comando en el conteo
    await ctx.send(f"Se han borrado {cantidad} mensajes.")


token = 'aqui va el token'
bot.run(token)
