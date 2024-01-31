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
    """,

'B': """
Seguir Explorando:\n
Optas por seguir explorando el sistema solar en busca de otras señales de vida o recursos.\n
Encuentras una luna con un extraño monolito. ¿Decides investigar o ignorar el monolito?\n
Escribe `!decision B1` para investigar \n
`!decision B2` para ingnorar.
""",

'B1': """
Investigar el Monolito:\n
Al tocar el monolito, experimentas una visión del futuro que te guía hacia una ruta segura para regresar a casa.\n
Final C - De vuelta a casa:\n
Al elegir investigar el monolito logras regresar a casa , te das cuenta que han pasado siglos desde que te fuiste.\n
""",

'B2': """
Ignorar el Monolito:\n
Decides no investigar el monolito y continúas explorando, sin obtener información adicional.\n
final D - Viaje infinito:\n
vagas por la inmensidad tratando de regresar a casa fallidamente durante decadas, buscas de nuevo el monolito pero no lo vuelves a encontrar por lo que jamas vuelves a casa.\n
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

@bot.command(name='hola')
async def saludo(ctx):
    message = """
Hola aventurer@ :D bienvenido al juego interactivo espacial \n
cuando estes list@ para tu aventura hazmelo saber mediante el comando '!comenzar' para iniciar tu aventura\n
que te diviertas :D"""
    await ctx.send(f"{message}")

@bot.command(name='decision')
async def historia(ctx, *args):
    if len(args) == 0:
        await ctx.send('--Debes ingresar una de las opciones por favor UnU--')
    else:
        letra = args[0].upper()
        await ctx.send(historias[letra])


@bot.command(name='clear')
async def borrar_chat(ctx, cantidad: int):
    await ctx.channel.purge(limit=cantidad + 1)  # El +1 es para incluir el comando en el conteo
    await ctx.send(f"Se han borrado {cantidad} mensajes.")


token = 'MTIwMTkzMDg4OTY3Njk4NDQwMA.GOLVKn.Fe2Bh2ClDAUOyb4X4Ywcpp_I0DNCQIlRO0ND2o'
bot.run(token)
