class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash_function(self, key):
        return key % self.size

    def insert(self, value):
        key = value % self.size
        index = self._hash_function(key)
        self.table[index].append(value)

    def get(self, key):
        index = self._hash_function(key)
        for val in self.table[index]:
            if val == key:
                return index
        raise KeyError(f"Key '{key}' not found")

    def remove(self, key):
        index = self._hash_function(key)
        for i, val in enumerate(self.table[index]):
            if val == key:
                del self.table[index][i]
                return
        raise KeyError(f"Key '{key}' not found")

    def imprimir(self):
        for index, bucket in enumerate(self.table):
            print(f"Posição {index}: {bucket}")

#1 Verifique se a lista de valores apresenta colisão quando utilizamos uma tabela hash. Valore[120,  123, 145, 90, 39, 45, 23, 220]?

hash_table = HashTable(8)
hash_table.insert(120)
hash_table.insert(123)
hash_table.insert(145)
hash_table.insert(90)
hash_table.insert(39)
hash_table.insert(45)
hash_table.insert(23)
hash_table.insert(220)

hash_table.imprimir()

#2 Diante da lista de Valore[120, 123, 145, 90, 39, 45, 23, 220], qual o valor do índice para 145 que tá  apontando para a tabela hash?
hash_table.get(145)

#3 Verifique se a lista de caracteres apresenta colisão quando utilizamos uma tabela hash.  Valore['U','N','I','E','S','P','F','A','C','U','L','D','A','D','E']?
conjunto1 = ('U','N','I','E','S','P','F','A','C','U','L','D','A','D','E')
hash_table = HashTable(15)
for i in conjunto1:
  hash_table.insert(ord(i))
hash_table.imprimir()

#4 Dado os valores 2341, 4234, 2839, 430, 22, 397, 3920, uma tabela hash de tamanho 7, e função de  hash h(x) = x % 7, mostre o resultante depois de inserir os valores na ordem dada.

valores = [2341, 4234, 2839, 430, 22, 397, 3920]
tamanho_tabela = 7

hash_table = HashTable(tamanho_tabela)

for valor in valores:
  hash_table.insert(valor)

hash_table.imprimir()

#5 Dada uma tabela hash de tamanho 17, se as chaves 2, 32, 43, 16, 77, 51, 1, 17, 42, 111 forem  inseridas sequencialmente com a função de hash h(k) = k % 17, mostre o resultado depois de inserir  os valores na ordem dada.
hash_table = HashTable(17)
hash_table.insert(2)
hash_table.insert(32)
hash_table.insert(43)
hash_table.insert(16)
hash_table.insert(77)
hash_table.insert(51)
hash_table.insert(1)
hash_table.insert(17)
hash_table.insert(42)
hash_table.insert(111)

for i in range(17):
  print(f"Posição {i}: {hash_table.table[i]}")

  #6 Desenhe uma tabela de hash resultante da introdução das chaves 12, 44, 13, 88, 23, 94, 11, 39, 20, 16 e 5, usando a função de hash h(k) = (2k + 5)%11.

def h(k):
  return (2 * k + 5) % 11

chaves = [12, 44, 13, 88, 23, 94, 11, 39, 20, 16, 5]
tabela_hash = [[] for _ in range(11)]

for chave in chaves:
  indice = h(chave)
  tabela_hash[indice].append(chave)

print("Tabela Hash:")
for i in range(11):
  print(f"Posição {i}: {tabela_hash[i]}")