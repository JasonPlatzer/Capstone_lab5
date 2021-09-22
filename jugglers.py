from peewee import *

db = SqliteDatabase('jugglers.sqlite')


class Juggler(Model):
        name = CharField()
        country = CharField()
        catches = IntegerField()

        class Meta:
            database = db

        def __str__(self):
            return f'{self.name}, {self.country}, {self.catches}'

def add_juggler():
    try:       
        juggler_name = str(input('Enter a juggler name '))
        juggler_country = str(input('Enter their country '))
        juggler_catches = int(input('Enter their number of catches '))
        new_juggler = Juggler(name=juggler_name, country=juggler_country, catches=juggler_catches)
        new_juggler.save()
    except ValueError as e:
        print('Can\'t add juggler')
        
    
                  

def search_for_juggler():
    found = True
    try:
        name = input('Enter jugglers name to search for ')
        juggler = Juggler.select().where(Juggler.name == name)
        print(list(juggler))    
    except ValueError as e:
        print('Can\'t find juggler')
   
        
    

def change_catches(): 
        try:
            name = input('Enter jugglers name ')
            new_catches = int(input('Enter their new number of catches '))
            Juggler.update(catches=new_catches).where(Juggler.name == name).execute()             
        except  ValueError as e:
            print('You must enter a number')
            
def delete_juggler():
    name = input('Enter juggler to delete ')
    try:
        Juggler.delete().where(Juggler.name == name).execute()
    except ValueError as e:
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
