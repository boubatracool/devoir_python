def transform(chain):
    # votre programme ici
    chain1 = chain[0]
    chain2 = chain[1]

    list1 = chain1.split(",")
    list2 = chain2.split(",")

    resulat = set(list1).intersection(list2)
    resulat = sorted(resulat, key=lambda x: int(x), reverse=True)
    
    if len(resulat) > 0:
        return ",".join(resulat) + ":Boubacar_Traoré_Master1_IA"
    else:
        return "None"


# vous ne modifierez rien après cette ligne
if __name__ == "__main__":
    arr1 = ["1,3,4,7,13", "1,2,4,13,15"]
    out = transform(arr1)
    print(out)  # doit afficher ---> 31,4,1:nom_prenom_classe

    arr3 = ["9, 3, 5, 7, 14", "10, 2, 6, 16, 15"]
    out = transform(arr3)
    print(out)  # doit afficher ---> None
