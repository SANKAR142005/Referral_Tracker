import mysql.connector

def getconnection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="prince@142005",
        database="referral_db"
    )
