# ISIT 333 - Lab 9
# November 28, 2021
# Hoang Do

# import pandas
import pandas as pd

def display_menu():
    print()
    print("* * * * * * * COMMAND MENU * * * * * * *")
    print("1 - Print Name, Type, Generation")
    print("2 - Print Name, HP, Attack, Defense, Speed")
    print("3 - Print all of the GRASS type Pokemon")
    print("4 - Print all of the Pokemon in order of HP (highest to lowest)")
    print("5 - Print all of the Pokemon in order of NAME A-Z")
    print("6 - all the LEGENDARY Pokemon")
    print("7 - all the LEGENDARY Pokemon")

def display_name_type_and_generation(pokemon):
    print(pokemon[["Name", "Type 1", "Type 2", "Generation"]])

def display_name_hp_attack_defense_speed(pokemon):
    print(pokemon[["Name", "HP", "Attack", "Defense", "Speed"]])

def display_dataframe_grass_type_pokemon(pokemon):
    grass_type_pokemon = pokemon[(pokemon["Type 1"] == "Grass")|(pokemon["Type 2"] == "Grass")]
    frame_grass_type_pokemon = pd.DataFrame(grass_type_pokemon)
    print(frame_grass_type_pokemon[["Name", "Type 1", "Type 2"]])

def display_dataframe_pokemon_hp_highest_to_lowest(pokemon):
    pokemon_hp_highest_to_lowest = pokemon.sort_values("HP", ascending=False)
    frame_pokemon_hp_highest_to_lowest = pd.DataFrame(pokemon_hp_highest_to_lowest)
    print(frame_pokemon_hp_highest_to_lowest[["Name", "HP"]])

def display_dataframe_pokemon_name_in_ascending_order(pokemon):
    pokemon_name_in_ascending_order = pokemon.sort_values("Name")
    frame_pokemon_name_in_ascending_order = pd.DataFrame(pokemon_name_in_ascending_order)
    print(frame_pokemon_name_in_ascending_order["Name"])

def display_dataframe_legendary_pokemon(pokemon):
    legendary_pokemon = pokemon[pokemon["Legendary"] == True]
    frame_legendary_pokemon = pd.DataFrame(legendary_pokemon)
    print(frame_legendary_pokemon[["Name", "Legendary"]])

def main():
    # print("Welcome to MCU Superheroes Database")
    # save data to a variable "pokemon"
    pokemon = pd.read_csv("pokemon.csv")

    while True:
        display_menu()
        print()
        command = input("Command: ")
        print()
        if command == "1":
            display_name_type_and_generation(pokemon)
        elif command == "2":
            display_name_hp_attack_defense_speed(pokemon)
        elif command == "3":
            display_dataframe_grass_type_pokemon(pokemon)
        elif command == "4":
            display_dataframe_pokemon_hp_highest_to_lowest(pokemon)
        elif command == "5":
            display_dataframe_pokemon_name_in_ascending_order(pokemon)
        # elif command == "6":
        #     break
        else:
            print("Unknown command. Please try again.")

    # farewell message
    print("Thank you for using MCU superhero database. See you later for more interesting about Marvel Cinematic Universe!")

if __name__ == "__main__":
    main()