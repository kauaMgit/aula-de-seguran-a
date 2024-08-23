class Carro:
    def __init__(self,marca, modelo, ano, cor , preco):
        self.__marca = marca
        self.__modelo =modelo
        self.__ano = ano
        self.__cor = cor
        self.__preco = preco

    def get_marca(self):
        return self.__marca
    
    def set_marca(self, nova_marca):
        self.__marca =  nova_marca

    def get_modelo(self):
        return self.__modelo
    
    def set_modelo(self, novo_modelo):
        self.__modelo = novo_modelo

    def get_ano(self):
        return self.__ano
    
    def set_ano(self, novo_ano):
        self.__ano = novo_ano

    def get_cor(self):
        return self.__cor
    
    def set_cor(self, nova_cor):
        self.__cor = nova_cor

    def get_preco(self):
        return self.__preco
    
    def set_preco(self, novo_preco):
        self.__preco = novo_preco

# exemplo de uso de classe de carro 
meu_Carro = Carro('toyota','corolla',2020,'preto',50000)

# obtendo os valores dos atributos
print('marca',meu_Carro.get_marca())
print('modelo',meu_Carro.get_modelo())
print('ano',meu_Carro.get_ano())
print('cor',meu_Carro.get_cor())
print('preco',meu_Carro.get_preco())

#alterando valores dos atributos
meu_Carro.set_modelo('camry')
meu_Carro.set_ano(2021)
meu_Carro.set_cor('branco')
meu_Carro.set_preco(55000)


#verificando as alteracoes
print('novo modelo',meu_Carro.get_modelo())
print('novo ano',meu_Carro.get_ano())
print('nova cor',meu_Carro.get_cor())
print('novo preco',meu_Carro.get_preco())