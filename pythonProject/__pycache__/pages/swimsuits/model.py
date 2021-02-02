from utilities.db.db_manager import dbManager as db
from pages.register.user import user

def sett(value, default):
    if value == '' or value is None:
        return default
    else:
        return value


class model:

    def __init__(self, category, color='%', max_price=100000, min_price=0, size='makat'):
        self.category = category
        self.size = size
        self.color = color
        self.max_price = sett(max_price, 100000)
        self.min_price = sett(min_price, 0)
        self.models_selected = self.fetch_models()

    def fetch_models(self):  # return DF with all the models in a specific category
        query = "SELECT makat, path from models where category like '%s' and color like '%s' and price>='%s' and price<='%s' " \
                "and %s >0;" % (self.category, self.color, self.min_price, self.max_price, self.size)
        return db.fetch(query)

    @staticmethod
    def update_models_values(orders, user_name):
        counter_misses = 0
        for order in orders:
            query = "select %s as size_amount from models where makat= %s ;" % (order.size, order.makat)
            ans = db.fetch(query)
            if ans[0].size_amount-order.quantity >= 0:
                query = "update models set %s=(%s- %s) where makat = %s ;" % (order.size, order.size, order.quantity, order.makat)
                db.commit(query)
                user.delete_cart(user_name, order.size, order.makat )
            else:
                counter_misses = counter_misses +1
        return counter_misses



    @staticmethod
    def featch_model(makat):
        query = "SELECT * from models where makat = %s;" % makat
        selected_model = db.fetch(query)
        return selected_model




