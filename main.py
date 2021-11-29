# ISIT 333 - Lab 9
# November 28, 2021
# Hoang Do

# import pandas
import pandas as pd

def display_menu():
    print()
    print("* * * * * * * COMMAND MENU * * * * * * *")
    print("1 - Display all of the Pokemon by Name, Type, Generation")
    print("2 - Display all of the Pokemon by Name, HP, Attack, Defense, Speed")
    print("3 - Display only the GRASS type Pokemon")
    print("4 - Display all of the Pokemon in order of HP (highest to lowest)")
    print("5 - Display all of the Pokemon in order of NAME A-Z")
    print("6 - Display only the LEGENDARY Pokemon")
    print("7 - Search the Pokemon by Name and Display the Associated Data")
    print("8 - Exit the Program")

def display_by_name_type_and_generation(pokemon):
    print(pokemon[["Name", "Type 1", "Type 2", "Generation"]])

def display_by_name_hp_attack_defense_and_speed(pokemon):
    print(pokemon[["Name", "HP", "Attack", "Defense", "Speed"]])

def display_dataframe_of_only_grass_type(pokemon):
    # this function displays only GRASS type, no matter Type 1 GRASS or Type 2 GRASS
    grass_type_pokemon = pokemon[(pokemon["Type 1"] == "Grass")|(pokemon["Type 2"] == "Grass")]
    frame_grass_type_pokemon = pd.DataFrame(grass_type_pokemon)
    print(frame_grass_type_pokemon[["Name", "Type 1", "Type 2"]])

def display_dataframe_of_highest_to_lowest_hp(pokemon):
    pokemon_hp_highest_to_lowest = pokemon.sort_values("HP", ascending=False)
    frame_pokemon_hp_highest_to_lowest = pd.DataFrame(pokemon_hp_highest_to_lowest)
    print(frame_pokemon_hp_highest_to_lowest[["Name", "HP"]])

def display_dataframe_of_name_in_ascending_order(pokemon):
    pokemon_name_in_ascending_order = pokemon.sort_values("Name")
    frame_pokemon_name_in_ascending_order = pd.DataFrame(pokemon_name_in_ascending_order)
    print(frame_pokemon_name_in_ascending_order)

def display_dataframe_of_only_legendary(pokemon):
    legendary_pokemon = pokemon[pokemon["Legendary"] == True]
    frame_legendary_pokemon = pd.DataFrame(legendary_pokemon)
    print(frame_legendary_pokemon[["Name", "Legendary"]])

def search_by_name_and_display(pokemon):
    try:
        search_value = input("Input a name of a Pokemon: ")
        associated_data = pokemon[pokemon["Name"] == search_value]
        frame_associated_data = pd.DataFrame(associated_data)
        print(frame_associated_data)
    except:
        print("Something went wrong. Please try again!")
        search_value = input("Input a name of a Pokemon: ")
# Name,Type 1,Type 2,Total,HP,Attack,Defense,Sp. Atk,Sp. Def,Speed,Generation,Legendary
def main():
    print("Welcome to the Incredible Pokemon Data")
    # save data to a variable "pokemon"
    pokemon = pd.read_csv("pokemon.csv")

    while True:
        display_menu()
        print()
        command = input("Command: ")
        print()
        if command == "1":
            display_by_name_type_and_generation(pokemon)
        elif command == "2":
            display_by_name_hp_attack_defense_and_speed(pokemon)
        elif command == "3":
            # display only GRASS type, no matter Type 1 GRASS or Type 2 GRASS
            display_dataframe_of_only_grass_type(pokemon)
        elif command == "4":
            display_dataframe_of_highest_to_lowest_hp(pokemon)
        elif command == "5":
            display_dataframe_of_name_in_ascending_order(pokemon)
        elif command == "6":
            display_dataframe_of_only_legendary(pokemon)
        elif command == "7":
            search_by_name_and_display(pokemon)
        elif command == "8":
            break
        else:
            print("Unknown command. Please try again.")

    # farewell message
    print("Thank you for using the Incredible Pokemon Data. See you later for more interesting about the Pokemon!")

if __name__ == "__main__":
    main()