# Definindo a classe Heroi
class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo
    
    def atacar(self):
        # Condicionais para definir o ataque baseado no tipo do herói
        if self.tipo == "mago":
            ataque = "usou magia"
        elif self.tipo == "guerreiro":
            ataque = "usou espada"
        elif self.tipo == "monge":
            ataque = "usou artes marciais"
        elif self.tipo == "ninja":
            ataque = "usou shuriken"
        else:
            ataque = "fez um ataque comum"
        
        # Exibindo a mensagem de ataque
        print(f"O {self.tipo} atacou usando {ataque}")

# Criando objetos da classe Heroi e testando o método atacar
heroi1 = Heroi("Arthas", 30, "guerreiro")
heroi1.atacar()  # Exibe: O guerreiro atacou usando espada

heroi2 = Heroi("Merlin", 150, "mago")
heroi2.atacar()  # Exibe: O mago atacou usando magia

heroi3 = Heroi("Liu Kang", 35, "monge")
heroi3.atacar()  # Exibe: O monge atacou usando artes marciais

heroi4 = Heroi("Ryu Hayabusa", 29, "ninja")
heroi4.atacar()  # Exibe: O ninja atacou usando shuriken
