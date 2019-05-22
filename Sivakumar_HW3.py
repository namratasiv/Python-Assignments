# Namrata Sivakumar
# 1001508168

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 15:04:09 2019

@author: namratasivakumar
"""
import sqlite3 


def view():
    
    conn = sqlite3.connect("players_Data.db") 

 
    query = '''SELECT name, wins, losses, ties
               FROM Player ORDER BY name '''
 
    cursor = conn.execute(query)

#print(cursor.fetchall())
    print("{:15}{:>3} {:>15} {:>15} {:>15} ".format("Name","Wins", "Losses","Ties","Games"))
    print("--------------------------------------------------------------------------------")
       
    for row in cursor:
        print("{:15}{:>3} {:>15} {:>15} {:>15}".format(row[0],row[1], row[2], row[3],(row[1]+row[2]+row[3] )))
    
    print()
        

    conn.close()

def add():
    conn = sqlite3.connect("players_Data.db") 
    conn.execute('''
        CREATE TABLE if not exists Player
        (       
          
          name          TEXT,
          wins        INT,
          losses        INT,
          ties        INT
          
        )         
        ''')
    
    name = input("Name: ")
    wins = int(input("Wins: "))
    losses = int(input("Losses: "))
    ties = int(input("Ties: "))
    

    sql = '''INSERT INTO Player (name, wins, losses, ties) 
             VALUES (?, ?, ?, ?)'''
    conn.execute(sql, (name, wins, losses, ties))
    
                    
    conn.commit()
    
    conn.close()
    
    print(name," was inserted to the database! ")
    print()

def ddel():
    conn = sqlite3.connect("players_Data.db") 
    
    
    name = input("Name: ")
    
    

    sql = '''DELETE FROM Player WHERE name = ? '''
    conn.execute(sql, (name,))
    
                    
    conn.commit()
    
    conn.close()
    
    print(name," was deleted from the database! ")
    print()

def upd():
    conn = sqlite3.connect("players_Data.db") 
    
    name = input("Name: ")
    wins = int(input("Wins: "))
    losses = int(input("Losses: "))
    ties = int(input("Ties: "))
    
    

    sql = '''UPDATE Player SET wins = ?, losses = ?, ties = ? WHERE name = ? '''
    conn.execute(sql, (wins, losses, ties, name))
    
                    
    conn.commit()
    
    conn.close()
    
    print(name," was UPDATED! ")
    print()

    
    
    
    
    
    

def main():
    
    choice =''
    
    while choice!='exit':
        
        
        print("Player Manager\n")
        print("COMMAND MENU")
        print("view - View players")
        print("add - Add a player")
        print("update - Update a player")
        print("del - Delete a player")
        print("exit - Exit Program\n")
        choice = input("Command: ")
        
        if choice=='view':
            view()
        elif choice=='add':
            add()
        elif choice=='del':
            ddel()
        elif choice == 'update':
            upd()
        else:
            print("Bye!")

main()
    
    


