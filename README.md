

# Labirinto Secreto

**Número da Lista**: X  
**Conteúdo da Disciplina**: Grafos 1  

## 👨‍💻 Alunos
| Matrícula | Aluno |
| --------- | ------------------------------- |
| 20/0060783 | Ana Beatriz W. Massuh |
| 21/1063194 | Lucas Victor Ferreira de Araújo |

---

## 🧠 Sobre o Projeto

**Labirinto Secreto** é um jogo interativo feito em Python com Pygame, desenvolvido para ilustrar o funcionamento de algoritmos de **busca em grafos** em um labirinto gerado dinamicamente.

Você pode:
- Jogar manualmente até encontrar a saída;
- Assistir a busca automática usando **BFS (Busca em Largura)**;
- Assistir a busca usando **DFS (Busca em Profundidade)**;
- Visualizar os caminhos percorridos e o nó final da busca.

---

## 🎥 Demonstração

<p align="center">
  <a href="https://youtu.be/9HX3TL2cAvw">
    <img src="https://img.youtube.com/vi/9HX3TL2cAvw/0.jpg" alt="Labirinto Secreto - Jogo Interativo com Algoritmos de Busca em Grafos" width="560" height="315"/>
  </a>
</p>

<p align="center">
  <sub>Fonte: <a href="https://github.com/Lucas13032003">Lucas Víctor</a> e <a href="https://github.com/AnaBeatrizMassuh">Ana Beatriz W. Massuh</a>, 2025</sub>
</p>

---

## 🖼️ Screenshots

<!-- Imagem redimensionada -->
<p align="center">
  <img src="https://github.com/projeto-de-algoritmos-2025/Grafos1_LabirintoSecreto/blob/main/assets/img/menu.png?raw=true" alt="Descrição da imagem" width="400"/>
</p>

<!-- Fonte com link -->
<p align="center">
  <sub>Fonte: <a href="https://github.com/Lucas13032003">Lucas Víctor</a> e <a href="https://github.com/AnaBeatrizMassuh">Ana Beatriz W. Massuh</a>, 2025</sub>
</p>


## ⚙️ Instalação

**Linguagem**: Python 
**Biblioteca**: [Pygame](https://www.pygame.org/)  

### 📦 Pré-requisitos

Certifique-se de ter o Python 3 instalado. Em seguida, instale as dependências com:

```bash
pip install pygame
```

### 🔽 Clonando o Repositório

```bash
https://github.com/projeto-de-algoritmos-2025/Grafos1_LabirintoSecreto.git

cd labirinto-secreto
```

---

## ▶️ Como Usar

Execute o projeto com:

```bash
python3 main.py
```

No menu principal, escolha:
- **Jogar**: Controle manual até a saída;
- **BFS**: Executar busca automática em largura;
- **DFS**: Executar busca automática em profundidade;
- **Sair**: Encerrar o jogo.

---

## 📁 Estrutura do Projeto

```bash
.
├── busca.py         # Algoritmos de busca (BFS e DFS)
├── grafo.py         # Estrutura do grafo e funções de manipulação
├── config.py        # Cores, dimensões e constantes do jogo
├── main.py          # Arquivo principal da aplicação
├── assets/          # Imagens 
└── README.md
```

---

## ✨ Extras

- O labirinto é gerado aleatoriamente a cada execução.
- O jogador, algoritmos e armadilhas são representados visualmente.
- Ideal para aprendizado interativo de grafos.
- Interface retrô e minimalista.

