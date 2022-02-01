from db_connection import Connection
print('=============================================================')
print('Start Service')
connection = Connection()
try:
    output = connection.session.execute("SELECT * FROM system.local")
    for row in output:
            print("You are now Connected to cluster '{}'".format(row.cluster_name))
except Exception as e:
    print(e)
    print('Failure')
else:
    print('Success')
finally:
        print('Closing connection (up to 10s)')
        connection.close()
print('================================================================')
