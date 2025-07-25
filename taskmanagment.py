
class Task: 
    id_counter = 1 #for assigning unique IDs

    def __init__(self, name, description, status):
        self.id = Task.id_counter
        Task.id_counter += 1
        self.name = name
        self.description = description
        self.status = status
    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Description: {self.description}, Status: {self.status}"

   
class TaskManager:
    def __init__(self):
        self.mylist = []

    def task_create(self, name, description, status):
        task = Task(name, description, status)
        self.mylist.append(task)
        return task

    def task_delete(self, task_id):
        for task in self.mylist:
            if task.id == task_id:
                self.mylist.remove(task)
                break  # Stop after finding and removing the task


    def show_list(self):
        for task in self.mylist:
            print(task)

manager = TaskManager()
manager.task_create("foodprepare", "preparing vegetable", True)
manager.task_create("wash dishes", "kitchen cleanup", False)

manager.show_list()  # Shows all tasks

manager.task_delete(1)  # Deletes the task with ID 1

print("After deletion:")
manager.show_list()



