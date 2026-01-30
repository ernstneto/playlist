import os

class SongRegisterView:
  def registry_song_initial(self) -> dict:
    self.__clear()
    print("Implementar Nova Musica \n\n")

    title = input("Determine o nome da musica: ")
    artist = input("Determina o nome do artista: ")
    year = input("Determine o ano de publicação: ")

    new_song_informations = {
      "title": title,
      "artist": artist,
      "year": year
    }
    return new_song_informations

  def __clear(self):
    os.system("cls||clear")

  def registry_song_success(self, controller_response: dict) -> None:
    self.__clear()
    print("Música cadastrada com sucesso!\n")
    print("Detalhes da música cadastrada:")
    print(f"Título: {controller_response['attributes']['title']}")
    print(f"Artista: {controller_response['attributes']['artist']}")
    print(f"Ano de Publicação: {controller_response['attributes']['year']}\n")
    input("Pressione Enter para continuar...")
  
  def registry_song_failure(self, controller_response: dict) -> None:
    self.__clear()
    print("Falha ao cadastrar a música.\n")
    print(f"Erro: {controller_response['error']}\n")
    input("Pressione Enter para continuar...")