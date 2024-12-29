class Carro:
    def __init__(self,marca,modelo,ano,cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
    
    def ligar(self):
        print(f'{self.marca} {self.modelo} está ligado.')
    
    def desligar(self):
        print(f'{self.marca} {self.modelo} está desligado.')
    
    def acelerar(self):
        print(f'{self.marca} {self.modelo} está acelerando...')