# FindIt

**Número da Lista**: X<br>
**Conteúdo da Disciplina**: Grafos1<br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 19/0026758  |  Deivid Alves de Carvalho  |
| 19/0030879  |  João Pedro Moura Oliveira |

## Sobre 
- O objetivo é construir um gerador de labirinto e um solucionar de labirinto seguido de uma interface.
- O gerador de labirinto é criado utilizando a estrutura de um grafo com busca por uma DFS ou uma BFS. Quanto maior a profundidade do grafo, sua cor é alterada para melhor visualização da estrutura.
- O solucionador faz uma busca por DFS ou BFS dentro da estrutura gerada buscando pelo nó de saída, quando achado é feito um backtrack até o inicio demonstrando o caminho feito pelo solucionador.

## Screenshots
### Gerando labirintos (dfs e bfs)
<p>
    <img src="assets/dfsMaze.gif" width="450" height="450" />
    <img src="assets/bfsMaze.gif" width="450" height="450" />
</p>

### Resolvendo labirintos (dfs em uma bfs e bfs em uma dfs)
<p>
    <img src="assets/dfsSolver.gif" width="450" height="450" />
    <img src="assets/bfsSolver.gif" width="450" height="450" />
</p>

## Instalação 
**Linguagem**: Python<br>
**Framework**: Pygame<br>
 
## Uso 
```bash
# Primeiro baixe o Pygame
$ pip install pygame

# Rode a main
$ python src/main.py
```
Após dar run na main.py, é necessário escolher a opção de gerador e solucionador do labirinto.
