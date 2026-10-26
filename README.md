# Tasktracker

Um programa de terminal simples baseado no conceito Kanban, permitindo o gerenciamento de tarefas nas categorias TODO, DOING e DONE.

## Funcionalidades

* Adicionar novas tarefas em qualquer coluna.
* Editar o texto de tarefas existentes através do número de índice.
* Mover tarefas entre as colunas (por exemplo, de TODO para DOING).
* Limpar as tarefas de uma coluna específica ou de todo o quadro.
* Visualizar o quadro completo atualizado a cada ação executada.

## Como executar

1. Certifique-se de ter o Python instalado na sua máquina.
2. Salve o código do programa em um arquivo chamado `tasktracker.py`.
3. Abra o terminal (ou prompt de comando) do seu sistema ou no próprio VS Code.
4. Navegue até a pasta onde o arquivo foi salvo.
5. Execute o seguinte comando:

python tasktracker.py

## Guia de Execução Docker

Como construir a imagem
Para empacotar a aplicação e criar a receita estática, abra o terminal na raiz do repositório e execute:

```bash
docker build -t tasktracker-app .
```
Como rodar o container em modo isolado
Para iniciar a aplicação garantindo a alocação do terminal interativo diretamente na imagem, utilize:te:

```bash
docker run -it tasktracker-app
```
Como rodar via orquestração (Recomendado)
Para iniciar o sistema orquestrado com as variáveis corretas de entrada de dados já configuradas, execute:
```bash
docker compose run tasktracker-app
```