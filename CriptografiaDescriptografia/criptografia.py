import json

class Criptografia:
    def __init__(self):
        with open("enconding.json", "r", encoding="utf-8") as arquivo:
            self.enconding = json.load(arquivo)

        with open("decoding.json", "r", encoding="utf-8") as arquivo:
            self.decoding = json.load(arquivo)

    def criptografar(self, mensagem: str) -> str:
        mensagem_criptografada = ""
        for char in mensagem:
            if char in self.enconding:
                mensagem_criptografada += self.enconding[char]
            else:
                mensagem_criptografada += char
        return mensagem_criptografada
    
    def descriptografar(self, mensagem: str) -> str:
        mensagem_descriptografada = ""
        for char in mensagem:
            if char in self.decoding:
                mensagem_descriptografada += self.decoding[char]
            else:
                mensagem_descriptografada += char
        return mensagem_descriptografada