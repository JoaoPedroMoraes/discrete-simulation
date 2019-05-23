#comando para instalação: pip3 install simpy
import simpy

class Carro:
    def __init__(self, env):
        self.frequencia = 3
        self.env = env
        self.env.process(self.run())
        
    def run(self):
        while True:
            yield self.env.timeout(self.frequencia)
            print('Carro passou em ', self.env.now)
            
#Declarou na variavel o env do ambiente        
env = simpy.Environment()
#Instancia o objeto pessoa com a variavel env'
p = Carro(env)
env.run(until = 50) #como é um loop infinito é bom colocar um delimitador para o tempo
