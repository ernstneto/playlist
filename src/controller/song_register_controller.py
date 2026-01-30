from src.model.entities.music import Music
from src.model.repositories.musics_repository import music_repository


class SongRegisterController:
  def insert(self, new_song_informations: dict) -> dict:
    try:  
      self.__verify_songs_infos(new_song_informations)
      self.__verify_if_song_already_registered(new_song_informations)
      self.__insert_song(new_song_informations)
      return self.__format_response(new_song_informations)
    except Exception as e:
      return self.__format__error_response(e)
  
  def __verify_if_song_already_registered(self, new_song_informations: dict) -> None:
    new_song_title = new_song_informations['title']
    search_response = music_repository.find_music_by_title(new_song_title)

    if search_response is not None:
      raise Exception("A música já está registrada.")

  def __verify_songs_infos(self, new_song_informations: dict) -> None:
    if(len(new_song_informations['title'])> 100):
      raise ValueError("O título da música não pode exceder 100 caracteres.")
    
    year = int(new_song_informations['year'])
    if(year > 2026):
      raise ValueError("O ano de publicação deve ser até 2026.")
    
  def __insert_song(self, new_song_informations: dict) -> None:
    new_music = Music(
      title=new_song_informations['title'],
      artist=new_song_informations['artist'],
      year=int(new_song_informations['year'])
    )
    music_repository.insert_music(new_music)


  def __format_response(self, new_song_informations: dict) -> dict:
    return {
      "success": True,
      "count": 1,
      "attributes": {
        "title": new_song_informations['title'],
        "artist": new_song_informations['artist'],
        "year": new_song_informations['year']
      }
    }
  
  def __format__error_response(self, err: Exception) -> dict:
    return {
      "success": False,
      "error": str(err)
    }