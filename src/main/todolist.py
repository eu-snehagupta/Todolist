class Todolist:

    def __init__(self):
        self.todolist = []

    def get_list(self):
        return self.todolist

    def add_to_list(self, task):
        self.todolist.append(task)
        return self.todolist

    def update_list(self, old_task, update_task):
        index = self.todolist.index(old_task)
        self.todolist[index] = update_task
        return self.todolist

    def remove_list(self):
        del self.todolist

    def remove_task_from_list(self, task):
        self.todolist.remove(task)



