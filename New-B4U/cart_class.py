from utilities.db.db_manager import dbManager as db

class cart:

    def _init_(self, user_id, products):
        self.user_id = user_id
        self.products = None

    def clear(self):
        self.products = None

    def remove_item (self, item):
        query = "DELETE FROM productInCart WHERE cart='self' and product='item' "
        db.commit(query)

    def add_item (self, item, request):
        query = "INSERT INTO productInCart (user_id, makat, quantity, size, price) VALUES ('%s' , '%s', '%s', '%s', '%s');" % (self.user_id, item.makat, request.adding['quantity'], request.adding['size'], item.price)
        db.commit(query)

    def cart_total_price(self):
        query = "SELECT sum(price) FROM productInCart WHERE cart = '%s'; " % self
        totalPrice = db.fetch(query)
