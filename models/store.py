from db import db


class StoreModel(db.Model):

    __tablename__ = 'stores'

    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.String(80))

    items = db.relationship('ItemModel', lazy='dynamic')
    # the lazy dynamic, is everytime it call go to the table, rather than directly taking the massive ammount and creating object

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()
# the above equation select * from items where name = name Limit 1, also converts to an object model object

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
