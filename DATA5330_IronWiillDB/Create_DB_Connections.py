#Connect to AWS hosted Postgres DB 'iwdb':
dmconn = psycopg2.connect(
    database= settings.database, 
    user= settings.user, 
    password= settings.password,
    host= settings.host, 
    port= settings.port
)
cursor = dmconn.cursor()

#Connect to USU MS SQL Database:
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                      'Server= settings.Server'
                      'Database= settings.DatabaseUSU;'
                      'UID=settings.UID;'
                      'PWD=settings.PWD;'
                      'Trusted_Connection=no;')
