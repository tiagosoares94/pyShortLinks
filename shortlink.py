from pyshorteners import Shortener

class shortlinks(Shortener):
    def __init__(self):
        print('''
        Instruções: 
            Entre com uma URL válida e aperte enter.
            exemplo: https://dev.to/peteranglea/6-months-of-working-remotely-taught-me-a-thing-orten
        Opções:
            1. Encurtar a URL
            2. Decodificar uma URL encurtada
            3. Transformar URL em QR code
        ''')
        self.option = int(input("Escolha uma opção: "))
        self.url = str(input("Entre com a URL: "))
        self.shortener = Shortener('Tinyurl')
        if self.option == 1:
            self.short_url()
        elif self.option == 2:
            self.decode_url()
        elif self.option == 3:
            self.qrcode_url()
        else:
            pass

    def short_url(self):
        self.encurta = self.shortener.short(self.url)
        print("Short URL: " + self.encurta + "\n")
        

    def decode_url(self):
        self.decodedUrl = self.shortener.expand(self.url)
        print("URL decodificada: " + self.decodedUrl + "\n")

    def qrcode_url(self):
        self.encurta = self.shortener.short(self.url)
        print(self.shortener.qrcode())

app = shortlinks()
