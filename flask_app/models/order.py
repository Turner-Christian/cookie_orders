from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Order:
    DB = 'cookies_schema'
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.cookie_type = data['cookie_type']
        self.number_of_boxes = data['number_of_boxes']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls,data):
        query = 'INSERT INTO cookie_orders(name,cookie_type,number_of_boxes) VALUES(%(name)s,%(cookie_type)s,%(number_of_boxes)s)'
        return connectToMySQL(cls.DB).query_db(query,data)
    
    @classmethod
    def show_all(cls):
        query = 'SELECT * FROM cookie_orders'
        result = connectToMySQL(cls.DB).query_db(query)
        all_orders = []
        for order in result:
            all_orders.append(cls(order))
        return all_orders

    @classmethod
    def show_one(cls,id):
        query = 'SELECT * FROM cookie_orders WHERE id=%(id)s'
        result = connectToMySQL(cls.DB).query_db(query,{'id' : id})
        return result[0]
    
    @classmethod
    def update_cookie(cls,data):
        query = """
        UPDATE cookie_orders
        SET
        name = %(name)s,
        cookie_type = %(cookie_type)s,
        number_of_boxes = %(number_of_boxes)s,
        updated_at = NOW()
        WHERE id = %(id)s;
        """
        result = connectToMySQL(cls.DB).query_db(query,data)
        if result:
            return result
        else:
            return None

    @staticmethod
    def vald_order(input):
        is_valid = True
        if not input['name']:
            flash('Name is required')
            is_valid = False
        if len(input['name']) < 2:
            flash('Name must be at least 2 characters')
            is_valid = False
        if not input['cookie_type']:
            flash('Cookie Type is required')
            is_valid = False
        if len(input['cookie_type']) < 2:
            flash('Cookie Value must be at least 2 characters')
            is_valid = False
        if not input['number_of_boxes']:
            flash('Number of Boxes is required')
            is_valid = False
        if input['number_of_boxes'] < '1':
            flash('Number of Boxes must be at least 1')
            is_valid = False
        return is_valid