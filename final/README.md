## `data`

/data/interim/hero_data.csv  
/data/interim/player_data.csv  
Tabelas descrevem informações associadas a heróis e players, respectivamente.

/data/processed/match_data.csv  
/data/processed/graph_data.csv  
/data/processed/performance_data.csv  
/data/processed/hero_role_data.csv  
Tabelas descrevem informações de partidas públicas, relações entre jogadores que jogam juntos, performance desses jogadores e papel de heróis, respectivamente.

## `notebooks`

/notebooks/QUERIE-SQL.ipynb   
Notebook descreve as funções de taxa de winrate de herói e jogador.

## `src`

/src/graph_data.py  
/src/hero_data.py  
/src/match_data_request.py  
/src/performance_data_request.py  
/src/player_data_request.py  

Scripts definem criação de banco de dados específicos.
Para rodar os scripts basta que toda a pasta src esteja salva na máquina local.

## `assets`

### Modelo conceitual
![modelo_conceitual](assets/conceitual.png)  

### Modelo lógico  
![modelo_logico](assets/logico.png)  

# Modelo para Apresentação da Entrega Prévia do Projeto

# Projeto `<Dota2Analysis>`

# Equipe - `D2A`
* `Hugo Carvalho de Almeida Navarro` - `198893`
* `Matheus Augusto da Silva Cândido` - `241640`
* `Felipe Pacheco Manoel` - `215347`


## Resumo do Projeto
Criação de um dataset baseado em informações retiradas diretamente do jogo DOTA 2, e posterior análise desse dataset.  
 Com o crescimento constante dos eSports ao redor do mundo, o cenário tende a ser cada vez mais competitivo e disputado. Assim, junto com esses jogos, cresce a necessidade de ferramentas capaz de prover insights aprofundados que fornecam algum tipo de vantagem ao jogador e a equipe. Como objeto de estudo, vimos no DOTA 2 um ambiente rico em informações públicas que podem ser analisadas afim de atingirmos o objetivo citado.

## Slides da Apresentação
[Slides final](slides/final.pdf)

## Modelo Conceitual

![modelo_conceitual](assets/conceitual.png)  

## Modelos Lógicos

![modelo_logico](assets/logico.png)  
> Coloque aqui os modelos lógicos dos bancos de dados relacionados aos modelos conceituais. Para o modelo relacional, sugere-se o formato a seguir. Para outros modelos lógicos, sugere-se aqueles apresentados em sala.

> Exemplo de modelo lógico relacional
~~~
PESSOA(_Código_, Nome, Telefone)
ARMÁRIO(_Código_, Tamanho, Ocupante)
  Ocupante chave estrangeira -> PESSOA(Código)
~~~

> Para o modelo de grafos de propriedades, utilize este
> [modelo de base](https://docs.google.com/presentation/d/10RN7bDKUka_Ro2_41WyEE76Wxm4AioiJOrsh6BRY3Kk/edit?usp=sharing) para construir o seu.
> Coloque a imagem do PNG do seu modelo lógico como ilustrado abaixo (a imagem estará na pasta `image`):
>
> ![Modelo Lógico de Grafos](images/modelo-logico-grafos.png)

> Você pode usar um grafo ilustrando as classes, como este:
> ![Modelo Lógico de Grafos de Conhecimento](images/grafo-conhecimento-classes.png)
>
> Além de outro com exemplo de instâncias, como este:
> ![Modelo Lógico de Grafos](images/grafo-conhecimento-exemplo.png)

> Para modelos hierárquicos (XML e JSON), utilize um formato
> conforme o abaixo:

> ![Modelo Lógico Hierárquico](images/modelo-logico-hierarquico.png)

## Dataset Publicado

título | link | breve descrição
----- | ----- | -----
`<match_data.csv>` | `<./data/processed/match_data.csv>` | `<O arquivo contém uma série de informações referentes à partidas públicas>`
`<performance_data.csv>` | `<./data/processed/performance_data.csv>` | `<O arquivo contém uma série de informações referentes a performance de jogadores de partidas já visitadas>`
`<hero_data_winrate.csv>` | `<./data/processed/hero_data_winrate.csv>` | `<O arquivo contém uma série de informações referentes à taxa de vitória de cada herói>`
`<player_data_winrate.csv>` | `<./data/processed/player_data_winrate.csv>` | `<O arquivo contém uma série de informações referentes a taxa de vitórias de um dado jogador>`
`<hero_role_data.csv>` | `<./data/processed/hero_role_data.csv>` | `<O arquivo contém uma série de informações referentes a heróis e sua função>`
`<graph_data.csv>` | `<./data/interim/graph_data.csv>` | `<O arquivo contém informações referentes a duplas de jogadores que se encontram em uma dada partida>`
`<hero_data.csv>` | `<./data/interim/hero_data.csv>` | `<O arquivo contém uma série de informações referentes a heróis>`
`<player_data.csv>` | `<./data/interim/player_data.csv>` | `<O arquivo contém uma série de informações referentes a jogadores de partidas já visitadas>`

## Bases de Dados

título da base | link | breve descrição
----- | ----- | -----
`<OpenDota API>` | `<https://docs.opendota.com/>` | `<API pública consumida através do método GET para diversos filtros>`

## Detalhamento do Projeto
A contrução do dataset é feita a partir do consumo da API OpenDota API a partir do método GET, como descrito a seguir:

~~~python
api_response = requests.get('https://api.opendota.com/api/publicmatches?api_key=YOUR-API-KEY')

if api_response.status_code != 200:
    print("API Request Error - Public Matches not found")

    return 0
else:
    public_matches = api_response.json()
~~~

A resposta da API é transformada em uma estrutura de dados de mapa, formato json nesse caso, e lida para alimentação do respectivo csv linkado ao script.  
O script match_data_request.py irá criar nossa base de dados central onde, para cada partida visitada, os ids dos jogadores será explorado no API, assim como suas performances, criando assim novos datasets.  
~~~python
api_player_info = requests.get('https://api.opendota.com/api/players/' + Player_ID + '?api_key=549DB7F6A3D0BD71854A393A1334C7AC')
~~~
Link para arquivos src:  
`<https://github.com/FelipePM01/Dota2Analysis/tree/src_update/final/src>`  
`<./src>`  

* tratamento de dados recebidos por GET/
* agregação de dados fragmentados obtidos a partir de diferentes chamadas à API
* integração de dados de vários datasets para criação de queries
* transformação de dados para facilitar análise e pesquisa


## Evolução do Projeto
> Relatório de evolução, descrevendo as evoluções na modelagem do projeto, dificuldades enfrentadas, mudanças de rumo, melhorias e lições aprendidas. Referências aos diagramas, modelos e recortes de mudanças são bem-vindos.
> Podem ser apresentados destaques na evolução dos modelos conceitual e lógico. O modelo inicial e intermediários (quando relevantes) e explicação de refinamentos, mudanças ou evolução do projeto que fundamentaram as decisões.
> Relatar o processo para se alcançar os resultados é tão importante quanto os resultados.

## Perguntas de Pesquisa/Análise Combinadas e Respectivas Análises

> Apresente os resultados da forma mais rica possível, com gráficos e tabelas. Mesmo que o seu código rode online em um notebook, copie para esta parte a figura estática. A referência a código e links para execução online pode ser feita aqui ou na seção de detalhamento do projeto (o que for mais pertinente).

> Liste aqui as perguntas de pesquisa/análise e respectivas análises. Nem todas as perguntas precisam de queries que as implementam. É possível haver perguntas em que a solução é apenas descrita para demonstrar o potencial da base. Abaixo são ilustradas três perguntas, mas pode ser um número maior a critério da equipe.
>
### Perguntas/Análise com Resposta Implementada

> As respostas às perguntas podem devem ser ilustradas da forma mais rica possível com tabelas resultantes, grafos ou gráficos que apresentam os resultados. Os resultados podem ser analisados e comentados. Veja um exemplo de figura ilustrando uma comunidade detectada no Cytoscape:

> ![Comunidade no Cytoscape](images/cytoscape-comunidade.png)

#### Pergunta/Análise 1
> * Pergunta 1
>   
>   * Explicação sucinta da análise que será feita e conjunto de queries que
>     responde à pergunta.

#### Pergunta/Análise 2
> * Pergunta 2
>   
>   * Explicação sucinta da análise que será feita e conjunto de queries que
>     responde à pergunta.

#### Pergunta/Análise 3
> * Pergunta 3
>   
>   * Explicação sucinta da análise que será feita e conjunto de queries que
>     responde à pergunta.

### Perguntas/Análise Propostas mas Não Implementadas

#### Pergunta/Análise 1
* Pergunta 1
  
* Qual herói de uma certa função tem a maior winrate?

#### Pergunta/Análise 2
* Pergunta 2
   
* Qual item tem a maior winrate dado um determinado herói?

#### Pergunta/Análise 3
* Pergunta 3
  
* Qual a taxa de jogadores que saem das partidas antes de seu término?

#### Pergunta/Análise 4
* Pergunta 4
  
* Qual é o herói mais popular no geral? E em um rank específico?

#### Pergunta/Análise 5
* Pergunta 5
  
* Como se comporta a winrate de jogadores conforme o ouro ou experiencia por minuto  aumenta? Esse comportamento muda dependendo do rank?
