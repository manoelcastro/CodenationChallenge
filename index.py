from requisicao import BuscarDados
from traducao import Tradutor
from entrega import Entregar

print('Verificando se já existe orientações')
if BuscarDados.preparar_arquivo():
  print('Requiscao feita com sucesso e documento preparado!')
if Tradutor.traduzir_cifra():
  print('Codigo decifrado com sucesso!')
  print('Resultado da atividade:')
print(Entregar.arquivo())  
