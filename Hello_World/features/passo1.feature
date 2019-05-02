#language:pt

Funcionalidade: Pesquisa em site de viagens
Cenario:Pesquisar passagem para Salvador,sem data definida
Dado que estou no site do decolar.com
Quando pesquiso destino da viagem para Salvador
Então o resultado Salvador,Bahia,Brasil irá aparecer
E a opçao para nao escolher dia deve ser marcada
Entao o navegador clica no pesquisar
E o resultado de destino ira aparecer