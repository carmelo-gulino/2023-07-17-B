from database.DB_connect import DBConnect
from model.product import Product


class DAO:
    def __init__(self):
        pass

    @staticmethod
    def get_all_brands():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select distinct gp.Product_brand brand from go_products gp order by gp.Product_brand """
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row['brand'])
        cursor.close()
        cnx.close()
        return result

    @staticmethod
    def get_nodes(brand):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select * from go_products gp where gp.Product_brand = %s"""
        cursor.execute(query, (brand,))
        result = []
        for row in cursor:
            result.append(Product(**row))
        cursor.close()
        cnx.close()
        return result

    @staticmethod
    def get_peso(p1_number, p2_number, year):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select count(distinct gds2.Retailer_code) peso
                    from go_daily_sales gds , go_daily_sales gds2 
                    where gds2.Retailer_code = gds.Retailer_code and gds2.Product_number = %s 
                    and gds.Product_number = %s and year (gds2.`Date`) = %s and gds2.`Date` = gds.`Date` """
        cursor.execute(query, (p1_number, p2_number, year))
        result = None
        for row in cursor:
            result = row['peso']
        cursor.close()
        cnx.close()
        return result
