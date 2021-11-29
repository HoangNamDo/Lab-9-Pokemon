# first import pandas
import pandas as pd

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

# ASSIGNMENT INSTRUCTIONS ---

# BUILD A MENU SYSTEM WITH OPTIONS FOR THE FOLLOWING OPTIONS

# 1 - Print out a report with only the following fields displaying - Name, Type, Generation

# 2 - Print out a report displaying the name, HP, Attack, Defense, Speed 

# 3 - Create a dataFrame displaying all of the GRASS type Pokemon in the csv file

# 4 - Create a dataFrame displaying all of the Pokemon in order of HP (highest to lowest)

# 5 - Create a dataFrame displaying all of the Pokemon in order of NAME A-Z

# 6 - Create a dataFrame of all the LEGENDARY Pokemon. 

# 7 - Create a search for a name of a Pokemon and return the data associated with the Pokemon. Do a try/except to catch any error or record not found. Allow the user to search multiple times until they choose to exit.