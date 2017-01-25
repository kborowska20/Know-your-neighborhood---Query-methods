import sys
from city import City
from voivodeship import Voivodeship

def printing_menu():
    print("What would you like to do:\n"
    "(1) List statistics\n"
    "(2) Display 3 cities with longest names\n"
    "(3) Display county's name with the largest number of communities\n"
    "(4) Display locations, that belong to more than one category\n"
    "(5) Advanced search\n"
    "(0) Exit program\n")


def get_from_object_to_list(list_of_obj):
    list_of_all = []
    for persons in list_of_obj:
        list = []
        list = [persons.name, persons.surname, persons.age, persons.gender, persons.pesel, persons.login, persons.status, persons.date_when_added]
        list_of_all.append(list)
    return list_of_all


def print_table(table, title_list):

    table.insert(0, title_list)
    width_list = []
    for i in range(len(table[0])):
        longest_string = 0
        for row in table:
            if len(row[i]) > longest_string:
                longest_string = len(row[i])
        width_list.append(longest_string)
    print("╔", end="")
    for column in range(len(table[0])):
        print("{0:═^{w}}".format("═", w=width_list[column]+2), end="")
        if column+1 != len(table[0]):
            print("╦", end="")
    print("╗\n", end="")
    '''content'''
    for row_number, row in enumerate(table):
        for column, cell in enumerate(row):
            print("║{0:^{w}}".format(cell, w=width_list[column]+2), end="")
        print("║\n", end="")
        if row_number+1 != len(table):
            print("╠", end="")
            for column, cell in enumerate(row):
                print("{0:═^{w}}".format("═", w=width_list[column]+2), end="")
                if column+1 != len(table[0]):
                    print("╬", end="")
            print("╣\n", end="")
        '''footer'''
        if row_number+1 == len(table):
            print("╚", end="")
            for column, cell in enumerate(row):
                print("{0:═^{w}}".format("═", w=width_list[column]+2), end="")
                if column+1 != len(table[0]):
                    print("╩", end="")
            print("╝")
    table.remove(table[0])





def main():
    while True:

        printing_menu()
        user_input = input("Select an option:")

        if user_input == "1":
            head = []
        elif user_input == "2":
            pass
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        elif user_input == "5":
            pass
        elif user_input == "0":
            sys.exit()

main()