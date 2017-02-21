import sys
from printing import *
from voivodeship import *





def main():


    while True:

        Printing.printing_menu()

        user_input = input("Select an option:")

        City.data_reader("malopolska.csv")

        if user_input == "1":
            head = ["Number", "Area Type"]
            Printing.print_table(Printing.get_from_object_to_list(City.area()), head)

        elif user_input == "2":
            head = ["Number", "City"]
            Printing.print_table(City.longest_name_cities(),head)

        elif user_input == "3":
            head = ["num","name"]
            Printing.print_table(City.county_name(), head)

        elif user_input == "4":
            head = ["How much","coummunity"]
            Printing.print_table(City.lagerst_commiunty(), head)

        elif user_input == "5":
            user_input2 = input("Give me searching name: ")
            head = ["name", "area type"]
            Printing.print_table(City.searching_f(user_input2),head)

        elif user_input == "0":
            sys.exit()




if __name__ == '__main__':
    main()