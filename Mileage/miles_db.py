import sqlite3

db = sqlite3.connect('mileage.db')  #Creates of opens db file

cur = db.cursor() #need a cursor object to perform operations
"""
    Before running this test, create test_miles.db
    Create expected miles table
    create table miles (vehicle text, total_miles float);
"""
cur.execute('create table If Not Exists miles (vehicle text, total_miles float)')


class MileageError(Exception):
    pass

def add_miles(vehicle, new_miles):
    '''If the vehicle is in the database, increment the number of miles by new_miles
    If the vehicle is not in the database, add the vehicle and set the number of miles to new_miles
    If the vehicle is None or new_miles is not a positive number, raise MileageError
    '''

    if not vehicle:
        raise MileageError('Provide a vehicle name')
        vehicleInput()
    if not isinstance(new_miles, (int, float))  or new_miles < 0:
        raise MileageError('Provide a positive number for new miles')
        milesInput(vehicle)

    rows_mod = cur.execute('UPDATE MILES SET total_miles = total_miles + ? WHERE vehicle = ?', (new_miles, vehicle))
    if rows_mod.rowcount == 0:
        cur.execute('INSERT INTO MILES VALUES (?, ?)', (vehicle, new_miles))
    db.commit()


def vehicleInput():
    vehicle = input('Enter vehicle name or enter to quit:')
    vehicle = vehicleToUpper(vehicle)
    if not vehicle:
        return vehicle
    vehicleCheck = cur.execute("select * from miles where vehicle = ?", (vehicle,))
    # making a variable to test if it comes back none
    checkOutput = vehicleCheck.fetchone()
    print(checkOutput)
    return vehicle

def milesInput(vehicle):
    try:
        miles = float(input('Enter new miles for {}: '.format(vehicle,)))
        return miles
    except ValueError:
        print("Needs to be a number")
        milesInput()

def vehicleToUpper(vehicle):
    vehicle = vehicle.upper()
    return vehicle

def main():
    while True:
        vehicle = vehicleInput()
        if not vehicle:
            db.close()
            break
        miles =  milesInput(vehicle)

        add_miles(vehicle, miles)






if __name__ == '__main__':
    main()
