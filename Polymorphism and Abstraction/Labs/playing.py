class Guitar:

    def play(self):
        return "Playing the guitar"

def start_playing(guitar):
    return guitar.play()

guitar = Guitar()
print(start_playing(guitar))