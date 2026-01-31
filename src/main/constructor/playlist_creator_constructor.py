from src.controller.playlist_creator_controller import PlaylistCreatorController
from src.view.playlist_creator_view import PlaylistCreatorView


def playlist_creator_process():
  playlist_creator_view = PlaylistCreatorView()
  playlist_creator_controller = PlaylistCreatorController()

  response = playlist_creator_controller.create_playlist(playlist_creator_view)

  if response["success"]:
    playlist_creator_view.playlist_creator_success(response)
  else:
    playlist_creator_view.playlist_create_fail(response)