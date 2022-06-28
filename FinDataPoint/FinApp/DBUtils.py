from . import Defaults
import pyodbc
import textwrap

def DB_Execute_MS(sql_query, action):

    Defaults.logger("Entering -> | DB_Insert() |", level = "info")
    print('inside',sql_query, action)
    # Open database connection
    #db = pymssql.connect(host ='ADAS\SQLEXPRESS2019',user ='sa',password ='Paromita@19',database ='vrx_sfts')
    # db = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+Defaults.host_ms+';DATABASE='+Defaults.schema_ms+';UID='+Defaults.user_ms+';PWD='+ Defaults.password_ms)
    # constr =textwrap.dedent('DRIVER={ODBC Driver 17 for SQL Server};Server=tcp:'+Defaults.host_ms+';Database='+Defaults.schema_ms+';Uid='+Defaults.user_ms+';Pwd='+ Defaults.password_ms+';Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
    constr =textwrap.dedent('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+Defaults.host_ms+';DATABASE='+Defaults.schema_ms+';UID='+Defaults.user_ms+';Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;convert_unicode=True;PWD='+ Defaults.password_ms)
    db = pyodbc.connect(constr)
    # print(db)
    # db.setdecoding(pyodbc.SQL_CHAR, encoding='utf-8')
    # db.setdecoding(pyodbc.SQL_WCHAR, encoding='utf-8')
    db.setencoding(encoding='utf-8')
    # db.setdecoding(pyodbc.SQL_WMETADATA, encoding='utf-32le')
    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    if action == "insert":
        try:
                # Execute the SQL command
            status = cursor.execute(sql_query)
            print("status",status)
                # Commit your changes in the database
            db.commit()
            return status
        except:
            # Rollback in case there is any error
            db.rollback()
            Defaults.logger("DB INSERT FAILED", sql_query, "debug")
            return False

    elif action == "fetch":
        try:
            # Execute the SQL command
            print("fatch")
            print(sql_query)
            cursor.execute(sql_query)
            # fetch all the content from the query
            fetched_content = cursor.fetchall()
            # for row in fetched_content:
            #         for culm in row:
            #             col=culm
            #             col = col.encode('utf-8').strip()
            return fetched_content

        except Exception as e:
            # log the exception
            Defaults.logger("DB FETCH EXCEPTION", e, "debug")
            Defaults.logger("DB FETCH EXCEPTION sql", sql_query, "debug")
            return False
    
    



    elif action == "delete":
        try:
    # cursor   
            cursor.execute(sql_query)   
    # commit
            db.commit()    
    # total number of rows inserted  
        except pyodbc.connector.Error as err:   
            print("Error:", err.message)
            db.rollback()
            Defaults.logger("DB delet FAILED", sql_query, "debug")
            return False
    # close connection

    return True


