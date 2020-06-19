#python
c = "Crackle"
p = "Pop"
for x in range(1,101) :
  if (x%15==0) :
    print(c + p)
  elif (x%3 == 0) :
    print(c)
  elif (x%5==0) :
    print(p)
  else :
    print(x)
