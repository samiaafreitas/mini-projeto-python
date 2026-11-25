# PontoVerde - coleta seletiva comunitária

Mini-projeto do bloco de Python. É um programa de terminal, orientado a objetos, para uma central de reciclagem de bairro controlar o material que recebe dos moradores e o que manda para as cooperativas.

## O problema

Em muito ponto de coleta comunitário o controle é feito no caderno: quem trouxe o quê, quanto tem guardado, quando dá pra mandar pra cooperativa. Aí acontece de o depósito lotar sem ninguém perceber, de eletrônico ir junto com o resto e ser recusado, ou de não ter nenhum número pra mostrar quanto o bairro reciclou no mês.

O programa resolve isso de um jeito simples:

- registra cada entrega (morador, ponto de coleta, tipo de material, peso e se veio limpo);
- separa o que precisa de triagem antes de ir pro estoque (material sujo e todo eletrônico);
- controla o estoque por peso e avisa quando a central passa de 75% e de 90% da capacidade, recusando entregas que não cabem;
- monta lotes por tipo de material e manda pra uma cooperativa, que só recebe eletrônico se for habilitada;
- mostra relatório com total recebido, total enviado, volume estimado reciclado e quem mais entregou.

Os materiais aceitos são papel, plástico, vidro, metal e eletrônicos.

## Como rodar

Precisa de Python 3.10 ou mais novo (o menu usa `match/case`). Não tem nenhuma biblioteca externa.

```
git clone https://github.com/samiaafreitas/mini-projeto-python.git
cd mini-projeto-python
python main.py
```

No Linux/Mac pode ser `python3 main.py`.

O programa já começa com dois pontos de coleta, duas cooperativas e dois moradores cadastrados, pra dar pra testar direto. Os dados ficam só na memória, então somem quando o programa fecha.

Um teste rápido pelo menu:

1. opção 2, registrar uma entrega de plástico sujo;
2. opção 5, ver que ele está na triagem e não no estoque;
3. opção 3, fazer a triagem;
4. opção 4, mandar o lote de plástico pra Coopagres;
5. opção 6, ver o relatório.

## Como o código está organizado

- `materiais.py`: `MaterialReciclavel` e as filhas `Papel`, `Plastico`, `Metal`, `Vidro` e `Eletronico`
- `participantes.py`: `Morador`, `PontoColeta`, `CooperativaDestino`, `Entrega` e `Lote`
- `central.py`: `CentralReciclagem`, que cuida do estoque, triagem, lotes e relatório
- `main.py`: menu e leitura do que o usuário digita

Onde aparece cada conteúdo do bloco:

- Herança: cada material herda de `MaterialReciclavel`. O `Vidro` estende `cuidados()` chamando o método da classe mãe e acrescentando o aviso de quebra. O `Eletronico` sobrescreve `precisa_triagem()` e `fazer_triagem()`, porque ele sempre passa por triagem, mesmo limpo.
- Polimorfismo: a central chama `material.precisa_triagem()`, `material.fazer_triagem()` e `material.volume_estimado()` sem saber qual é o tipo, e cada classe responde do seu jeito.
- Encapsulamento: peso, tipo, estoque e históricos são atributos com `_` e são acessados por métodos (`get_peso()`, `get_entregas()` etc).
- Parâmetro opcional: `peso_em_estoque(tipo=None)` devolve o total da central ou só de um tipo, que foi o jeito de "sobrecarga" que vimos pra Python.
- Laços, funções, condicionais, `match/case`, listas, dicionários e métodos de string (na validação do que é digitado).

## Sobre o volume estimado

O volume é só uma estimativa pra dar uma ideia do espaço que o material ocuparia no lixo. Cada classe tem um `litros_por_kg` (papel 8, plástico 20, vidro 2,5, metal 5, eletrônico 4). Usei valores aproximados de material solto, não é medida exata.

## O que dá pra melhorar

- salvar os dados em arquivo (JSON ou CSV) pra não perder quando fecha;
- triagem item por item, em vez de tudo de uma vez;
- relatório por mês.
