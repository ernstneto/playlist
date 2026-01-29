def introduction_page() -> str:
  print("Welcome to the Music Playlist Manager!")
  print("Select an option:")
  print("1. Insert Music")
  print("2. Create Playlist")
  print("5. Exit")
  command = input("Desired option: ")
  return command