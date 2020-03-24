import requests
import json

class BuscarDados:

  @classmethod
  def requisitar(cls):
    try:
      answer = open('answer.json', 'r')
    except:
      answer = 0

    if not(answer):
      try:
        requisicao = requests.get("https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=028af1d790a80796d4d965e219d4add080931db8")
        return requisicao

      except:
        print('Ocorreu um erro na requisição.')
        pass

    return False

  @classmethod
  def preparar_arquivo(cls):  
    resposta = cls.requisitar()

    if not resposta:
      return False
    
    respostaJson = resposta.json()
    respostaJson['cifrado'] = respostaJson['cifrado'].lower()
    answer = open('answer.json','w')
    json.dump(respostaJson, answer, indent=4)
    answer.close()
    return True