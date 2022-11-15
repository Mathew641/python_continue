
# continue -- This is also a functional keyword, which has opposite concept from that of break.


'''for num in range(1,21): # range(1,21) = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21] , basicaly the list has been created.
    if(num<10):
      continue
    print(num)'''

# Suppose, if we use same code for solving the same problem but this time don't use continue keyword

for num in range(1,21): # range(1,21) = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21] , basicaly the list has been created.
    if(num<10):
      #continue
      print(num)
 # see, so we get completely wrong output i.e. all the no.'s less than 10 has been printed instead what we targetting to print i.e. no.>10.ab
