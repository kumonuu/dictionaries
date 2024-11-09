country = {}
while True: 
    print("""
    1. insert element
    2. display country
    3. display capital
    4. get the capital
    5. delete
    6. exit
    """)
    menu_choice = int(input("Enter a number from 1-4: "))
    if menu_choice == 1:
        country_input = input("What is the country? ")
        capital_input = input("What is the capital? ")
        country[country_input] = capital_input
    elif menu_choice == 2:
        print(country.keys())
    elif menu_choice == 3:
        print(country.values())
    elif menu_choice == 4:
        country_input = input("What is the country? ")
        print(country.get(country_input, "No capital found"))
    elif menu_choice == 5:
        country_input = input("What is the country? ")
        del country[country_input]
    else:
        break