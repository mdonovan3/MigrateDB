import psycopg2

hostname = '192.168.130.9'
username = 'inventory'
password = '1261brg'
database = 'inventory'

conn = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )
cur = conn.cursor()
cur.execute( "SELECT inventory_name FROM product_instances" )
for inv_name in cur.fetchall() :
  print (inv_name)
    
    