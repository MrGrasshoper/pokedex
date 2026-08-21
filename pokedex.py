
import requests

def get_pokemon_data(pokemon_name):
    """Fetches Pokémon data from the PokeAPI."""
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        pokemon_id = data["id"]
        name = data["name"].capitalize()
        types = [t["type"]["name"].capitalize() for t in data["types"]]
        abilities = [a["ability"]["name"].capitalize() for a in data["abilities"]]
        return {"id": pokemon_id, "name": name, "types": types, "abilities": abilities}
    else:
        return None

def display_pokemon_data(data):
    """Displays formatted Pokémon data."""
    if data:
        print(f"\n--- {data['name']} ---")
        print(f"ID: {data['id']}")
        print(f"Types: {", ".join(data['types'])}")
        print(f"Abilities: {", ".join(data['abilities'])}")
    else:
        print("Pokémon not found.")

def main():
    """Main function to run the Pokedex."""
    print("Welcome to the Pokedex!")
    test_pokemon = ["Pikachu", "Charmander", "Mewtwo", "InvalidPokemon"]
    for pokemon_name in test_pokemon:
        print(f"\n--- Searching for {pokemon_name} ---")

        pokemon_data = get_pokemon_data(pokemon_name)
        display_pokemon_data(pokemon_data)

    print("Goodbye!")

if __name__ == "__main__":
    main()
