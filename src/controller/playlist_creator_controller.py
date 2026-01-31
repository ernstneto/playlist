from src.model.repositories.musics_repository import music_repository
import random


class PlaylistCreatorController:
    
    def create_playlist(self) -> dict:
        try:
          musics = self.__get_all_songs_and_verify()
          playlist = self.__create_playlist(musics)
          return self.__format_response(playlist)
        except Exception as e:
          return self.__format_error_response(e)
    
    def __get_all_songs_and_verify(self) -> list:
        music = music_repository.get_all_musics()
        if music is []:
            raise Exception("No songs registered to create a playlist.")
        return music
    
    def __create_playlist(self, musics: list) -> list:
        random.shuffle(musics)
        return musics
    def __format_response(self, playlist: list) -> dict:
        return {
            "success": True,
            "playlist": playlist
        }
    def __format_error_response(self, err: Exception) -> dict:
        return {
            "success": False,
            "error": str(err)
        }