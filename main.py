# ISIT 333 Lab 9
# November 28, 2021
# Hoang Do

# first import pandas
import pandas as pd

# ASSIGNMENT INSTRUCTIONS ---

# BUILD A MENU SYSTEM WITH OPTIONS FOR THE FOLLOWING OPTIONS

# 1 - Print out a report with only the following fields displaying - 

# 2 - Print out a report displaying the  

# 3 - Create a dataFrame displaying all of the GRASS type Pokemon in the csv file

# 4 - Create a dataFrame displaying all of the Pokemon in order of HP (highest to lowest)

# 5 - Create a dataFrame displaying all of the Pokemon in order of NAME A-Z

# 6 - Create a dataFrame of all the LEGENDARY Pokemon. 

# 7 - Create a search for a name of a Pokemon and return the data associated with the Pokemon. Do a try/except to catch any error or record not found. Allow the user to search multiple times until they choose to exit.

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

def display_name_type_generation(pokemon):
    print(pokemon[["Name", "Type 1", "Type 2", "Generation"]])

def main():
    print("Welcome to MCU Superheroes Database")
    # then save data to a variable "pokemon"
    pokemon = pd.read_csv("pokemon.csv")

    ## EXAMPLE DATA CALLS - COMMENT OR REMOVE lines 7 - 25 BEFORE SUBMITTING

    # print first 5 records
    print()
    print("Top 5 records\n")
    print(pokemon.head(5))

    # print information about csv data
    print()
    print("Basic information about the Pokemon data\n")
    print(pokemon.info())

    # print statistical information about all records in the data file
    print()
    print("Basic statistical information about the Pokemon data\n")
    print(pokemon.describe())

    # print the minimum value of HP column - note this should align with the data in the describe() function
    print("The minimum HP value is", pokemon["HP"].min())
    while True:
        display_menu()
        print()
        command = input("Command: ")
        print()
        if command == "1":
            list_name_and_alias(conn, cursor)
        elif command == "2":
            list_species_and_citizenship(conn, cursor)
        elif command == "3":
            list_birth_year_and_status(conn, cursor)
        elif command == "4":
            list_portrayed_by(conn, cursor)
        elif command == "5":
            cursor = add_new_superhero(conn, cursor)
        elif command == "6":
            break
        else:
            print("Unknown command. Please try again.")

    # save the updates/inserts to the database
    conn.commit()
    # close the connection
    conn.close()
    # farewell message
    print("Thank you for using MCU superhero database. See you later for more interesting about Marvel Cinematic Universe!")

if __name__ == "__main__":
    main()