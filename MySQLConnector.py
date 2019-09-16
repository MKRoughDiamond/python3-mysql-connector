import pymysql
import getpass
import copy
import pickle

class MySQLConnector():
    def __init__(self, host, id_, db, cursor_type=pymysql.cursors.DictCursor):
        self.host = host
        self.id = id_
        self.db = db
        self.history = []
        self.cursor_type = cursor_type


    def get_settings(self):
        return copy.copy((self.host, self.id, self.db, self.cursor_type))


    def set_settings(self, host=None, id_=None, db=None, cursor_type=None):
        if host is not None:
            self.host = host
        if id_ is not None:
            self.id = id_
        if db is not None:
            self.db = db
        if cursor_type is not None:
            self.cursor_type = cursor_type
        self.history = []


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


    def clear_history(self):
        self.history=[]


    def get_history(self):
        return copy.copy(self.history)


    def print_history(self):
        if len(self.history) < 1:
            print("[]")
        else:
            if self.cursor_type == pymysql.cursors.DictCursor:
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


    def export_csv(self, filename=None):
        if len(self.history) < 1:
            print("Nothing to Export")
            return

        if filename is None:
            filename = input("input file name to export (e.g. *.csv) : ")
        with open(filename,'w') as f:
            if type(self.cursor_type) == type(pymysql.cursors.DictCursor):
                string = ""
                for name in self.history[0].keys():
                    try:
                        string = string + str(name) + ','
                    except:
                        string = string + ','
                f.write(string+'\n')

                for item in self.history:
                    string=""
                    for column in item.values():
                        try:
                            string = string + str(column) + ','
                        except:
                            string = string + ','
                    f.write(string+'\n')
            else:
                for item in self.history:
                    string=""
                    for column in item:
                        try:
                            string = string + str(column) + ','
                        except:
                            string = string + ','
                    f.write(string+'\n')


    def export_pickle(self, filename=None):
        if len(self.history) < 1:
            print("Nothing to Export")
            return

        if filename is None:
            filename = input("input file name to export (e.g. *.pickle) : ")
        with open(filename, 'wb') as f:
            pickle.dump(self.history,f)
