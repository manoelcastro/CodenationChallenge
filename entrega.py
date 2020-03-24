import requests

class Entregar:
  @classmethod
  def arquivo(cls):
    url = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=028af1d790a80796d4d965e219d4add080931db8'
    answer = {'answer': open('answer.json', 'rb')}
    r = requests.post(url, files=answer)
    return r.json()