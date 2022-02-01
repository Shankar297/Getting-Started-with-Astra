from db_connection import Connection

print('====================================================')
print('Inserting......')

try:
    connection=Connection()
    emp_id=int(input('Select your Id: '))
    emp_city=(input('Select your City: '))
    emp_name=(input('Select your Name: '))
    emp_phone=int(input('Select your Phone Number: '))
    emp_sal=int(input('Select your Salary: '))

    output=connection.session.execute(
        "INSERT INTO emp (emp_id, emp_city, emp_name, emp_phone,emp_sal) VALUES(%s,%s,%s,%s,%s)",
        [emp_id, emp_city, emp_name, emp_phone, emp_sal]
    )
except Exception as e:
    print(e)
    print('Failure')
else:
    print('Details inserted ')
    print('Success')
    print('Closing connection (up to 10s)')
finally:
    connection.close()
print('========================================================')