t = input("Ievadi tekstu: ")
if t.count("e")>0:
  t = t.replace("e", " ")
  t = t.upper()
  print("Teksts: ", t)
else:
  d = "NAV VAJADZĪGO BURTU."
  print(d)