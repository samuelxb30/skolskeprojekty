while True:
 akysposobinput = int(input("Ked chces trojuholnik od najvacieho po najmensi stlac 1 a ked opacne tak 2 ---> "))


 def prvysposob():
   znak = "X"

   for i in range(20, 0, -1):
    print(znak*i)
   print("") #kvôli oddeleniu

 def druhysposob():
  znak = "X"

  for i in range(0, 20, 1):
    print(znak*i)
  print("") #kvôli oddeleniu

 if akysposobinput == 1:
  prvysposob()

 if akysposobinput == 2:
  druhysposob()
