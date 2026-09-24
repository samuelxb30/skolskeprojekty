ovocie = ["marhula", "jablko"]
zelenina = ["petrzlen", "mrkva"]
sladkosti = ["cukor", "cokolada"]



polozkyaceny = {
  "jablko": (1, 100),
  "marhula": (1.5, 60),
  "banan": (1.5, 20),
  "petrzlen": (2, 35),
  "cukor": (2.3, 5),
  "mrkva": (2, 35),
  "cokolada": (3, 20),
  "rohlik": (0.10, 300)
}

kosik = []

print("Dobry den, nech sa paci mozte si vybrat\n")
for polozka, (cena, mnozstvo) in polozkyaceny.items():
  print(f"{polozka} - {cena}€ - {mnozstvo} ostáva")

while True:
      
   vyber = input("co chces pridat? ---> ")

   if vyber in polozkyaceny:
    try:
     kolko = int(input("Kolko chces? ---> "))
    except ValueError:
      print("napis cislo")
      continue

    cena, mnozstvo = polozkyaceny[vyber]

    if kolko <= mnozstvo:
     mnozstvo -=kolko
     polozkyaceny[vyber] = (cena, mnozstvo)

     kosik.append([vyber, cena, kolko])
    else:
      print("Nemame tolko kusov")

   elif vyber.lower() == "uz nic" or vyber.lower() == "nothing":
     anoniezobrazenieinput = input("Chces zobrazit kosik? ---> ")

     if anoniezobrazenieinput.lower() == "ano":
         spolu = 0

         for polozka, cena, mnozstvo in kosik:
           spolu += cena * mnozstvo
       
         print("\n--------------------")
         for polozka, cena, mnozstvo in kosik:
            if polozka in ovocie:
             kategoria = "ovocie"
               
            elif polozka in zelenina:
             kategoria = "zelenina"
               
            elif polozka in sladkosti:
             kategoria = "sladkost"
               
            else:
             kategoria = "ine"

            print(f"{polozka} - {cena}€ x {mnozstvo} - {kategoria}")
         print("      -------")
         print(f"spolu: {spolu} €")
     elif anoniezobrazenieinput.lower() == "nie":
       break

   else:
    print("Taku vec nemame")