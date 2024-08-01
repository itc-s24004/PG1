class MyIterator:
  def __init__(self, data):
    self.data = data
    self.index = 0

  def __iter__(self):
    #MyIterator が __next__() を実装しているので self をイテレータとして返す
    return self
  
  def __next__(self):
    if self.index == len(self.data):
      raise StopIteration()
    value = self.data[self.index]
    self.index = self.index + 1
    return value
  

# シーケンスを一例として文字列を渡す
itr = MyIterator("spam")
for char in itr:
  print(char, end=" ")





def reverse(data):
  '''引数に受け取ったシーケンスを逆向きに返す'''
  ret = []
  for index in range(len(data)-1, -1, -1):
    ret.append(data[index])
  return ret



# リストをforループのinに添える(forループで反復氏が作られる)
for char in reverse("flog"):
  print(char, end=" ")