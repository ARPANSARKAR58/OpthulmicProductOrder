'''
	Python script to declare following:
        Defining file path, location, DB credentials, 
        Global variables, logger info format
	@author : Vrx_lences @Anirudha
'''
# from setuptools import setup

# setup(
#     name='anirudha',
#     packages=['anirudha'],
#     include_package_data=True,
#     install_requires=[
#         'flask',
#     ],
# )
import logging

# Set the log level
LOG_LEVEL = "DEBUG"

# Set the logger settings
logging.basicConfig(format='\n\t%(asctime)s - %(levelname)s \n %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=LOG_LEVEL)

# Encryption settings



# =============================================================================
# Flag List for node updates with default list values as False
# =============================================================================
node_settings_flag_list =  [False for i in range(100)]
# =============================================================================

# =============================================================================
# DataBase credentials for debugging (Anirudha's system) SQL SERVER local
# =============================================================================
# host_ms = 'ADAS\SQLEXPRESS2019'
# user_ms = 'sa'
# password_ms = 'Paromita@19'
# schema_ms = 'anurudha'
# =============================================================================
# DataBase credentials for debugging (Azure's) SQL SERVER
# =============================================================================
# host_ms = 'vrx.database.windows.net'
# user_ms = 'sftuser'
# password_ms = 'Pass@word_'
# schema_ms = 'vrxlab'


host_ms = 'ADAS\MSSQL2019EXP'
user_ms = 'sa'
password_ms = 'Itteam@19'
schema_ms = 'OPODB'

# =============================================================================
# Logging method
# =============================================================================
def logger(tag = "", value = "", level = "info"):
    if level == "debug":
        logging.debug("===== %s = %s \n", tag, value)
        
    elif level == "info":
        logging.info("===== %s \n", tag)
        
    if level == "warning":
        logging.debug("===== %s = %s \n", tag, value)
        
    if level == "error":
        logging.error("===== %s = %s \n", tag, value)
# =============================================================================
DEPARTMENT_LOGISTIC = 1
DEPARTMENT_CASTOMER_SERVICE = 2
DEPARTMENT_STOCK = 3
DEPARTMENT_RX = 4
DEPARTMENT_FITTING = 5
DEPARTMENT_DESPATCH = 6
WEARING_CONNECTION = 'Module failed to respond Please check wiring.'
#============================================================================