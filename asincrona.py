import asyncio #Importamis asyncio para hacer la programación asíncrona
import time

async def main(): #Subrutina
    print(f"Holiwis {time.strftime('%X')}")
    await asyncio.sleep(1)
    print(f"zorra {time.strftime('%X')}")

print(main) #Aquí lo toma como una función
