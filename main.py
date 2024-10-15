"""
Name: Aaryan Sharma
Program-2 : Chicago Lobbyist Database App
CS - 341 (Spring 2024)
Professor: Ellen Kidane
"""


import sqlite3 as sq
import objecttier


def stats ():                                                                                                           # This function is used to display the statistics at the very start of the program.
    conn = sq.connect("Chicago_Lobbyists.db")

    print("** Welcome to the Chicago Lobbyist Database Application **\n")
    print("General Statistics:")
    print(f"  Number of Lobbyists: {objecttier.num_lobbyists(conn):,}")
    print(f"  Number of Employers: {objecttier.num_employers(conn):,}")
    print(f"  Number of Clients: {objecttier.num_clients(conn):,}")

    conn.close()


def func1 ():                                                                                                           # This function is used to run Command-1 for the program.
    conn = sq.connect("Chicago_Lobbyists.db")
    lobbyistName = input("Enter lobbyist name (first or last, wildcards _ and % supported): ")
    print()
    lobbyistList = objecttier.get_lobbyists(conn, lobbyistName)                                                         # Utilizing the get_lobbyist function, in order to display the details of the lobbyist with name "lobbyistName"

    print("Number of lobbyists found:", len(lobbyistList))
    print()

    if (len(lobbyistList) > 100):
        print("\nThere are too many lobbyists to display, please narrow your search and try again...")

    else:
        for lobbyist in lobbyistList:
            print(f"{lobbyist.Lobbyist_ID} : {lobbyist.First_Name} {lobbyist.Last_Name} Phone: {lobbyist.Phone}")

        print()

    conn.close()


def func2():                                                                                                            # This function is used to run Command-2 for the program.
    conn = sq.connect("Chicago_Lobbyists.db")

    lobbyistId = input("Enter Lobbyist ID: ")
    print()
    lobbyistDetails = objecttier.get_lobbyist_details(conn, lobbyistId)                                                 # Utilizing the get_lobbyist_details function, in order to display the details of the lobbyist with id "lobbyistID"

    if not lobbyistDetails:
        print("No lobbyist with that ID was found.")
        print()

    else:
        outputYear = "  Years Registered: "
        outputEmployers = "  Employers: "

        for year in lobbyistDetails.Years_Registered:
            outputYear += f"{year}, "

        for employer in lobbyistDetails.Employers:
            outputEmployers += f"{employer}, "

        print(f"{lobbyistDetails.Lobbyist_ID} :")
        print(f"  Full Name: {lobbyistDetails.Salutation} {lobbyistDetails.First_Name} {lobbyistDetails.Middle_Initial} {lobbyistDetails.Last_Name} {lobbyistDetails.Suffix}")
        print(f"  Address: {lobbyistDetails.Address_1} {lobbyistDetails.Address_2} , {lobbyistDetails.City} , {lobbyistDetails.State_Initial} {lobbyistDetails.Zip_Code} {lobbyistDetails.Country}")
        print(f"  Email: {lobbyistDetails.Email}")
        print(f"  Phone: {lobbyistDetails.Phone}")
        print(f"  Fax: {lobbyistDetails.Fax}")
        print(outputYear)
        print(outputEmployers)
        print(f"  Total Compensation: ${lobbyistDetails.Total_Compensation:,.2f}")
        print()

    conn.close()


def func3():                                                                                                            # This function is used to run Command-3 for the program.
    conn = sq.connect("Chicago_Lobbyists.db")
    N = int(input("Enter the value of N: "))
    if (N <= 0):
        print("Please enter a positive value for N...")

    else:
        year = input("Enter the year: ")
        print()
        lobbyistDetails = objecttier.get_top_N_lobbyists(conn, N, year)                                                 # Utilizing the get_top_N_lobbyists function, in order to display the details of the lobbyists that are ranked in the top "N" spots.

        for index, lobbyist in enumerate(lobbyistDetails, start=1):
            print(f"{index} . {lobbyist.First_Name} {lobbyist.Last_Name}")
            print(f"  Phone: {lobbyist.Phone}")
            print(f"  Total Compensation: ${lobbyist.Total_Compensation:,.2f}")
            print("  Clients: ", end="")
            for client in lobbyist.Clients:
                print(f"{client}, ", end="")
            print("\n")


    conn.close()


def func4 ():                                                                                                           # This function is used to run Command-4 for the program.
    conn = sq.connect("Chicago_Lobbyists.db")
    year = input("Enter year: ")
    lobbyistID = input("Enter the lobbyist ID: ")

    val = objecttier.add_lobbyist_year(conn, lobbyistID, year)                                                          # Adding the lobbyist with ID "lobbyistID" to the database.

    if (val == 0 or val == -1):
        print("\nNo lobbyist with that ID was found.\n")

    else:
        print("\nLobbyist successfully registered.\n")

    conn.close()

def func5 ():                                                                                                           # This function is used to run Command-5 for the program.
    conn = sq.connect("Chicago_Lobbyists.db")
    lobbyistID = input("Enter the lobbyist ID: ")
    salutation = input("Enter the salutation: ")
    val = objecttier.set_salutation(conn, lobbyistID, salutation)                                                       # Adding the salutation for lobbyist with ID "lobbyistID" to the database.

    if (val == 0 or val == -1):
        print("\nNo lobbyist with that ID was found.\n")

    else:
        print("\nSalutation successfully set.\n")

    conn.close()


def menu ():                                                                                                            # This function drives the main menu, and is called in the "main" function.
    choice = input("Please enter a command (1-5, x to exit): ")
    print()

    while (choice != "x"):
        if (choice < '1' or choice > '5' or not choice.isnumeric()):
            print("**Error, unknown command, try again...")
            choice = input("Please enter a command (1-5, x to exit): ")
            print()
            continue

        elif (choice == '1'):
            func1()

        elif (choice == '2'):
            func2()

        elif (choice == '3'):
            func3()

        elif (choice == '4'):
            func4()

        elif (choice == '5'):
            func5()

        choice = input("Please enter a command (1-5, x to exit): ")
        print()


if __name__ == "__main__":
    stats()
    print()
    menu()