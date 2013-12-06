from font import Font, FontLoader

class TextDrawer:
    def setFont(self, font):
        pass

    def draw(self, text):
        pass

def getText():
    return 'Git'

class Font:
    pass

class FontLoader:
    def loadFont(self, directory):
        pass

text = getText()
font = FontLoader().loadFont('fancyFont/')

drawer = TextDrawer()
drawer.setFont(font)
drawer.draw(text)
