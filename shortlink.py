"""
Script principal
"""
from pyshorteners import Shortener

class Shortlinks(Shortener):
    """
    Classe que lida com a compressão ou encurtamento do link.
    """
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
            print('Opção inválida.')

    def short_url(self):
        """
        Encurta uma URL
        """
        self.shortened_url = self.shortener.short(self.url)
        print("Short URL: " + self.shortened_url + "\n")

    def decode_url(self):
        """
        Descomprime uma URL
        """
        self.decoded_url = self.shortener.expand(self.url)
        print("URL decodificada: " + self.decoded_url + "\n")

    def qrcode_url(self):
        """
        Gera o QRCode da URL.
        """
        self.shortener.short(self.url)
        print(self.shortener.qrcode())

APP = Shortlinks()
