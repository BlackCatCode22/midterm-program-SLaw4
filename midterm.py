# Write a program in your choice of language (Python, Java, C++) that performs the following tasks:

# Use fileIO to read the input file (arrivingAnimals.txt)
# Write a fuction or method that calculates a birthday from the originating data.
# Write a function or method to create a uniqueID for each animal.
# Write a function or method to name each new animal using animalNames.txt
# Write functions or methods to calculate a birthday, color, weight, and origin for each new animal.
# Organize the animals into habitats (each species must have its own habitat).
# Use fileIO to produce an output text file similiar to (sampleOutput.txt)
# Use 2D arrays and 1D arrays to organize your zoo.

# You may use structs, classes, lists, linked lists if you like, but these data structures are not part of the first half of our class. We will use these programming techniques for our final priograms.

# Information will arrive in the following format with an unknown number of lines:

# 6 year old female lion, born in spring, tan color, 300 pounds, from Zanzibar, Tanzania 12 year old female lion, born in winter, dark tan color, 375 pounds, from KopeLion, Tanzania
import numpy as np
import re
from datetime import date
import math

num_of_hyenas = 0
num_of_lions = 0
num_of_tigers = 0
num_of_bears = 0

hyena_list = []
lion_list = []
tiger_list = []
bear_list = []


def calc_age_in_years(birth_date):
    today = date.today()

    # the parameter birth_date must be a date object
    # we can subtract one date object from another date object
    date_diff = today - birth_date

    # Use the .days method on date_diff to get age in days
    age_in_days = date_diff.days

    # divide by days in a year
    age_in_years = age_in_days/365.242199

    # truncate to get age in years
    age_in_years = math.trunc(age_in_years)

    # return a whole number representing years
    return age_in_years


print("\n\n\n")

my_file = open("C:/Users/lawse/myGitDir/midterm/animalNames.txt",
               "r", encoding="utf-8")

# Read the file line by line into a data structure called 'Lines_names'
Lines_names = my_file.readlines()

# Close the input file (if you open a file, be sure to close it)
my_file.close()

# Output each line in Lines
line_count = 0
for line in Lines_names:
    print("Line " + str(line_count+1) + ":  " + line)
    line_count += 1

# Read the file into a Python list
list_of_lines = []
for line in Lines_names:
    list_of_lines.append(line)

# Demonstrate the list
print("\n\n Here is a list of the lines in the animal names file...\n\n")
print("line 0 is: " + str(list_of_lines[0]))

hyena_names_list = list_of_lines[2].replace(',', "").split()
lion_names_list = list_of_lines[6].replace(',', "").split()
tigers_names_list = list_of_lines[10].replace(',', "").split()
bears_names_list = list_of_lines[14].replace(',', "").split()


def the_birthday_function(years_old, season_of_birth):
    birth_year = 2023 - int(years_old.strip())
    birth_year = birth_year - 1

    if season_of_birth == "spring":
        birthday_date = "03-21"
    elif season_of_birth == "summer":
        birthday_date = "06-21"
    elif season_of_birth == "fall":
        birthday_date = "09-21"
    elif season_of_birth == "winter":
        birthday_date = "12-21"
    else:
        birthday_date = "01-01"

    animal_birthday = str(birth_year) + "-" + birthday_date

    return animal_birthday

# uniqueID function


def uniqueID(species_name, num_of_animals_in_species):
    match species_name:
        case "hyena":
            prefix = "Hy"
        case "lion":
            prefix = "Li"
        case "tiger":
            prefix = "Ti"
        case "bear":
            prefix = "Be"
        case default:
            prefix = "Xx"

    return prefix + "0" + str(num_of_animals_in_species)


print("\n\n Welcome to Dennis's Digital Zoo \n\n")

my_file = open(
    "C:/Users/lawse/myGitDir/midterm/arrivingAnimals.txt", "r", encoding="utf-8")

# Read the file line by line into a data structure called 'Lines'
Lines = my_file.readlines()

# Close the input file (if you open a file, be sure to close it)
my_file.close()

# Output each line in Lines
line_count = 0
for line in Lines:
    print("Line " + str(line_count+1) + ":  " + line)
    line_count += 1

# Read the file into a Python list
list_of_lines = []
for line in Lines:
    list_of_lines.append(line)

# Demonstrate the list
print("\n\n Here is a list of the lines in the text file...\n\n")
print("line 0 is: " + str(list_of_lines[0]))


# Get the file contents into an array
# Talk about the difference between list and array
my_array = np.asarray(list_of_lines)

# Find how many elements are in our new array
num_of_array_elements = my_array.size

# Output the new array
array_line = 0
for element in my_array:
    print("\n" + str(my_array[array_line]))
    array_line += 1

# Process each element of the new array
array_line = 0
for element in my_array:
    print("\n" + str(my_array[array_line]))

    # get the data elements needed from this one line for the birthday
    #
    # Split on blank space to get words in the line
    split_on_space = my_array[array_line].split(" ")
    print(split_on_space)

    # from this split, get what data elements we can
    # ['4', 'year', 'old', 'female', 'hyena,', 'born', 'in', 'spring,', 'tan', 'color,', '70', 'pounds,', 'from', 'Friguia', 'Park,', 'Tunisia\n']
    # years_old will always be the first data element, so we use 0 for the first element in our split list
    years_old = split_on_space[0]

    # output every small change so you know you got it right
    print("years_old: " + years_old)

    # next is sex, which will always be the fourth word (element number 3 because list element numbering starts at 0)
    sex = split_on_space[3]
    print("sex: " + sex)

    # we can get species here
    species = split_on_space[4]
    print("species: " + species)

    # we have a comma at the end of this word, so we must remove it
    species = re.sub(",", "", species)

    # test with a print()
    print(" species without a comma: " + species)

    # season of birth
    season = split_on_space[7]
    print("season: " + season)

    # we have a comma at the end of this word, so we must remove it
    season = re.sub(",", "", season)

    # test with a print()
    print(" season without a comma: " + season)

    # we got a couple of our needed data elements. now let's calculate what we can using the functions we wrote
    birth_date = the_birthday_function(years_old, season)
    print("birthdate: " + birth_date)

    # increment the number of animals in species
    # and while we know the species...
    # generate a uniqueID and get a name!
    if (species == "hyena"):
        num_of_hyenas += 1

        # and now we can call uniqueID()
        unique_id = uniqueID(species, num_of_hyenas)

        # get a name from the name list that we created with file io
        # if we are here, we know we need a hyena name
        name = hyena_names_list[num_of_hyenas]
    elif (species == "lion"):
        num_of_lions += 1

        # and now we can call uniqueID()
        unique_id = uniqueID(species, num_of_lions)

        # get a name from the name list that we created with file io
        # if we are here, we know we need a lion name
        name = lion_names_list[num_of_lions]
    elif (species == "tiger"):
        num_of_tigers += 1

        # and now we can call uniqueID()
        unique_id = uniqueID(species, num_of_tigers)

        # get a name from the name list that we created with file io
        # if we are here, we know we need a hyena name
        name = tigers_names_list[num_of_tigers]
    elif (species == "bear"):
        num_of_bears += 1

        unique_id = uniqueID(species, num_of_bears)

        name = bears_names_list[num_of_bears]
    else:
        print("\n error in incrementing species")

    print("unique_id: " + unique_id)
    print("name is: " + name)
    ##########################################

    # Split on comma because some data elements (like color, wright, and origin)
    # have a varied number of words
    after_split_on_comma = my_array[array_line].split(", ")

    print(after_split_on_comma)

    color = after_split_on_comma[2]
    print("color = " + color)

    weight = after_split_on_comma[3]
    print("weight is: " + weight)

    origin = after_split_on_comma[4] + " " + after_split_on_comma[5]
    print("origin = " + origin)

    origin = origin.strip()

    # Last two items, we need an age in years and an arrived date
    split_on_dash = birth_date.split("-")
    my_year = split_on_dash[0]
    my_month = split_on_dash[1]
    my_day = split_on_dash[2]

    # test our split()
    print("my_year = " + my_year)
    print("my_month = " + my_month)
    print("my_day = " + my_day)

    # cast strings to ints because that's what our date object needs
    birth_date_object = date(int(my_year), int(my_month), int(my_day))

    # pass our new date object to our calc_age_in_years() function
    animal_age_in_years = calc_age_in_years(birth_date_object)

    # validate our function
    print("animal_age_in_years is: " + str(animal_age_in_years))

    # arrival date is easy (after all that date() processing!
    arrival_date = date.today()
    print("arrival_date = " + str(arrival_date))

    # That should be it. Let's see....
    str01 = unique_id + "; " + name + "; " + \
        str(animal_age_in_years) + " years old; " + \
        "birth date: " + birth_date + "; "
    str02 = color + "; " + sex + "; " + weight + "; " + \
        origin + "; arrived: " + str(arrival_date)

    output_line = str01 + str02

    print("\noutput_line = " + output_line)

    # get this output line into the proper list()
    if (species == "hyena"):
        hyena_list.append(output_line)
    elif (species == "tiger"):
        tiger_list.append(output_line)
    elif (species == "lion"):
        lion_list.append(output_line)
    else:
        bear_list.append(output_line)

    array_line += 1
    # End of processing each line with the two splits()
    # Write our species list to our output file.
    print("Hyena Habitat: \n\n")
    for line in hyena_list:
        print(line + "\n")

    my_file = open("midTermOutput.txt", "w", encoding="utf-8")

    my_file.write(
        "Midterm Program Output; by programmer name, Spring 2023, Fresno, CA\n\n")

    my_file.write("Hyena Habitat: \n\n")
    for i in hyena_list:
        my_file.write(i)
        my_file.write("\n")
    my_file.write("\n\n")

    my_file.write("Lion Habitat: \n\n")
    for i in lion_list:
        my_file.write(i)
        my_file.write("\n")
    my_file.write("\n\n")

    my_file.write("Tiger Habitat: \n\n")
    for i in tiger_list:
        my_file.write(i)
        my_file.write("\n")
    my_file.write("\n\n")

    my_file.write("Bear Habitat: \n\n")
    for i in bear_list:
        my_file.write(i)
        my_file.write("\n")
    my_file.write("\n\n")

    my_file.close()
