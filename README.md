# Exercício  

## Do que se trara:
Uma API http simples feita em python utilizando o framework Flask e banco de dados MySQL.

## Descrição do exercício:
### Pessoa:  
* Será cadastrada previamente (pelo dev) com Nome, Cpf, Dívida, Score e Data de nascimento.  
* A dívida deve ser um valor em reais entre 0 ao +infinito (podendo ser com até duas casas decimais).  
* O score deverá ser um número de 0 até 1000, porém caso haja alguma dívida ativa, ela deverá ser menor de 1000.
* A pessoa poderá ter apenas uma única dívida, que quando paga, deverá ficar salva com o valor R$0,00. | 0.0 no banco.


### Birô:
* Terá acesso acesso as informações (Nome, Dívida, Score) de todas as pessoas maiores de 18 anos cadastradas
* Deverá ter uma rota para a pessoa requisitar o seu score e a sua dívida.
* Deverá ter uma rota para a pessoa pagar sua dívida. (A dívida não poderá ser paga parcelada ou apenas uma parte dela,
terá que ser a vista)
* Quando a dívida for paga o score deverá aumentar até o máximo (1000).