'''
Returneaza true daca n este prim si false daca nu.
'''
def is_prime(n):
  if nr < 2:
    return False
  for i in range(2,nr):
    if nr % i ==0:
      return False
  return True
  
  
'''
Returneaza produsul numerelor din lista lst.
'''
def get_product(lst):
  return a*b*c
  
  
'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''
def get_cmmdc_v1(x, y):
  while n!=m:
    if n>m:
      n=n-m
    else:
      m=m-n
  
  
'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''
def get_cmmdc_v2(x, y):
  while m != 0:
    r=n%m
    n=m
    m=r
  return n
  
  
def main():
  f = False
  while f != True:
    print("1 Determinare nr prim")
    print("2 Produsul a n nr naturale")
    print("3 Prima metoda de aflare a CMMDC")
    print("4 A doua metoda de aflare a CMMDC")
    print("5. Iesire")
    optiune = input("Alege obtiunea")
    if optiune == "1":
      nr=int(input("Dati un nr : "))
      if is_prime(nr):
        print("Nr este prim ")
      else:
        print("Nr nu este prim")
    if optiune == "2":
      nr1 = int(input("Nr 1 este:"))
      nr2 = int(input("Nr 2 este:"))
      nr3 = int(input("Nr 3 este:"))
      p = get_prod(nr1,nr2,nr3)
      print(f"Produsul dintre {nr1},{nr2},{nr3} este = {p}")

    if optiune == "3":
      n = int(input("Nr 1 este:"))
      m = int(input("Nr 2 este:"))
      cmd = cmmdc1(n,m)
      print(f"Cmmdc a nr {n},{m} este {cmd}")

    if optiune =="4":
      n = int(input("Nr 1 este:"))
      m = int(input("Nr 2 este:"))
      cmd = cmmdc2(n,m)
      print(f"Cmmdc a nr {n},{m} este {cmd}")

    if optiune =="5":
      f = True

if __name__ == '__main__':
  main()
