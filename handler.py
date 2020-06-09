import pymysql

endpoint = '#'
username = '#'
password = '#'
database = 'Transactions_Prod'
connection = pymysql.connect(
    endpoint, user=username, passwd=password, db=database)


def lambda_handler():
    cursor = connection.cursor()
    cursor.execute('select * from transactions')
    rows = cursor.fetchall()

    for row in rows:
        print("{0} {1} {2}".format(rows[0], row[1], row[2]))


lambda_handler()
