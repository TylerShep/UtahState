#INGEST INTO "iwdm.public.placed_bet":
dmconn.close()

#Connect to ironwill RDB:
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                      'Server=stairwaytoheaven.usu.edu;'
                      'Database=ironwill;'
                      'UID=pupuser;'
                      'PWD=longpasswordsareablight;'
                      'Trusted_Connection=no;')

df = pd.read_sql('''SELECT *
                    FROM betlog;''',conn)
conn.close()

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
    cursor.execute('''INSERT INTO placed_bet (bet_id,
                                                bet_amount,
                                                bet_on,
                                                bet_result,
                                                customer_id,
                                                game_id)
                                                
                    VALUES (%d, %d, '%s', NULL, %d, '%s')'''% (df['bet_id'].loc[x], df['bet_amount'].loc[x], df['bet_on'].loc[x], df['customer_id'].loc[x], df['game_id'].loc[x]))
                                                
    dmconn.commit()
    
    bet_id_str = str(df['bet_id'].loc[x])
    print("Betting record id %s ingested" % (bet_id_str))
