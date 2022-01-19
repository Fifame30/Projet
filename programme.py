# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 13:59:38 2022

@author: aissa
"""
def readfile(fichier):
    try:
        #with open("fichier_a_traiter.txt", encoding="utf8") as fh:
        with open(fichier, encoding="utf8") as fh:
            return fh.read().splitlines()
    except:
        return None
    
def writefile(fichier,contenu):
     with open(fichier,"w") as f:
         for line in contenu:
             f.write(line+"\n")
var=readfile("fichier_a_traiter.txt")
csvlines=[]
for line in var:
    if line.startswith('\t')==False:
        data=[" "]*5
        lsplit=line.split(" ")
        data[0]=lsplit[0]
        for index,word in enumerate(lsplit):
            if word=="IP":
                data[1]=word
            if word==">":
                data[2]=lsplit[index-1]
                data[3]=lsplit[index+1]
            if word=="HTTP":
                data[4]=word
        csvline=";".join(data)
        csvlines.append(csvline)
        print(csvline)
writefile("resultat.csv",csvlines)

