#comando para instalação: pip3 install simpy
import simpy

class Pessoa:
    def __init__(self, env):
        self.env = env
        env.process(self.run())
        
    def run(self):
        while True:
            print('Começou a estudar em', self.env.now)
            tempo_estudo = 2
            yield self.env.process(self.estudar(tempo_estudo))
            
            print('Foi para as redes sociais em', self.env.now)
            tempo_redes_sociais = 5
            yield self.env.timeout(tempo_redes_sociais)
            
    def estudar(self, tempo_estudo):
        yield self.env.timeout(tempo_estudo)

#Declarou na variavel o env do ambiente        
env = simpy.Environment()
#Instancia o obejto pessoa com a variavel env'
p = Pessoa(env)

env.run(until = 50) #como é um loop infinito é bom colocar um delimitador para o tempo
