def conversion_caractere_en_int(caractere_chiffre):

    if (caractere_chiffre=='I'):
        return 1
    elif (caractere_chiffre=='V'):
        return 5
    elif (caractere_chiffre=='X'):
        return 10
    elif (caractere_chiffre == 'L'):
        return 50
    elif (caractere_chiffre == 'C'):
        return 100
    elif (caractere_chiffre == 'D'):
        return 500
    elif (caractere_chiffre == 'M'):
        return 1000
    else:
        return 0

def romain_en_nombre_int(chaine_de_caracRomain):

    compteur = 0
    res = 0
    
    while (compteur < len(chaine_de_caracRomain)):
        if (compteur+1 != len(chaine_de_caracRomain)):
            if(conversion_caractere_en_int(chaine_de_caracRomain[compteur]) < conversion_caractere_en_int(chaine_de_caracRomain[compteur+1])):
                res = res - conversion_caractere_en_int(chaine_de_caracRomain[compteur])
                compteur += 1 
            else :
                res = res + conversion_caractere_en_int(chaine_de_caracRomain[compteur])
                compteur += 1
        else :
            res = res + conversion_caractere_en_int(chaine_de_caracRomain[compteur])
            compteur += 1
    return res


def int_en_nombre_romain(nombre_int):

    tab_unit = [" ","I","II","III","IV","V","VI","VII","VIII","IX"]
    tab_diz = [" ","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
    tab_cent = [" ","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
    tab_mill = [" ","M","MM","MMM"]
    tab_res = []
    compteur = 0
    quotient = nombre_int
    nbr_elem_tab_res = 0    

    if nombre_int > 3000 or nombre_int < 0:  #d'après la consigne on doit transformer tout nombre compris entre 0 et 3000
        return "Le nombre à transformer ne doit être compris entre 0 et 3000"

    while compteur < 4 : #Boucle qui permet d'extraire unité, dizaine puis centaine. 
        reste = nombre_int % 10 
        quotient = quotient // 10
        nombre_int = quotient
        tab_res.append(reste)
        compteur += 1

    tab_res[0] = tab_unit[tab_res[0]]
    tab_res[1] = tab_diz[tab_res[1]]
    tab_res[2] = tab_cent[tab_res[2]]
    tab_res[3] = tab_mill[tab_res[3]]

    while nbr_elem_tab_res < len(tab_res):   #Boucle qui permet de supprimer les "0" donc les " "  EX : 103 = C III --> CIII
        if tab_res[nbr_elem_tab_res] == " ":
            tab_res.pop(nbr_elem_tab_res)
        else :
            nbr_elem_tab_res = nbr_elem_tab_res + 1

    tab_res.reverse()    
    tab_res = ''.join(tab_res)  #Transformation de la liste "tab_res" en chaine de caractère pour faciliter le print

    return tab_res


    
def calculatrice (operateur, chaine_de_caracRomain_1 , chaine_de_caracRomain_2):

    res = 0
    nb_romain_1 = romain_en_nombre_int(chaine_de_caracRomain_1)
    nb_romain_2 = romain_en_nombre_int(chaine_de_caracRomain_2)

    if (operateur == '+'):
        res = nb_romain_1 + nb_romain_2
    elif (operateur == '-'):
        res = nb_romain_1 - nb_romain_2
    elif (operateur == '*'):
        res = nb_romain_1 * nb_romain_2
        
    elif (operateur == '/'):
        res = nb_romain_1 / nb_romain_2
    #res = int_en_nombre_romain(res)      #Possibilité d'enlevé le premier '#' pour obtenir le résultat en chiffre romain
    
    return res