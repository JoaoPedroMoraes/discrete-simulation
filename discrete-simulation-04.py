#comando para instalação: pip3 install simpy
import simpy

class Carro:
    def __init__(self, env):
        self.frequencia = 3
        self.env = env
        self.env.process(self.run())
        
    def run(self):
        while True:
            yield self.env.process(self.frequencia)
            print('Carro passou em', self.env.now)
            
