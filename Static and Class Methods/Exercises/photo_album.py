from math import ceil


class PhotoAlbum:
    COUNT_OF_PHOTOS = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(ceil(photos_count / cls.COUNT_OF_PHOTOS))

    def add_photo(self, label: str):
        for p in range(len(self.photos)):
            if len(self.photos[p]) < PhotoAlbum.COUNT_OF_PHOTOS:
                self.photos[p].append(label)
                return f"{label} photo added successfully on page {p + 1} slot {len(self.photos[p])}"

        return "No more free slots"

    def display(self):
        result = [
            f'{"-" * 11}'
        ]
        for p in self.photos:
            result.append(("[] " * len(p)).rstrip())
            result.append("-" * 11)

        return '\n'.join(result)


# album = PhotoAlbum(4)
#
# print(album.add_photo("baby"))
#
# print(album.add_photo("first grade"))
#
# print(album.add_photo("eight grade"))
#
# print(album.add_photo("party with friends"))
#
# print(album.photos)
#
# print(album.add_photo("prom"))
#
# print(album.add_photo("wedding"))
#
# print(album.add_photo("eight grade"))
#
# print(album.add_photo("eight grade"))
#
# print(album.add_photo("eight grade"))
#
# print(album.add_photo("eight grade"))
#
# print(album.add_photo("eight grade"))
#
# print(album.display())

