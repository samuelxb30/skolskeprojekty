from pathlib import Path #modul na ignorovanie (dostatie vacieho permission) safety features pre normalny open() 

filepath = Path("createdautomatically/notes.txt") #vytvoreny dir

filepath.parent.mkdir(parents=True, exist_ok=True) #filepath.parent vytvori vsetky subory okrem posledneho, mkdir vytvory directory, parents vytvori vsetky predchadzajuce priecinky a exist ok ignoruje uz vytvorene aby sa predoslo padaniu

with open(filepath, "w") as f:      #vytvori subor vo filepath a napise pomocou "w". as sa pouziva na urcenie mena premennej ked sa pouziva with. f.write("xx") napise nieco do toho suboru
    f.write("Hello world!")
