# Definição da classe Node para representar cada nó da lista ligada
class Node:
    def __init__(self, data):
        self.data = data  # Dado armazenado no nó
        self.next = None  # Ponteiro para o próximo nó

# Definição da classe LinkedList para representar a lista ligada
class LinkedList:
    def __init__(self):
        self.head = None  # Inicializa a cabeça da lista como None

    # Método para adicionar uma tarefa à lista
    def add_task(self, task):
        new_node = Node(task)  # Cria um novo nó com a tarefa
        new_node.next = self.head  # Aponta o próximo do novo nó para a cabeça atual
        self.head = new_node  # Atualiza a cabeça para o novo nó

    # Método para remover uma tarefa da lista
    def remove_task(self, task):
        temp = self.head  # Inicializa um ponteiro temporário na cabeça
        if temp is not None:
            if temp.data == task:  # Se a tarefa a ser removida está na cabeça
                self.head = temp.next  # Atualiza a cabeça para o próximo nó
                temp = None  # Remove o nó atual
                return
        while temp is not None:
            if temp.data == task:  # Encontra a tarefa a ser removida
                break
            prev = temp  # Mantém o nó anterior
            temp = temp.next  # Move para o próximo nó
        if temp == None:
            return
        prev.next = temp.next  # Remove o nó atual da lista
        temp = None  # Libera o nó atual

    # Método para exibir todas as tarefas na lista
    def display_tasks(self):
        temp = self.head  # Inicializa um ponteiro temporário na cabeça
        while temp:
            print(temp.data)  # Imprime o dado do nó atual
            temp = temp.next  # Move para o próximo nó

# Definição da classe Stack para representar uma pilha
class Stack:
    def __init__(self):
        self.stack = []  # Inicializa a pilha como uma lista vazia

    # Método para empilhar um item
    def push(self, item):
        self.stack.append(item)  # Adiciona o item ao topo da pilha

    # Método para desempilhar um item
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()  # Remove e retorna o item do topo da pilha
        return None

    # Método para verificar se a pilha está vazia
    def is_empty(self):
        return len(self.stack) == 0  # Retorna True se a pilha estiver vazia

# Definição da classe Queue para representar uma fila
class Queue:
    def __init__(self):
        self.queue = []  # Inicializa a fila como uma lista vazia

    # Método para enfileirar um item
    def enqueue(self, item):
        self.queue.append(item)  # Adiciona o item ao final da fila

    # Método para desenfileirar um item
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)  # Remove e retorna o item do início da fila
        return None

    # Método para verificar se a fila está vazia
    def is_empty(self):
        return len(self.queue) == 0  # Retorna True se a fila estiver vazia

# Exemplo de uso das classes definidas
tasks = LinkedList()
tasks.add_task("Estudar para a prova")
tasks.add_task("Comprar mantimentos")
tasks.add_task("Limpar a casa")

print("Lista de Tarefas:")
tasks.display_tasks()

tasks.remove_task("Comprar mantimentos")
print("\nLista de Tarefas após remover 'Comprar mantimentos':")
tasks.display_tasks()
