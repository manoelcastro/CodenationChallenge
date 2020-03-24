import json
import re
from sha1 import Resumir

class Tradutor:
  @classmethod
  def abrir_arquivo(cls):
    try:
      answer = open('answer.json', 'r')
      cls.arquivo = json.load(answer)
    except:
      pass
    return
  
  @classmethod
  def traduzir_cifra(cls):
    cls.abrir_arquivo()  
    decifrado = ''.join(cls.decifre())
    cls.arquivo['decifrado'] = decifrado.lower()
    cls.arquivo['resumo_criptografico'] = Resumir.sha1(cls.arquivo['decifrado'])

    try:
      cls.answer = open('answer.json', 'w')
      json.dump(cls.arquivo, cls.answer, indent=4)
    except:
      return 0

    cls.answer.close()
    return 1
 
  @classmethod
  def preparar_excecoes(cls):
    exc = re.compile("[\s\W0-9]")
    lista_excecoes = set(re.findall(exc, cls.arquivo['cifrado']))
    return lista_excecoes
  
  @classmethod
  def decifre(cls):
    traducao_letras = []
    
    for char in cls.arquivo['cifrado']:
      if not char in cls.preparar_excecoes():
        ascii_codigo = ord(char)
        char = chr(ascii_codigo - cls.arquivo['numero_casas'])
      traducao_letras.append(char)
    return traducao_letras 