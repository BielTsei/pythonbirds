class Pessoa:
    olhos=2
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar(self):
        return f"Olá meu nome é {self.nome}."

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_classe_pai = super().cumprimentar()
        return f'{cumprimentar_classe_pai} Aperto de mão.'

class Mutante(Pessoa):
    def cumprimentar(self):
        cumprimentar_classe_pai_2 = super().cumprimentar()
        return f'{cumprimentar_classe_pai_2} Abraço.'
    olhos = 3

if __name__ == '__main__':
    gabriel = Mutante(nome='Gabriel')
    luciano = Homem(gabriel, nome='Luciano')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)
    luciano.sobrenome = 'Ramalho'
    del luciano.filhos
    luciano.olhos = 1
    del luciano.olhos
    print(luciano.__dict__)
    print(gabriel.__dict__)
    print(Pessoa.olhos)
    print(luciano.olhos)
    print(gabriel.olhos)
    print(id(Pessoa.olhos), id(luciano.olhos), id(gabriel.olhos))
    print(Pessoa.metodo_estatico(), luciano.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), luciano.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(gabriel, Homem))
    print(isinstance(gabriel, Pessoa))
    print(gabriel.olhos)
    print(luciano.cumprimentar())
    print(gabriel.cumprimentar())