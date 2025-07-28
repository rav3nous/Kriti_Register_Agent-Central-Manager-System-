from agents import function_tool
import mysql.connector

@function_tool
def update_db(name:str,email:str,country_code:str,phone_number:str,password:str):
    try:
        connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345678",
        database="register_agent"
        )
        cursor=connection.cursor()
        cursor.execute(f"insert into registerCredentials values ('{name}','{email}','{country_code}','{phone_number}','{password}')")
        connection.commit()
        connection.close()
        return True
    except:
        return False

