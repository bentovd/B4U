from utilities.db.db_manager import dbManager as db


class user:
    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password

    def exist(self):  # check if the user is already exist in DB
        query = "SELECT user_name FROM users WHERE user_name = '%s'; " % self.user_name
        data = db.fetch(query)
        if data:
            return True
        return False

    def add_to_db(self):
        query = "INSERT INTO users (user_name, password) VALUES ('%s' , '%s');" % (self.user_name, self.password)
        db.commit(query)

    def add_item(self, item, request):
        query = "INSERT INTO productincart (user_name, makat, quantity, size, price) VALUES ('%s' ,%s ,%s ,'%s' ,%s);" % (
        self.user_name, item.makat, request.form["number"], request.form["size"], item.price)
        db.commit(query)

    def valid_login(self):  # return 0 if the user dosnt exist, 1 if password match user_name, 2 not match
        user_exist = self.exist()
        if user_exist:
            query = "select user_name from users where user_name = '%s' and password = '%s';" % (
            self.user_name, self.password)
            ans = db.fetch(query)
            if ans:
                return 1
            else:
                return 2
        else:
            return 0

    @staticmethod
    def get_orders(user):
        query = "select m.path, p.user_name, sum(p.quantity) as quantity, p.size, p.price, m.makat from productincart as p " \
                "inner join models as m on  p.makat=m.makat " \
                "where p.user_name= '%s'" \
                "group by p.user_name, m.makat, p.size, m.path, p.price;" % (user)
        orders = db.fetch(query)
        query2 = "select sum(p.price*p.quantity) as total from productincart as p " \
                 "where p.user_name= '%s'" \
                 "group by p.user_name;" % (user)
        total_cart = db.fetch(query2)
        return orders, total_cart

    @staticmethod
    def delete_order(order, user):
        query = "delete from productincart where user_name='%s' and makat=%s and size='%s';" % (user, int(order["makat"]), order["size"])
        db.commit(query)

    @staticmethod
    def delete_cart(user, size, makat):
        query = "delete from productincart where user_name = '%s' and size='%s' and makat=%s;" % (user, size, makat)
        db.commit(query)
