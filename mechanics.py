from random import randint

mercadorias =   {
  "1": "Poção",
  "2": "Pão",
}
x = mercadorias.get(input(""))
print("você comprou:", x)

dado = randint(0,6)

y = input("")

if(y == "girar"):
print(dado)
