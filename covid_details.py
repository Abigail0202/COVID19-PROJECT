import mysql.connector
import main_details

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="covid19_db"
)

mycursor = mydb.cursor()

#covid19 details

def covid19_details():

     #insert data

    sql = "INSERT INTO covid19_details (patient_name, patient_age, gender, location, symptoms, test_result, vaccination_status, first_dosage_status, second_dosage_status) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    patient_name = input("Enter Your Name:")
    patient_age = input("Enter Your Age:")
    gender = input("Enter Your Gender:")
    location = input("Enter Your Location:")
    symptoms = input("List any symptoms (comma-separated): ").split(',')
    test_result = input("Enter your test result (positive/negative): ")
    vaccination_status = input("Are you vaccinated? (yes/no): ")

    # Define the dosage dates based on vaccination status
    if vaccination_status.lower() == 'yes':
        first_dosage_status = input("Enter the date of your first dosage: ")
        second_dosage_status = input("Enter the date of your second dosage: ")
    else:
        first_dosage_status = None
        second_dosage_status = None

    val = (patient_name, patient_age, gender, location, ','.join(symptoms), test_result, vaccination_status, first_dosage_status, second_dosage_status)
    mycursor.execute(sql, val)
    mydb.commit()
    print(f"Patient {patient_name} details have been uploaded... ! ")
    var=input("Do You Want To Continue Press Yes: ")
    if var=="yes":
       main_details.access_function()
    else:
        print(" *********** Thanks For Updating*********** ")

# view data

def view_covid19_details():
    mycursor.execute("SELECT * FROM covid19_details")  # Corrected table name
    myresult = mycursor.fetchall()
    for i in myresult:
        print(i)
    var = input("Do You Want To Continue? Press Yes: ")
    if var == "yes":
        main_details.access_function()
    else:
        print("Response recorded successfully.")

        

def update_covid19_details():

    #update data

    sql="update covid19_details set vaccination_status ='yes' where id=2"
    mycursor.execute(sql)
    mydb.commit()
    print(" ***********Updated Successfully******** ")
    var=input("Do You Want To Continue Press Yes: ")
    if var=="yes":
       main_details.access_function()
    else:
        print(" *********** Thanks For Updating*********** ")


def delete_covid19_details():

    #delete data

    column_name=input("Which column you want to delete:")
    delete_data=input(f"Which data  you want to delete in {column_name} column: ")
    sql= f"Delete from covid19_details where {column_name} = %s"
    mycursor.execute(sql, (delete_data,))
    mydb.commit()
    print(" ***********Deleted Successfully******** ")

    var=input("Do You Want To Continue Press Yes: ")
    if var=="yes":
         main_details.access_function()
    else:
        print(" *********** Thanks For Updating*********** ")

