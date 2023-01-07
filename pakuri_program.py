from pakudex import *

#pakudex = Pakudex(capacity=userinput)

# 1. add pakuri
#pakudex.add_pakuri(userinput2)
if __name__ == "__main__":


    print("Welcome to Pakudex: Tracker Extraordinaire!")
    real_number = True
    while real_number == True:        # getting capacity
        try:
            max_capacity = int(input("Enter max capacity of the Pakudex:"))
            if max_capacity < 0:
                raise ValueError
            real_number = False

        except ValueError:               # print error message if value error is raised
            print("Please enter a valid size.")



    print(f"The Pakudex can hold {max_capacity} species of Pakuri.")
    Pakudex_object = Pakudex(max_capacity)
    # main menu
    size = 0
    pakudex_continue = True

    while pakudex_continue == True:
        print("Pakudex Main Menu")
        print("-----------------")
        print("1. List Pakuri")
        print("2. Show Pakuri")
        print("3. Add Pakuri")
        print("4. Evolve Pakuri")
        print("5. Sort Pakuri")
        print("6. Exit\n")


        menu_choice = input("What would you like to do? ")   # input option




        if menu_choice == "1":
            pakudex_list = Pakudex_object.get_species_array()

            if pakudex_list == None:                    # error if there are no pakuri inside of the list
                print("No Pakuri in Pakudex yet!")

            else:
                count = 1
                print("Pakuri In Pakudex:")    # print out the pakuri in the list
                for item in pakudex_list:
                    print(f"{count}. {pakudex_list[count - 1]}")
                    count += 1
                print(" ")

        elif menu_choice == "2":

            critter_name = input("Enter the name of the species to display: ")
            critter_show = Pakudex_object.get_stats(critter_name)           # gets stats for specific critter

            if critter_show == None:                # error if there is no pakuri under that name
                print("Error: No such Pakuri!\n")
                continue

            print(f"Species: {critter_name}")           # prints states
            print(f"Attack: {critter_show[0]}")
            print(f"Defense: {critter_show[1]}")
            print(f"Speed: {critter_show[2]}\n")




        elif menu_choice == "3":

            if max_capacity == size:
                print("Error: Pakudex is full!")                # if pakudex is full error
                continue

            critter_add = input("Enter the name of the species to add: ")
            final_test = Pakudex_object.add_pakuri(critter_add)

            if final_test == True:
                print(f"Pakuri species {critter_add} successfully added!")      # if critter has been added to pakudex
                size += 1

            if final_test == False:
                print("Error: Pakudex already contains this species!")         # pakudex already has this species


        elif menu_choice == "4":
            evolve_choice = input("Enter the name of the species to evolve: ")
            evolved_pakuri = Pakudex_object.evolve_species(evolve_choice)       # evole the pakuri based on input

            if evolved_pakuri == True:
                print(f"{evolve_choice} has evolved!")                      # if pakuri has evolved print this

            if evolved_pakuri == False:
                print("Error: No such Pakuri!")                             # print this if not evolved


        elif menu_choice == "5":
            Pakudex_object.sort_pakuri()                        # sorts the pakuri and then prints statement
            sort_result = Pakudex_object.sort_pakuri()
            if sort_result == True:
                print("Pakuri have been sorted!")


        elif menu_choice == "6":
            pakudex_continue = False   # ends the program
            print("Thanks for using Pakudex! Bye!")

        else:
            print("Unrecognized menu selection!\n")   # incorrect menu selection







