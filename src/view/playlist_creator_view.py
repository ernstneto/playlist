import os
from src.model.repositories.musics_repository import music_repository


class PlaylistCreatorView:
    def __init__(self):
        self._music_repository = music_repository

    def get_all_musics(self):
        musics = self._music_repository.get_all_musics()
        return [{
            "title": music.title,
            "artist": music.artist,
            "year": music.year
        } for music in musics]
    
    def playlist_creator_success(self, controller_response: dict) -> None:
        self.__clear()
        print("Playlist criada com sucesso!")

        for music in controller_response["musics"]:
            print(f"- {music['title']} - {music['artist']} ({music['year']})")
    
    def playlist_create_fail(self, error_message: str) -> dict:
        self.__clear()
        print(f"Erro na criação da playlist:\nErro: {error_message}\n")
    
    def __clear(self):
        os.system("cls||clear")