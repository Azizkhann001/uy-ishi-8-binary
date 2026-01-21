books = [
    ("O'tkan kunlar", "Roman"),
    ("Mehrobdan chayon", "Roman"),
    ("Shum bola", "Povest"),
    ("Alkimyogar", "Roman"),
    ("Boy va kambag'al", "Hikoya"),
    ("Urush va tinchlik", "Roman"),
    ("Kecha va kunduz", "Roman"),
    ("Yulduzli tunlar", "Povest"),
    ("Qorako'z Majnun", "Hikoya"),
    ("Qalb ko'zi", "Hikoya")
]
guruhlangan={}

for kitob, janr in books:
    if janr not in guruhlangan:
        guruhlangan[janr]=[]
    guruhlangan[janr].append(kitob)
        

print(guruhlangan)
