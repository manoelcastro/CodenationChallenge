import hashlib

class Resumir:
  @classmethod
  def sha1(cls, text):
    resumo = hashlib.sha1(str(text).encode('utf-8'))
    print('Sha1 gerado com sucesso!')
    return resumo.hexdigest()