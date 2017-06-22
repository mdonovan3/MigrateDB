import psycopg2
from psycopg2 import extras

hostname = '192.168.130.9'
username = 'inventory'
password = '1261brg'
database = 'inventory'
wine_category_id = 1

conn = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
cur.execute( "SELECT * FROM products p, product_instances pi where p.product_id = pi.product_id \
and p.major_category_id = 1" )
for row in cur.fetchall() :
    print("%s, %s" % (row['inventory_name'], row['product_name']))
    
    
    