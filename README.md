# PontoVerde

Mini-projeto do bloco de Python. É um programa de terminal pra uma central de reciclagem do bairro anotar o material que recebe (papel, plástico e vidro) e mandar pra cooperativa quando junta bastante.

## Arquivos

- `materiais.py`: classe `Material` e as filhas `Papel`, `Plastico` e `Vidro`
- `central.py`: classe `Central`, que recebe os materiais e guarda o estoque
- `main.py`: menu

Pra rodar: `python main.py`

## O que usei do bloco

- Herança: `Papel`, `Plastico` e `Vidro` herdam de `Material`
- Polimorfismo: cada material tem seu próprio `cuidados()`
- Encapsulamento: o peso fica em `_peso` e é lido com `get_peso()`
- Listas, laços, if/else e match/case
