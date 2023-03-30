import sqlite3 as sl
def create_connection(db_name):
    conn = None
    try:
        conn = sl.connect(db_name)
        return conn
    except sl.Error as error:
        print(error)

def create_table(conn, sql):
            try:
                cursor = conn.cursor()
                cursor.execute(sql)
            except sl.Error as error:
                print(error)


def create_product(conn, product: tuple):
    try:
        sql = '''insert into products (product_title, price, quantity)
        values (?, ?, ?)
        '''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sl.Error as ww:
        print(ww)



def update_quantity(conn, product: tuple):
    try:
        sql = '''UPDATE products set quantity = ? WHERE id = ?
        '''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sl.Error as error:
        print(error)


def update_price(conn, product: tuple):
    try:
        sql = '''UPDATE products set price = ? WHERE id = ?
        '''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sl.Error as error:
        print(error)

def delete_product(connection, id):
    try:
        sql = '''DELETE FROM product WHERE id = ?'''
        cursor = connection.cursor()
        cursor.execute(sql, (id,))
        connection.commit()
    except sl.Error as e:
        print(e)

def select_all_products (connection, limit):
    try:
        sql = '''SELECT * FROM alL products >= ?'''
        cursor = connection.cursor()
        cursor.execute(sql, (limit,))

        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sl.Error as e:
        print(e)
def select_by_price_and_quantity(conn, limit):
    try:
        sql = '''SELECT * FROM products WHERE price < ? and quantity > ?
        '''
        cursor = conn.cursor()
        cursor.execute(sql, limit)
        rows = cursor.fetchall()

        for row in rows:
            print(row)
    except sl.Error as error:
        print(error)
def search_by_word(conn, word):
    try:
        sql = '''SELECT * FROM products WHERE product_title like ?
        '''
        cursor = conn.cursor()
        cursor.execute(sql, ('%'+word+'%',))
        rows = cursor.fetchall()

        for row in rows:
            print(row)
    except sl.Error as error:
        print(error)


con = sl.connect('hw.db')
sql_create_product_table = '''
CREATE TABLE products (
id Product INTEGER NOT NULL AUTOINCREMENT,
product_title VARCHAR(200) NOT NULL,
price DOUBLE(10,2) NOT NULL DEFAULT 0.0,
quantity INTEGER (5) NOT NULL DEFAULT 0'''


connection = create_connection(con)
create_table(connection, sql_create_product_table)
create_product(connection, ('Пепси', 80.5, 10))
create_product(connection, ('Сэндвич', 75.89, 5))
create_product(connection, ('Мыло детское', 30.25, 8))
create_product(connection, ('Вода газированная', 30.15, 4))
create_product(connection, ('Вода со вкусом лимона', 35.67, 12))
create_product(connection, ('Вода со вкусом банана', 49.99, 9))
create_product(connection, ('Шоколад', 120.34, 15))
create_product(connection, ('Печенье шоколадное', 115.58, 7))
create_product(connection, ('Печенье овсяные', 138.12, 15))
create_product(connection, ('Чипсы', 125.19, 11))
create_product(connection, ('Чипсы со вкусом краба', 123.79, 8))
create_product(connection, ('Halls', 34.45, 17))
create_product(connection, ('Жвачка', 35.23, 10))
create_product(connection, ('Ручка синяя', 96.5, 6))
create_product(connection, ('Молоко', 97.1, 12))
update_quantity(connection, (13, 7))
update_price(connection, (33.33, 12))
delete_product(connection, 2)
select_all_products(connection)
select_by_price_and_quantity(connection, (100, 5))
search_by_word(connection, 'Мыло')
connection.close()




