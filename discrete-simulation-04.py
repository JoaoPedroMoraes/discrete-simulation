#Aula 23/05
#comando para instalação: pip3 install simpy
import simpy

class Carro:
    def __init__(self, env, nome, frequencia):
        self.nome = nome
        self.frequencia = frequencia
        self.env = env
        self.env.process(self.run())
        
    def run(self):
        while True:
            yield self.env.timeout(self.frequencia)
            print(self.nome ,'passou no tempo de', self.env.now)

class Onibus:
    def __init__(self, env, nome, frequencia):
        self.nome = nome
        self.frequencia = frequencia
        self.env = env
        self.env.process(self.run())
        
    def run(self):
        while True:
            yield self.env.timeout(self.frequencia)
            print('O onibus', self.nome ,'passou no tempo de', self.env.now)
            
            
#Declarou na variavel o env do ambiente        
env = simpy.Environment()
#Instancia dos objetos carro com a variavel de ambiente env
p = Carro(env, 'Opala', 4)
q = Carro(env, 'Palio', 2)
r = Carro(env, 'Fusca', 7)
x = Onibus(env, 'Pedreira Lomas', 1)
y = Onibus(env, 'Alcindo do Cacela', 0.5)
env.run(until = 50) #Como é um loop infinito é bom colocar um delimitador para o tempo
