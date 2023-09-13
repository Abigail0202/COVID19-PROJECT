import covid_details

def access_function():
    print("***** Welcome to COVID-19 Data Maintenance Survey Software *****")
    print("1-> COVID 19 DETAILS")
    print("2-> VIEW COVID 19 DETAILS")
    print("3-> UPDATE COVID 19 DETAILS")
    print("4-> DELETE COVID 19 DETAILS")

    user = int(input("Enter Your Number: "))
    try:
        if user == 1:
            covid_details.covid19_details()
        elif user == 2:
            covid_details.view_covid19_details()
        elif user == 3:
            covid_details.update_covid19_details()
        elif user == 4:
            covid_details.delete_covid19_details()
        else:
            print("Please Type 1, 2, 3, or 4 only")
    except ValueError:
        print("Type Number Only")

access_function()
