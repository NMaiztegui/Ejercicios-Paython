def hiriak_ordenatzen(hiriak):
    # Hiri populatuenak biltzeko zerrenda bat sortzen dugu
    gehiagokoen_zerrenda = []

    # Hiri bakoitza iteratzen dugu
    for hiri, populazioa in hiriak.items():
        if populazioa > 200000:
            gehiagokoen_zerrenda.append(hiri)  # Populazio handiagoak zerrendan sartzen ditugu
    
    # Zerrenda alfabetikoki ordenatzen dugu
    gehiagokoen_zerrenda.sort()

    # Emaitza inprimatzen dugu
    print(gehiagokoen_zerrenda)


# Hiriak definitzen ditugu
gure_hiriak = {
    "Bilbo": 200800,
    "Donostia": 100000,
    "Iruñea": 203000
}

# Funtzioa exekutatzen dugu
hiriak_ordenatzen(gure_hiriak)
