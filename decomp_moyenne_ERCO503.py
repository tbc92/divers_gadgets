# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 18:21:09 2017

@author: tbc92

Correspond au sujet posté ici : 
    https://www.developpez.net/forums/d1755847/general-developpement/algorithme-mathematiques/mathematiques/distributions-meme-moyenne/

On a N interviewés, qui peuvent chacun mettre une note entre 0 et MX , combien 
y a-t-il de combinaisons qui permettent d'arriver au total T
 Si les réponses sont 1.0.0 ou 0.0.1, c'est pareil, ça compte pour 1.
 
 Il y a en fait une formule de récurrence expliquée sur le forum 
 (message du 28 octobre 14heures) qui permet de trouver rapidement le résultat.
 
"""

def fct(N, MX,T , tttt ) :
    """
     N = Nbre d'interviews, 
     MX = les réponses sont des nombres entre 0 et MX,
     T = La somme des N réponses.
    
     tttt est un dictionnaire qui permet de réutiliser un résultat intermédiaire précédemment calculé.
     Sans cette astuce, les temps de traitements sont énormes.
     Avec cette astuce, c'est instantané.
    """
    
    s = str(N)+ ";" + str(MX) + ";" + str(T)
    sch = tttt.get( s, "0")
    if sch != "0" :
        return  int ( sch ) 
    
    if N*MX<T or MX<0 or T<0 or N<1 :
        return 0
    
    if N == 1:
        if MX >= T :
            return 1
        else:
            return 0
    i = fct(N-1,MX,T, tttt) + fct (N, MX-1,T-N, tttt)
    tttt[s] = str(i)
    return i ;
 
def main() :
    tttt = {}  #  Dictionnaire
    ss=0
    for i in range(415) :
        j = fct( 46,9,i, tttt)  # 21976554
        print ( str(i) + "  >>>  " + str(j) )
        ss = ss + j
    print (ss)

if __name__ == '__main__':
    main()