import secrets
import json
import os
from const import(DATA,TAILLE,CHOIX_INTERFACE,FILE_TXT,FILE_TXTR)
import time
import colorsys
from tkinter import N
import turtle


def author_project():
    remove_screen()
    print("application made by mohamedndaw697@gmail.com".center(80," "))
    time.sleep(2)
    
    remove_screen()
    time.sleep(2)
    print("application made by mohamedndaw697@gmail.com".center(80," "))
    time.sleep(2)
    remove_screen()
    
    time.sleep(2)
    print("application made by mohamedndaw697@gmail.com".center(80," "))
    time.sleep(2)
    remove_screen()
    # time.sleep(2)
    
    
def remove_screen():
    if os.name =='posix':
        os.system('clear')
    else:
        os.system('cls')
        

def generate_id():
    # CETTE FONCTION PERMET DE GENERER DES ID
     id=secrets.token_hex(1)
     
    
    
    



def load_json_file():
    remove_screen()
    with open(DATA) as file:
        my_data=json.load(file)
        print(my_data)
 
def motif(TAILLE:int,motif:str):
    print(motif * TAILLE)  



       
def interface()->None:
    remove_screen()
    time.sleep(2)
    print("1 ".replace(" ","---".center(TAILLE,"-")),"Afficher les personnes\n")
    print("2 ".replace(" ","---".center(TAILLE,"-")),"Ajouter une personne\n")
    print("3 ".replace(" ","---".center(TAILLE,"-")),"Modifier une personne\n")
    print("4 ".replace(" ","---".center(TAILLE,"-")),"AUTRES\n")
    print("5 ".replace(" ","---".center(TAILLE,"-")),"Quitter\n")
    
    

def request(min,max:int,msg:str):
    entier=input(msg)
    while (not entier.isdigit() or int(entier) < min) or (int(entier) > max):
        entier=input(msg)
        # return int(entier)
        break
    i=""
    i=input("choisir de 1 à 5:\t")
    if i=="1":
        time.sleep(3)
        load_file_txt()
        back_input()
        request(1,3,"START ->\t")
        
    elif i=="2":
        time.sleep(3)
        add_data()
        back_input()
        request(1,3,"START ->\t")
    elif i=="4":
        time.sleep(3)

        t = turtle.Turtle()
        s = turtle.Screen()
        s.bgcolor('black')
        t.speed(0)
        n=36
        h = 0
        for i in range (460):
            c = colorsys.hsv_to_rgb(h,1,0.8)
            h+=1/n
            t.color(c)
            t.left(145)
            for j in range (5):
                t.forward(300)
                t.left(150)
    else:
        print('ce que tu as saisi n\'existe pas !!\n Appuie sur ctrl + c puis reprendre')
        while True:
            pass
        
    # else:
            # cas ou la saisie est correcte je dois appeler la fonction  response ici
        # return int(entier)

        
        
# def request2():

 
# request2()
    
        
        
    

def response(min,median,max:int)->None:
        # request(1,3,"choisir de 1 à 3 :\t") 
        monTableau=CHOIX_INTERFACE
        print(min)
        print(median)
        print(max)
        
        print(type(monTableau))
        
        
# response(min=CHOIX_INTERFACE[0],median=CHOIX_INTERFACE[1],max=CHOIX_INTERFACE[2])


def load_file_txt():
    remove_screen()
    with open(FILE_TXT) as file:
        # data= file.read().splitlines()[1:]
        for line in file:
            # remove_screen()
            row=(line.split(";"))
            # newRow= row[0]
            # newRow= row[1]
            # newRow= row[2]
            print(" ".join(row).center(80," "))
            
            

         
def back_input():
    back=input("\nretour à l'interface ->\t0\t")
    if back =="0":
        interface()
    else:
        print('tu as bloquer le programme ^_^')
        while True:
            pass
        
        
def add_data():
    remove_screen()
    id=secrets.token_hex(1)
    nom=input("entrer le nom :\t")
    if not nom.isalpha() or len(nom)<= 2:
        print("je n'accepte pas les noms avec chiffres ou les noms courts !")
    else:
        prenom=input("entrer le prenom :\t")
        if not prenom.isalpha() or len(prenom)<= 2:
                print("je n'accepte pas les prenoms avec chiffres ou les prenoms courts !")
        else:
            age=input("entrer l'age :\t")
            if not age.isdigit():
                print('l\'age ne peut contenir des chaînes !')
            if int(age) >= 100 or int(age) <= 0:
                print('entrer un age valide !')
            else:
                with open("user.txt","a") as f:
                    data= f.write("{} {} {} {}\n".format(id,nom,prenom,age))  
                    print("personne ajouter avec succès !")
                    return data
        
    



    
        
