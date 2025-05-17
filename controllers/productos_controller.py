from database.connection import DatabaseConnection
from database.queries import GET_ALL_PRODUCTOS_WITH_STOCK

class ProductosController:
    def obtener_productos_con_stock(self):
        db = DatabaseConnection()
        db.connect()
        cursor = db.execute(GET_ALL_PRODUCTOS_WITH_STOCK)
        productos = cursor.fetchall() if cursor else []
        db.close()
        return productos