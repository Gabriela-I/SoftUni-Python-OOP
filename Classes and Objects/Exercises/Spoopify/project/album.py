from project.song import Song


class Album:
    def __init__(self, name: str, *songs):
        self.name = name
        self.published = False
        self.songs = list(songs)

    def add_song(self, song: Song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if self.published:
            return f"Cannot add songs. Album is published."
        if song not in self.songs:
            self.songs.append(song)
            return f"Song {song.name} has been added to the album {self.name}."
        return "Song is already in the album."

    def remove_song(self, song_name: str):
        try:
            s = next(filter(lambda x: x.name == song_name, self.songs))
        except StopIteration:
            return 'Song is not in the album.'

        if self.published:
            return f"Cannot remove songs. Album is published."
        self.songs.remove(s)
        return f"Removed song {song_name} from album {self.name}."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        songs_data = '\n'.join([f"== {s.get_info()}" for s in self.songs])
        return f"Album {self.name}\n{songs_data}\n"
