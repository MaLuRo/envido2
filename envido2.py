import random

class Mazo:

  mazo = []
  mano = []
  def __init__(self):
    valores = [1,2,3,4,5,6,7,10,11,12]
    palos = ["Espada", "Basto", "Oro", "Copas"]
    for valor in valores:
      for palo in palos:
        tupla = palo, valor
        self.mazo.append(tupla)
    
  def mezclar_mazo(self):
    self.mazo_copia = self.mazo[:]
    random.shuffle(self.mazo_copia)

  def repartir_cartas(self):
    for i in range(3):
      self.mano.append(self.mazo_copia[i])
      self.mazo.remove(self.mazo_copia[i])
    return self.mano

class Jugador:

  nombre = ''
  mano = []

  def __init__(self,nombre,mano):
    self.nombre = nombre
    self.mano = mano

  def recibir_cartas(self):
    print(f"{self.nombre} tus cartas son {self.mano}")

  def cantar_envido(self):
    cantar = input("Quiere cantar envido? (si/no)")
    if cantar == "si":
      print("Envido Carajo!")
    elif cantar == "no":
      pass
    else:
      cantar = input("Quiere cantar envido? responda solo con si o con no)")

  def aceptar_envido(self):
    print("Quiero ver...")
  
  def verificar_envido(self):
    aux = 0
    counter = 0
    mano_dic = dict()
    lista= []
    for carta in self.mano:
      if carta[0] not in mano_dic:
        mano_dic [carta[0]] = carta[1]
      else:
        lista.append(carta[1])
        if len(lista) < 2:
          lista.append(mano_dic.get(carta[0]))
        mano_dic [carta[0]] = lista
#    print(mano_dic,"*")
    if len(mano_dic) == 1:
      ("Tiene FLOR")
      
    for item in lista:
      if item in [10,11,12]:
        counter += 1
      else:
        aux = aux + item
    if len(mano_dic) != 3:
      if counter == 0:
        aux += 20
        print(aux)
      elif counter == 1:
        aux += 20
        print(aux)
      else:
        if item in [10,11,12]:
          print("20")
        else:
          print("Sin envido")

mazo = Mazo()

mazo.mezclar_mazo()

mano = mazo.repartir_cartas()



print(mano)

