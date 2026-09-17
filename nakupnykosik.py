ovocie = ["marhula", "jablko"]
zelenina = ["petrzlen", "mrkva"]
sladkosti = ["cukor", "cokolada"]



polozkyaceny = {
  "jablko": 1,
  "marhula": 1.5,
  "banan": 1.3,
  "petrzlen": 2,
  "cukor": 2.3,
  "mrkva": 2,
  "cokolada": 3,
  "rohlik": 0.10
}

kosik = []

print("Dobry den, nech sa paci mozte si vybrat\n")
for polozka, cena in polozkyaceny.items():
  print(polozka, cena)

while True:
 try:
   pocetpoloziek = int(input("\nkolko chces pridat poloziek do kosika? ---> "))

 except ValueError:
  print("Napis cislo pocet")
  continue


 for i in range(pocetpoloziek):
      vyber = input("co chces pridat? ---> ")

      if vyber.lower() == "uz nic":
       break

      if vyber in polozkyaceny:
       cena = polozkyaceny[vyber]
       kosik.append([vyber, cena])

      else:
       print("Taku vec nemame")

 anoniezobrazenieinput = input("Chces zobrazit kosik? ---> ")

 if anoniezobrazenieinput.lower() == "ano":

      spolu = 0
      for polozka, cena in kosik:
        spolu += cena

      print("\n--------------------")
      for polozka, cena in kosik:
       
          if polozka in ovocie:
           kategoria = "ovocie"
 
          elif polozka in zelenina:
           kategoria = "zelenina"
 
          elif polozka in sladkosti:
           kategoria = "sladkost"
 
          else:
           kategoria = "ine"
           
          print(f"{polozka} - {cena} € - {kategoria}")
      print("      -------")
      print(f"spolu: {spolu} €")

 else:
  break