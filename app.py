import discord
from mcstatus import MinecraftServer
import asyncio

# Configura los valores aquí
TOKEN_DISCORD = "TOKEN"
SERVER_IP = "Example.com"  # Ejemplo: "localhost" o "example.com"
PORT = 25565 # Puerto del servidor de Minecraft
CHANNEL_ID = ID  # ID del canal de Discord que quieres modificar

# Crear una instancia del cliente de Discord
intents = discord.Intents.default()
client = discord.Client(intents=intents)

# Función para obtener la cantidad de jugadores de Minecraft
def get_player_count():
    try:
        server = MinecraftServer(SERVER_IP, PORT)
        status = server.status()
        return status.players.online
    except Exception as e:
        print(f"Error al obtener el estado del servidor: {e}")
        return 0

# Evento cuando el bot se conecta correctamente
@client.event
async def on_ready():
    print(f"Conectado como {client.user}")
    
    # Mantener el bot actualizando el canal cada 5 minutos
    while True:
        try:
            player_count = get_player_count()
            channel = client.get_channel(CHANNEL_ID)
            if channel:
                new_name = f"Online Players: {player_count}"
                await channel.edit(name=new_name)
                print(f"Nombre del canal actualizado a: {new_name}")
            else:
                print("No se pudo encontrar el canal.")
        except Exception as e:
            print(f"Error al actualizar el nombre del canal: {e}")
        
        # Esperar 5 minutos antes de la próxima actualización
        await asyncio.sleep(300)

# Iniciar el bot
client.run(TOKEN_DISCORD)
