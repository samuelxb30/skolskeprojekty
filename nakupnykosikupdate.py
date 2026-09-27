<<<<<<< HEAD
=======
ovocie = ["marhula", "jablko"]
zelenina = ["petrzlen", "mrkva"]
sladkosti = ["cukor", "cokolada"]

kupon = ["beli67", "dariuskral", "matojegoat", "MGfitman69"]
>>>>>>> 4c7f86e5c9509b324a62a39682e5a4ae6e45c019

polozkyaceny = {
  "jablko": (1,"ovocie", 100),
  "marhula": (1.5,"ovocie", 60),
  "banan": (1.5,"ovocie", 20),
  "petrzlen": (2,"zelenina", 35),
  "cukor": (2.3,"sladkosti", 5),
  "mrkva": (2,"zelenina", 35),
  "cokolada": (3,"sladkosti", 20),
  "rohlik": (0.10,"ine", 300)
}

kupon = [
  ["beli67", "dariuskral", "LIMITED"], 
  ["matojegoat", "MGfitman69"]
  ]

kosik = []

print("Dobry den, nech sa paci mozte si vybrat\n")
for polozka, (cena, kategoria, mnozstvo) in polozkyaceny.items():
  print(f"{polozka} - {cena}€ - {mnozstvo} ostáva")

while True:
      
   vyber = input("co chces pridat? ---> ")

   if vyber in polozkyaceny:
    while True:
     try:
      kolko = int(input("Kolko chces? ---> "))

      if kolko <= 0:
        print("Zadaj kladne cislo")
        continue

      break
      
     except ValueError:
      print("napis cislo")
      continue

    cena, kategoria, mnozstvo = polozkyaceny[vyber]

    if kolko <= mnozstvo:
     mnozstvo -=kolko
     polozkyaceny[vyber] = (cena, kategoria, mnozstvo)

     kosik.append([vyber, cena, kategoria, kolko])
    else:
      print("Nemame tolko kusov")

   elif vyber.lower() == "uz nic" or vyber.lower() == "nothing":

      anoniezobrazenieinput = input("Chces zobrazit kosik? ---> ")

      if anoniezobrazenieinput.lower() == "ano":
         spolu = 0

         for polozka, cena, kategoria, mnozstvo in kosik:
           spolu += cena * mnozstvo
<<<<<<< HEAD

         overo = False
         platny = False
         while True:
          kuponzobrazenieinput = input("uplatni kupon ---> ")

          if kuponzobrazenieinput.lower() == "nie" or kuponzobrazenieinput.lower() == "nemam":
           print("Kupon neuplatneny")
           break

          for deskupon, petkupon, overkupon in kupon:

           if kuponzobrazenieinput == deskupon:
            spolu = spolu - (spolu*30/100)
            print("\n prvy kupon uplatneny\n")
            platny = True
            break
           
           elif kuponzobrazenieinput == petkupon:
            spolu = spolu - (spolu*20/100)
            print("\n druhy kupon uplatneny")
            platny = True
            break

           if spolu >= 50:
              overo = True

           if overo:
             if kuponzobrazenieinput == overkupon:
               spolu = spolu - (spolu*40/100)
               print("KUPON NAD 50 EUR AKTIVOVANY")
               platny = True
               break
           else:
             break
             
          
          if platny:
            break
          else:
           print("neplatny kupon, skus znova")

         print("\n--------------------")
         for polozka, cena, kategoria, mnozstvo in kosik:

=======

         kuponzobrazenieinput = input("uplatni kupon ---> ")
         if kuponzobrazenieinput in kupon:
           spolu -= 10
           print("\nKupon uplatneny\n")

         elif kuponzobrazenieinput.lower() == "nie" or kuponzobrazenieinput.lower() == "nemam":
           print("Kupon neuplatneny")

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

>>>>>>> 4c7f86e5c9509b324a62a39682e5a4ae6e45c019
             print(f"{polozka} - {cena}€ x {mnozstvo} - {kategoria}")
         print("      -------")
         print(f"spolu: {spolu} €")
      elif anoniezobrazenieinput.lower() == "nie":
<<<<<<< HEAD
        break
=======
       break
>>>>>>> 4c7f86e5c9509b324a62a39682e5a4ae6e45c019

   else:
    print("Taku vec nemame")