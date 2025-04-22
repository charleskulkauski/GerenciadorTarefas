# Gerenciador de Tarefas

O **Gerenciador de Tarefas** é uma aplicação simples e eficiente para a organização e controle de tarefas diárias, com funcionalidades para adicionar, listar, alterar o status e excluir tarefas.

## Funcionalidades

- **Adicionar Tarefa**: Crie novas tarefas com título e descrição.
- **Listar Tarefas**: Exibe todas as tarefas, permitindo visualização detalhada.
- **Listar Tarefas por Status**: Filtra e exibe tarefas pendentes ou concluídas.
- **Alterar Status**: Altere o status de uma tarefa entre "Pendente" e "Concluída".
- **Excluir Tarefa**: Exclua tarefas selecionadas.

## Tecnologias Utilizadas

- **Python**: Linguagem principal utilizada para o desenvolvimento da aplicação.
- **PySide6**: Framework para a criação da interface gráfica no primeiro arquivo (GUI).
- **Terminal**: Interface de linha de comando no segundo arquivo (CLI).

## Interface Gráfica (GUI)

A aplicação possui uma interface gráfica desenvolvida com **PySide6** que permite interação fácil e rápida para gerenciamento de tarefas. Ela contém:

- **Lista de Tarefas**: Exibe as tarefas pendentes e concluídas.
- **Botões de Ação**:
  - **Adicionar**: Cria uma nova tarefa.
  - **Alterar Status**: Altera o status da tarefa selecionada.
  - **Excluir**: Exclui a tarefa selecionada.

### Exemplo de Tela

[Exemplo de Tela](https://prnt.sc/PFCxLlwXCKd5)

## Uso

### Como Rodar a Aplicação

#### Interface Gráfica (GUI)

1. Clone o repositório:
   ```bash
   git clone https://github.com/charleskulkauski/gerenciador_de_tarefas.git
   cd gerenciador_de_tarefas
   
2. Instale as dependências:
   ```bash
   pip install PySide6

3. Execute a aplicação
   ```bash
   python gerenciador_tarefas_gui.py

#### Interface de Linha de Comando (CLI)

1. Clone o repositório:
   ```bash
   git clone https://github.com/charleskulkauski/gerenciador_de_tarefas.git
   cd gerenciador_de_tarefas

2. Execute a aplicação
   ```bash
   python gerenciador_tarefas.py

## Licença

Distribuído sob a licença MIT. Veja LICENSE para mais informações.


