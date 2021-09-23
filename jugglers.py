from enum import unique
from peewee import *

db = SqliteDatabase('jugglers.sqlite')

class JugglerError():
    pass
class Juggler(Model):
        name = CharField()
        country = CharField()
        catches = IntegerField()

        class Meta:
            database = db

        def __str__(self):
            return f'{self.name}, {self.country}, {self.catches}'

def add_juggler():
          
        juggler_name = input('Enter a juggler name ')
        juggler_country = input('Enter their country ')
        #from https://stackoverflow.com/questions/62848332/preventing-a-user-from-entering-a-string-in-python-3
        juggler_catches = input('Enter their number of catches ')
        # checks if input is a number
        if juggler_catches.isnumeric():
            # if all info is entered this adds a new juggler to the database
            new_juggler = Juggler(name=juggler_name, country=juggler_country, catches=juggler_catches)
            new_juggler.save()
        else:
            print('you must enter a number')
   
        
        
    
                  

def search_for_juggler():
        name = input('Enter jugglers name to search for ')
        # looks for a juggler in the database
        juggler = Juggler.select().where(Juggler.name == name)
        if juggler:
            print(list(juggler))
        else:
            print('can\'t find juggler')    
    
   
        
    

def change_catches(): 
        
            name = input('Enter jugglers name ')
            
            new_catches = input('Enter their new number of catches ')
            if new_catches.isnumeric():
            #updates database and sets new catches according to name entered               
                Juggler.update(catches=new_catches).where(Juggler.name == name).execute()             
            else:
                print('You must enter a number')
            
def delete_juggler():
    name = input('Enter juggler to delete ')
    # looks for a juggler in database
    find_juggler = Juggler.select().where(Juggler.name == name)
    if find_juggler:
        # deletes juggler by name
        Juggler.delete().where(Juggler.name == name).execute()
    else:
        print('Can\'t find juggler')


def main():
    
    db.connect()
    db.create_tables([Juggler])


    ask_user = True
    while ask_user:
        question_num = int(input('Pick an option \n1. add juggler \n2. search for juggler \n3. edit catches for a juggler \n4. delete juggler \n5. exit\n'))
        if question_num == 1:
            add_juggler()
           
        if question_num == 2:
            search_for_juggler() 
        if question_num == 3:
            change_catches()
              
        if question_num == 4:
            delete_juggler()
            
        if question_num == 5:
            ask_user = False
main()   
