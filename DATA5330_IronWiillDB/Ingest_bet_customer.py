#INGEST INTO "iwdm.public.bet_customer":
dmconn.close()

#Connect to ironwill RDB:
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                      'Server=stairwaytoheaven.usu.edu;'
                      'Database=ironwill;'
                      'UID=pupuser;'
                      'PWD=longpasswordsareablight;'
                      'Trusted_Connection=no;')

df = pd.read_sql('''SELECT *
                    FROM customer_table;''',conn)
conn.close()

df['customer_name'] = df['customer_name'].str.replace('\'', '')
df[['customer_fname','customer_lname']] = df['customer_name'].str.split(pat= ' ',n=1, expand=True)

#Reconnect to iwdm DM:
dmconn = psycopg2.connect(
    database="iwdm", 
    user='tyler', 
    password='goaggies1234',
    host='tylerdata5330.cbg3gavcvfmn.us-west-2.rds.amazonaws.com', 
    port= '5432'
)
cursor = dmconn.cursor()

for x in df.index:
    cursor.execute('''INSERT INTO bet_customer (customer_id,
                                                customer_fname,
                                                customer_lname,
                                                customer_age,
                                                customer_since,
                                                customer_household,
                                                customer_income,
                                                customer_type,
                                                customer_mode_color)

                      VALUES (%d, '%s', '%s', %d, %d, %d, %d, '%s', '%s')''' % (df['customer_id'].loc[x], df['customer_fname'].loc[x], df['customer_lname'].loc[x], df['customer_age'].loc[x], df['customer_since'].loc[x], df['household_size'].loc[x], df['customer_income'].loc[x], df['customer_type'].loc[x], df['mode_color'].loc[x]))
    dmconn.commit()
    
    cus_id_str = str(df['customer_id'].loc[x])
    print("Betting customer_id %s record ingested" % (cus_id_str))
