from typing import List

from project.album import Album


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums: List[Album] = []

    def add_album(self, album: Album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        try:
            a = next(filter(lambda x: x.name == album_name, self.albums))
        except StopIteration:
            return f'Album {album_name} is not found.'

        if a.published:
            return f"Album has been published. It cannot be removed."
        self.albums.remove(a)
        return f"Album {album_name} has been removed."

    def details(self):
        album_data = '\n'.join([a.details() for a in self.albums])
        return f"Band {self.name}\n" \
               f"{album_data}"