from __future__ import print_function
import json
import mysql.connector

#mydb = mysql.connector.connect(host="localhost", user="root", passwd="Hydrogen@01")
#mycursor = mydb.cursor()
#mycursor.execute("show databases")
#for i in mycursor:
#    print(i)


def lambda_handler(event, context):
    #mydb = mysql.connector.connect(host="localhost", user="root", passwd="Hydrogen@01")
    #mycursor = mydb.cursor()
    #mycursor.execute("show databases")
    #for i in mycursor:
    #    print(i)
    #print("Received event: " + json.dumps(event, indent=2))
    print("value1 = " + event['key1'])
    print("value2 = " + event['key2'])
    print("value3 = " + event['key3'])
    return event['key1']  # Echo back the first key value
    #raise Exception('Something went wrong')




