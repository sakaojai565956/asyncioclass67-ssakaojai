from flask import Flask, render_template
import asyncio
import httpx
import time
import random
from pypokemon.pokemon import Pokemon


app = Flask(__name__)

async def get_pokemon(client, url):
    print(f"{time.ctime()} - get {url}")
    resp = await client.get(url)
    pokemon = resp.json()
    
    return pokemon

async def get_pokemons():
    async with httpx.AsyncClient() as client:
        tasks = []
        rand_list=[]
        for i in range(5):
            rand_list.append(random.randint(1,151))
            
        for number in rand_list:                                  
            url = f'https://pokeapi.co/api/v2/pokemon/{number}'
            tasks.append(asyncio.create_task(get_pokemon(client, url)))
        
        pokemon_tasks = await asyncio.gather(*tasks)
                
        pokemon_data = []
        for pokemon_object in pokemon_tasks:
            pokemon_data.append(Pokemon(pokemon_object))

        
    return pokemon_data
        

@app.route('/')
async def index():
    start_time = time.perf_counter()
    pokemons = await get_pokemons()
    end_time = time.perf_counter()
    print(f"{time.ctime()} - Get {len(pokemons)} pokemons. Time taken: {end_time - start_time} seconds")
    return render_template('index.html', pokemons=pokemons, end_time=end_time, start_time=start_time)
if __name__ == '__main__':
    app.run(debug=True, port=50001)