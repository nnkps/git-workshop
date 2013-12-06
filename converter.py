    def loadFont(self, directory):
        pass

class TextDrawer:
    def setFont(self, font):
        pass

    def draw(self, text):
        pass


t = getText()

def getText():
    return 'Git'

class Font:
    pass

class FontLoader:
    def loadFont(self, directory):
        pass

t = getText()
f = FontLoader().loadFont('fancyFont/')

def getText():
    return 'Git'

t = getText()
f = FontLoader().loadFont('fancyFont/')

t = getText()
f = FontLoader().loadFont('fancyFont/')
d = TextDrawer()
d.setFont(f)
d.draw(t)

