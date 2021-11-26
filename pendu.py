import random
import corrige_pendu

# Question 0
# Compléter dans les chaînes ci-dessous, sans enlever les guillemets:
NOM = "VOTRE NOM"
PRENOM = "VOTRE PRENOM"
EMAIL = "VOTRE EMAIL"


# Question 1
def charge_mots(chemin):
    # REMPLACER LA LIGNE CI-DESSOUS PAR VOTRE CODE

    # ouvrir le fichier
    file = open(chemin, 'r')  # open the file
    # read  , readlines
    lines = file.read().splitlines()  # on retourne les lignes du tableau sans les \n
    return lines, len(max(lines, key=len))


# Question 2
def test_charge_mots():
    # À COMPLÉTER AVEC VOS TESTS
    mots, lmax = charge_mots("mots.txt")

    assert (lmax == 25)  # verifier si la taille est bien 25
    assert (len(mots) == 59705)
    assert mots[0] == 'abaissa'
    assert mots[59704] == 'zyeuter'
    return


# Question 3
def mots_par_longueur(tab_mots, lmax):
    # REMPLACER LA LIGNE CI-DESSOUS PAR VOTRE CODE
    t = [[]]
    for i in range(lmax):
        iarray = []  # contient un element à un index bien particulier
        for j in range(len(tab_mots)):
            if len(tab_mots[j]) == (i + 1):
                iarray.append(tab_mots[j])
        t.append(iarray)

    return t


# Question 4
def test_mots_par_longeur():
    # À COMPLÉTER AVEC VOS TESTS
    mots = ['a', 'bonbon', 'code', 'dos', 'etre']
    lmax = 6
    lmots = mots_par_longueur(mots, lmax)
    assert lmots[0] == []
    assert lmots[1] == ['a']
    assert lmots[2] == []
    assert lmots[3] == ['dos']
    assert lmots[4] == ['code', 'etre']
    assert lmots[5] == []
    assert lmots[6] == ['bonbon']
    return


# Question 5
def choix_mot(tab_mots_long, l):
    # REMPLACER LA LIGNE CI-DESSOUS PAR VOTRE CODE
    mot_choisis = ""
    for i in range(len(tab_mots_long)):
        if i == l:
            index = random.randint(0, len(tab_mots_long[i]) - 1)
            mot_choisis = tab_mots_long[i][index]
    return mot_choisis


# Question 6
def test_choix_mot():
    # NE PAS MODIFIER LES 2 LIGNES SUIVANTES
    tab_mots, lmax = corrige_pendu.charge_mots("mots.txt")
    tab_mots_long = corrige_pendu.mots_par_longueur(tab_mots, lmax)
    # À COMPLÉTER CI-DESSOUS AVEC VOS TESTS, VOUS POUVEZ UTILISER
    # tab_mots_long POUR VOS TESTS
    mot_choisis_un = choix_mot(tab_mots_long, 4)
    assert mot_choisis_un != 'Dbz'

    return


# Question 7
def init_probleme(mot):
    # REMPLACER LA LIGNE CI-DESSOUS PAR VOTRE CODE
    # si par exemple l'user tape le code
    # si la lettre qu;il a taper est bien dans le mot
    # si oui alors on retourne un tableau la lettre et un boolean True/False
    problemes = []
    for pos, char in enumerate(mot):
        openParenthesis = "('"
        closisParenthesis = "')"
        character = openParenthesis + char + closisParenthesis
        separator = ","
        estTrouvé = str(False)
        probleme = character + separator + estTrouvé
        problemes.append(probleme.strip('"'))
    return problemes


# Question 8
def test_init_probleme():
    # À COMPLÉTER CI-DESSOUS AVEC VOS TESTS
    mot_choisit = "Avion"  # on a le mot que nous avons choisit pour faire le test
    probleme = init_probleme(mot_choisit)  # on le casse afin de pouvoir recuperer un tableau de probleme formaté
    for i in range(len(probleme)):  # je fais une boucle sur le probleme afin de recuperer les éléments
        mot_casse = probleme[i].split(sep=",", maxsplit=2)
        index_lettre_mot_casse = mot_casse[0].find(mot_choisit[i])
        if index_lettre_mot_casse != -1:
            lettre = mot_casse[0][index_lettre_mot_casse]
            assert lettre == mot_choisit[i]
            assert mot_casse[1] == str(False)
    return


# Question 9
def num_inconnues(probleme):
    # REMPLACER LA LIGNE CI-DESSOUS PAR VOTRE CODE
    count = 0
    for i in range(len(probleme)):  # je fais une boucle sur le probleme afin de recuperer les éléments
        mot_casse = probleme[i].split(sep=",", maxsplit=2)
        if mot_casse[1] == str(False):
            count = count + 1

    return count


# Question 10
def test_num_inconnues():
    # À COMPLÉTER CI-DESSOUS AVEC VOS TESTS
    # premier test
    problemes_trouves = ["('A'),True", "('B'),True", "('A'),True", "('L'),True", "('O'),True"]
    inconnues_trouve = num_inconnues(problemes_trouves)
    assert inconnues_trouve == 0
    # second test inconnues > connues
    mot_choisit_deux = ["('A'),True", "('B'),True", "('A'),False", "('L'),True", "('O'),False"]
    inconnues_trouve_deux = num_inconnues(mot_choisit_deux)
    assert inconnues_trouve_deux == 2
    # troisieme test avec que rien des inconnues
    mot_choisit_trois = init_probleme('Hillary')
    inconnues_trouve_trois = num_inconnues(mot_choisit_trois)
    assert inconnues_trouve_trois == 7
    return


# Question 11
def joue(probleme, lettre):
    # REMPLACER LA LIGNE CI-DESSOUS PAR VOTRE CODE
    problemes = []
    for i in range(len(probleme)):  # je fais une boucle sur le probleme afin de recuperer les éléments
        chaines_separe = probleme[i].split(sep=',')
        if lettre in chaines_separe[0]:
            chaines_separe[1] = str(True)
        element = chaines_separe[0] + ',' + chaines_separe[1]
        problemes.append(element)
    return problemes


# Question 12
def test_joue():
    # À COMPLÉTER CI-DESSOUS AVEC VOS TESTS
    mot_a_verifier = "Avion"
    probleme = init_probleme(mot_a_verifier)
    lettre_verifier_un = "A"
    # verification si le premier test marche bien
    test_probleme_1 = joue(probleme, lettre_verifier_un)
    print(test_probleme_1)
    num_inconnues_test_1 = num_inconnues(test_probleme_1)
    assert num_inconnues_test_1 == len(mot_a_verifier) - 1

    # deuxieme test avec que des valeurs false
    lettre_verifier_deux = "Z"
    test_probleme_2 = joue(probleme, lettre_verifier_deux)
    num_inconnues_test_1 = num_inconnues(test_probleme_2)
    assert num_inconnues_test_1 == len(mot_a_verifier)

    # troisieme  test avec que des valeurs un deux valeurs trouvé

    lettre_verifier_trois = "V"
    mot_a_verifie_trois = "AVV"
    test_probleme_3 = joue(init_probleme(mot_a_verifie_trois), lettre_verifier_trois)
    num_inconnues_test_1 = num_inconnues(test_probleme_3)
    assert num_inconnues_test_1 == len(mot_a_verifie_trois) - 2
    return


# Question 13
def affiche_probleme(tab):
    # REMPLACER LA LIGNE CI-DESSOUS PAR VOTRE CODE
    resultat = ""
    for i in range(len(tab)):
        chaines_separe = tab[i].split(sep=',')
        if chaines_separe[1] == str(True):
            resultat += chaines_separe[0][2]
        else:
            resultat += '.'

    return resultat


PENDU = (
    '  ___ ',
    ' |   |',
    ' o   |',
    '/|\  |',
    '/ \  |',
    '     |')


# Question 14
def affiche_pendu(n):
    # REMPLACER LA LIGNE CI-DESSOUS PAR VOTRE CODE
    k = 0
    if n <= 15:
        for i in range(len(PENDU)):
            for c in PENDU[i]:
                if c == ' ':
                    print(' ', end='')
                elif k < n:
                    print(c, end='')
                    k = k + 1
                else:
                    print(' ', end='')
            print()


def partie(mot):
    print(mot)
    # transformer le mot en probleme
    probleme = init_probleme(mot)
    # chercher le nombre d'inconnues
    inconnues_initial = num_inconnues(probleme)
    trait_pendu = 0
    asTrouve = False
    while inconnues_initial != 0 and trait_pendu != 15:
        # demander une lettre a l'user
        print(affiche_probleme(probleme))
        lettre = input("Veuillez entrer une lettre: ")
        # repeter l'operation tant que le joueur ne rentre pas une lettre valide
        while lettre.isnumeric():
            lettre = input("Lettre invalide ! Veuillez entrer une lettre: ")
        # faire un mouvement dans le jeu
        probleme = joue(probleme, lettre)
        actuel_nombre_inconnue = num_inconnues(probleme)
        if inconnues_initial - actuel_nombre_inconnue == 0:
            trait_pendu += 1
            affiche_pendu(trait_pendu)  # afficher le pendu
        else:
            inconnues_initial = actuel_nombre_inconnue

        if num_inconnues(probleme) == 0:
            asTrouve = True
            break
    if asTrouve:
        print("Félicitations vous avez gagné")
    else:
        print("Désolé vous avez perdu ! Le mot choisit était ", end=mot)
        print()

        #### NE PAS MODIFIER LE CODE CI-DESSOUS


def jeu():
    mots, lmax = charge_mots("mots.txt")
    # appel de la fonction de test

    lmots = mots_par_longueur(mots, lmax)
    while True:
        s = input("Saisir une longueur de mot ou q pour quitter: ")
        if s == 'q':
            print("Au revoir.")
            return
        try:
            l = int(s)
            if l > lmax or l <= 0:
                print("Longueur invalide")
                continue
            mot = choix_mot(lmots, l)
            partie(mot)
        except ValueError:
            print("Saisie invalide")


jeu()
