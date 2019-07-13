import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.items import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'price',
        type=float,
        required=True,
        help="This field cannot be left blank"
    )

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {"message": "Item not found"}, 400

    @jwt_required
    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message': f"An item with name '{name}' already exist"}, 400
        data = Item.parser.parse_args()
        item = ItemModel(name, data['price'])
        try:
            item.insert()
        except:
            return {'message': f"An error occured while inserting item"}, 500

        return item.json(), 201

    @jwt_required()
    def delete(self, name):
        if ItemModel.find_by_name(name) is None:
            return {'message': f"The item doesn't exist at all, better check what you are deleting"}, 400
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "DELETE FROM items WHERE name=?"
        cursor.execute(query, (name,))

        connection.commit()
        connection.close()

        return {'message': f"Item deleted"}

    @jwt_required
    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
        updated_item = ItemModel(name, data['price'])

        if item is None:
            try:
                updated_item.insert()
            except:
                return{'message': f"An error occured while inserting the item"}, 500
        else:
            try:
                updated_item.update()
            except:
                return{'message': "An error occured while updating"}

        return updated_item.json()



class ItemList(Resource):

    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items"
        result = cursor.execute(query)
        itemlist = []
        for row in result:
            itemlist.append({'name': row[0], 'price': row[1]})

        connection.close()
        return {'items': itemlist}
