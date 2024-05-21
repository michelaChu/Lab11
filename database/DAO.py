from database.DB_connect import DBConnect
from model.product import Product

class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getALlColors():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct (Product_color)
                    from go_products"""

        cursor.execute(query)

        for row in cursor:
            result.append(row["Product_color"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getALlNodes(colore):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select *
                from go_products
                where Product_color =%s"""

        cursor.execute(query, (colore,))

        for row in cursor:
            result.append(Product(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getALlEdges(anno, colore):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select gds1.Product_number as v1, gds2.Product_number as v2, count(distinct(gds1.`Date`)) as peso
                from go_daily_sales gds1
                join go_daily_sales gds2 on gds1.Retailer_code = gds2.Retailer_code 
                and gds1.`Date`= gds2.`Date` and year(gds1.`Date`) = %s
                join go_products gp1 on gp1.Product_number = gds1.Product_number 
                join go_products gp2 on gp2.Product_number = gds2.Product_number
                and gp1.Product_color = gp2.Product_color and gp1.Product_color = %s
                where gds1.Product_number < gds2.Product_number
                group by gds1.Product_number, gds2.Product_number
                having count(*)>0"""

        cursor.execute(query, (anno, colore,))

        for row in cursor:
            result.append((row["v1"], row["v2"], row["peso"]))

        cursor.close()
        conn.close()
        return result

