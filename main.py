# ISIT 333 - Lab 9
# November 28, 2021
# Hoang Do

# import pandas
import pandas as pd

def display_menu():
    print()
    print("* * * * * * * MAIN MENU * * * * * * *")
    print("1 - Display all of the Pokemon by Name, Type, Generation")
    print("2 - Display all of the Pokemon by Name, HP, Attack, Defense, Speed")
    print("3 - Display all of the GRASS type Pokemon")
    print("4 - Display all of the Pokemon in order of HP (highest to lowest)")
    print("5 - Display all of the Pokemon in order of NAME A-Z")
    print("6 - Display all of the LEGENDARY Pokemon")
    print("7 - Search the Pokemon by Name")
    print("8 - Exit the program")

def display_by_name_type_and_generation(pokemon):
    print(pokemon[["Name", "Type 1", "Type 2", "Generation"]])

def display_by_name_hp_attack_defense_and_speed(pokemon):
    print(pokemon[["Name", "HP", "Attack", "Defense", "Speed"]])

def display_dataframe_of_grass_type(pokemon):
    # this function displays all GRASS type Pokemon, could be Type 1 GRASS or Type 2 GRASS
    grass_type_pokemon = pokemon[(pokemon["Type 1"] == "Grass")|(pokemon["Type 2"] == "Grass")]
    frame_grass_type_pokemon = pd.DataFrame(grass_type_pokemon)
    print(frame_grass_type_pokemon[["Name", "Type 1", "Type 2", "HP", "Attack", "Defense", "Speed", "Legendary"]])

def display_dataframe_of_hp_highest_to_lowest_order(pokemon):
    hp_highest_to_lowest_order_pokemon = pokemon.sort_values("HP", ascending=False)
    frame_hp_highest_to_lowest_order_pokemon = pd.DataFrame(hp_highest_to_lowest_order_pokemon)
    print(frame_hp_highest_to_lowest_order_pokemon[["Name", "HP", "Type 1", "Type 2", "Total", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed", "Generation", "Legendary"]])

def display_dataframe_of_name_in_a_to_z_order(pokemon):
    name_in_a_to_z_order_pokemon = pokemon.sort_values("Name")
    frame_name_in_a_to_z_order_pokemon = pd.DataFrame(name_in_a_to_z_order_pokemon)
    print(frame_name_in_a_to_z_order_pokemon[["Name", "Type 1", "Type 2", "Total", "HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed", "Generation", "Legendary"]])

def display_dataframe_of_legendary(pokemon):
    legendary_pokemon = pokemon[pokemon["Legendary"] == True]
    frame_legendary_pokemon = pd.DataFrame(legendary_pokemon)
    print(frame_legendary_pokemon[["Name", "Legendary", "Type 1", "Type 2", "HP", "Attack", "Defense", "Speed"]])

def search_by_name(pokemon):
    try:
        while True:
            _continue = input("Press m to go back to main menu or press any other key to continue. ")
            print()

            if _continue.lower() != "m":
                search_input = input("Input a Pokemon name: ")
                print()
                associated_data = pokemon[pokemon["Name"] == search_input]
                frame_associated_data = pd.DataFrame(associated_data)

                if frame_associated_data.shape[0] == 0: # if there are 0 rows
                    print("Sorry, record not found. Please try again!\n")
                else:
                    print(f"Bravo! Here are all records for {search_input}:\n")
                    print(frame_associated_data)
                    print()
            else:
                print("Thank you!")
                break
    except:
        print("Something went wrong. Please try again!")

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
            # display GRASS type pokemon, could be Type 1 GRASS or Type 2 GRASS
            display_dataframe_of_grass_type(pokemon)
        elif command == "4":
            display_dataframe_of_hp_highest_to_lowest_order(pokemon)
        elif command == "5":
            display_dataframe_of_name_in_a_to_z_order(pokemon)
        elif command == "6":
            display_dataframe_of_legendary(pokemon)
        elif command == "7":
            search_by_name(pokemon)
        elif command == "8":
            break
        else:
            print("Unknown command. Please try again.")

    # farewell message
    print("Thank you for using the Incredible Pokemon Data. See you later for more interesting about the Pokemon!")

if __name__ == "__main__":
    main()