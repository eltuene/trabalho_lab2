from exercicio1 import TodoList

def test_add_task():
  todoList = TodoList()
  todoList.add_task("task1")
  todoList.add_task("task2")
  todoList.add_task("task3")
  assert todoList._TodoList__tasks == ["task1", "task2", "task3"]
  
def test_remove_task():
  todoList = TodoList()
  todoList.add_task("task1")
  todoList.add_task("task2")
  todoList.add_task("task3")
  todoList.remove_task(2)
  assert todoList._TodoList__tasks == ["task1", "task3"]
  
def test_clear_tasks():
  todoList = TodoList()
  todoList.add_task("task1")
  todoList.add_task("task2")
  todoList.add_task("task3")
  todoList.clear_tasks()
  assert todoList._TodoList__tasks == []