class TodoList:
  def __init__(self):
    self.__tasks = []
  
  def add_task(self, task):
    if task in self.__tasks:
      print("Tarefa já cadastrada.")
      return
    self.__tasks.append(task)
    
  def remove_task(self, index):
    index = int(index) - 1
    if index < 0 or index >= len(self.__tasks):
      print("Índice inválido. Tente novamente.")
      return
    del self.__tasks[index]
  
  def show_tasks(self):
    if self.__tasks == []:
      print("Nenhuma tarefa cadastrada.")
      return
    for task in self.__tasks:
      print(task)
      
  def clear_tasks(self):
    self.__tasks.clear()
 
 
if __name__ == "__main__":
  todoList = TodoList()

  while True:
    print("Menu:")
    print("1. Adicionar tarefa")
    print("2. Remover tarefa")
    print("3. Mostrar tarefas")
    print("4. Limpar lsita de tarefas")
    print("5. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
      task = input("Digite a tarefa: ")
      todoList.add_task(task)
    elif opcao == "2":
      task = input("Digite o número da tarefa para remover: ")
      todoList.remove_task(task)
    elif opcao == "3":
      todoList.show_tasks()
    elif opcao == "4":
      todoList.clear_tasks()
    elif opcao == "5":
      break
    else:
      print("Opção inválida. Tente novamente.")
