from models.cliente import Cliente
from models.conta import Conta


arthur: Cliente = Cliente('Arthur Oliveira', 'arthuroliveira@gmail.com', '123.645.262-55', '05/07/1991')
felipe: Cliente = Cliente('Felipe Silva', 'felipesilva@gmail.com', '442.145.567-15', '15/10/1951')

# print(arthur)
# print(felipe)

conta_arthur: Conta = Conta(arthur)
conta_felipe: Conta = Conta(felipe)

# print(conta_arthur)
# print(conta_felipe)
