from src.model.entities.music import Music


class MusicRepository:
    def __init__(self):
        self._musics_list = []

    def insert_music(self, music: Music) -> None:
        self._musics_list.append(music)

    def get_all_musics(self):
        return self._musics_list

    def find_music_by_title(self, title: str):
        for music in self._musics_list:
            if music.title == title:
                return music
        return None

# Singleton instance
music_repository = MusicRepository()