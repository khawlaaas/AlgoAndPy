import string


def analyse_lexique(texte):
    for c in [',', '.', '!', '?']:
        texte = texte.replace(c, " ")

    mots = texte.lower().split()

    frequences = {}
    for mot in mots:
        if mot in frequences:
            frequences[mot] += 1
        else:
            frequences[mot] = 1

    longueurs = [len(m) for m in mots]
    longueur_moyenne = sum(longueurs) / len(longueurs)

    max_freq = max(frequences.values())
    min_freq = min(frequences.values())
    mots_plus = [mot for mot, f in frequences.items() if f == max_freq]
    mots_moins = [mot for mot, f in frequences.items() if f == min_freq]

    palindromes = []
    for mot in mots:
        if len(mot) > 1 and mot == mot[::-1]:
            palindromes.append(mot)

    print("Nombre total de mots :", len(mots))
    print("Longueur moyenne des mots :", round(longueur_moyenne, 2))
    print("Mots les plus utilisés :", mots_plus)
    print("Mots les moins utilisés :", mots_moins)
    print("Palindromes détectés :", palindromes)
    print("\nFréquence des mots :", frequences)


def analyse_grammaticale(texte):
    separateurs = [".", "!", "?"]
    phrases = []
    phrase = ""

    for c in texte:
        phrase += c
        if c in separateurs:
            phrases.append(phrase.strip())
            phrase = ""

    nb_phrases = len(phrases)

    longueurs_phrases = [len(p.split()) for p in phrases]
    longueur_moyenne = sum(longueurs_phrases) / nb_phrases

    ponctuation = {".": 0, "!": 0, "?": 0, ",": 0, ";": 0, ":": 0}
    for c in texte:
        if c in ponctuation:
            ponctuation[c] += 1

    stats_mots = {"noms_propres": 0, "adverbes": 0, "adjectifs": 0, "autres": 0}
    mots = texte.replace(".", "").replace(",", "").split()
    for mot in mots:
        if mot[0].isupper():
            stats_mots["noms_propres"] += 1
        elif mot.endswith("ment"):
            stats_mots["adverbes"] += 1
        elif mot.endswith("e"):
            stats_mots["adjectifs"] += 1
        else:
            stats_mots["autres"] += 1

    print(f"Nombre de phrases : {nb_phrases}")
    print(f"Longueur moyenne des phrases (en mots) : {round(longueur_moyenne, 2)}")
    print(f"Types de ponctuation utilisés : {ponctuation}")
    print(f"Statistiques par type de mot : {stats_mots}")


def rapports(texte):
    for c in [",", ";", ":", "(", ")", "\"", "'"]:
        texte = texte.replace(c, "")

    separateurs = [".", "!", "?"]
    phrases = []
    phrase = ""

    for c in texte:
        phrase += c
        if c in separateurs:
            phrases.append(phrase.strip())
            phrase = ""

    mots = []
    for p in phrases:
        mots += p.lower().replace(".", "").replace("!", "").replace("?", "").split()

    freqs = {}
    for mot in mots:
        freqs[mot] = freqs.get(mot, 0) + 1

    mots_uniques = set(mots)

    top_10 = sorted(freqs.items(), key=lambda x: x[1], reverse=True)[:10]

    longueurs = [len(p.split()) for p in phrases]
    max_len = max(longueurs)
    phrases_longues = [p for p in phrases if len(p.split()) == max_len]

    diversite = (len(mots_uniques) / len(mots)) * 100

    print(f"Top 10 des mots : {top_10}")
    print(f"Phrases les plus longues ({max_len} mots) :")
    for p in phrases_longues:
        print("  -", p)
    print(f"Diversité du vocabulaire : {diversite:.2f}%")


with open("data.txt", "r") as fichier:
    texte = fichier.read()
analyse_grammaticale(texte)
analyse_lexique(texte)
rapports(texte)