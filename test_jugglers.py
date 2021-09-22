from peewee import *
#import sqlite3
import unittest
from unittest import TestCase
import jugglers
from jugglers import Juggler
   

# from http://docs.peewee-orm.com/en/latest/peewee/database.html
MODELS = [Juggler]
test_db = SqliteDatabase('test_jugglers.sqlite')



class TestJugglersDB(Model):


    def setUP(self):
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)
        test_db.connect()
        test_db.create_tables(MODELS)
        
    def compare_database_to_whats_entered(self, entered):
        test_db = SqliteDatabase('test_jugglers.sqlite')
        test_db.connect()
        cursor = test_db.execute_sql('SELECT * FROM Juggler')
        x = 0
        for row in cursor.fetchall():
            self.assertEqual(row[x], entered[x])
            x += 1

    def tearDown(self):
        test_db.drop_tables(MODELS)
        test_db.close()



    

   

   


if __name__ == '__main__':
    unittest.main()