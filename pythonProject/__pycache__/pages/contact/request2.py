from utilities.db.db_manager import dbManager as db


def delete_request(req_id):
    query = "DELETE FROM requests WHERE id= '%s';" % req_id


class request2:
    def __init__(self, name, last_name, email, phone, req):
        self.name = name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.request = req
        self.add_to_db()

    def add_to_db(self):
        query = "INSERT INTO requests (name, last_name, phone, email, request) VALUES ('%s' , '%s', '%s' , '%s', '%s')"\
                % (self.name, self.last_name, self.phone, self.email, self.request)
        db.commit(query)
        delete_request(1)

