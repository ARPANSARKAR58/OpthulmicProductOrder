# class DbCheckMiddleware(object):

#     def process_request(self, request):
#         try:
#             "pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+Defaults.host_ms+';DATABASE='+Defaults.schema_ms+';UID='+Defaults.user_ms+';PWD='+ Defaults.password_ms)"
#             success = True
#         except:
#             success = False                

#         request.db_connection_successful = success