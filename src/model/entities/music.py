class Music:
  def __init__(self, title: str, artist: str, year: int):
      self.title = title
      self.artist = artist
      self.year = year

  def __repr__(self):
      return f"Music(title='{self.title}', artist='{self.artist}', year={self.year})"