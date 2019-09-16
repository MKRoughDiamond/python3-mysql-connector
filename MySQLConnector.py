import pymysql
import getpass
import copy

class MySQLConnector():
    def __init__(self, host, id_, db, cursor_type=pymysql.cursors.DictCursor):
        self.host = host
        self.id = id_
        self.db = db
        self.history = []
        self.cursor_type = cursor_type

    def get_settings(self):
        return (self.host, self.id, self.db)

    def query(self):
        try:
            with pymysql.connect( host = self.host
                                , user = self.id
                                , passwd = getpass.getpass()
                                , db = self.db
                                , cursorclass = self.cursor_type) as cur:
                while True:
                    try:
                        string = input("MySQL(exit : 'exit') > ")
                        if string =='exit':
                            print('Exit without querying. History not changed')
                            break
                        else:
                            l = []
                            cur.execute(string)
                            self.history = cur.fetchall()
                            self.print_history()
                            return
                    except:
                        print('Query error occured')
                        continue
        except:
            print('Connection error occured')

    def get_history(self):
        return copy.copy(self.history)

    def print_history(self):
        if len(self.history) < 1:
            print("[]")
        else:
            if type(self.cursor_type) == type(pymysql.cursors.DictCursor):
                for name in self.history[0].keys():
                    print(name,end='\t')
                print()

                for item in self.history:
                    for column in item.values():
                        print(column,end='\t')
                    print()
                print("got {} element(s)".format(len(self.history)))
            else:
                print(self.history)
