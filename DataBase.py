import MySQLdb


class DataBase(object):


    def init(self,user_name,user_pass):
        self.mydb = MySQLdb.connect(host='localhost', user=user_name, passwd=user_pass, db='clients')
        self.cur = self.mydb.cursor()
        self.mydb.autocommit(True)




    def query(self, query):
        self.cur.execute(query)
        return self.cur.fetchall()

    def  dele(self):
        self.mydb.close()



