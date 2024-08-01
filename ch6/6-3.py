class Nigiri:
  category = "にぎり"
  top = "ねた"
  base = "しゃり"

  def show_attributes(self):
    print("top: {}, base: {}, catecory: {}".format(self.top, self.base, self.category))

class Maguro(Nigiri):
  top = "まぐろ"
  price = 100

  def __init__(self, wasabi="ワサビ抜き"):
    self.wasabi = wasabi

  def show_attributes(self):
    super().show_attributes()
    print("wasabi: {}".format(self.wasabi))

  def show_one_dish_price(self, num_nigiri=2):
    result = self.price * num_nigiri
    print("1皿({}かん)の値段: {}円".format(num_nigiri, result))

  
m = Maguro()
m.show_attributes()
m.show_one_dish_price()

m2 = Maguro("ワサビ入り")
m2.show_attributes()
m2.show_one_dish_price()