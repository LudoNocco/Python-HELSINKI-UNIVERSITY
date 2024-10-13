class Task:
    id_counter = 1

    def __init__(self, description: str, programmer: str, workload: int):
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.finished = False
        self.id = Task.id_counter
        Task.id_counter += 1

    def is_finished(self):
        return self.finished

    def mark_finished(self):
        self.finished = True

    def __str__(self):
        status = "FINISHED" if self.finished else "NOT FINISHED"
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {status}"

class OrderBook:
    def __init__(self):
        self.tasks = []

    def add_order(self, description: str, programmer: str, workload: int):
        self.tasks.append(Task(description, programmer, workload))

    def all_orders(self):
        return self.tasks

    def programmers(self):
        return list(set([task.programmer for task in self.tasks]))

    def mark_finished(self, id: int):
        task = next((task for task in self.tasks if task.id == id), None)
        if task is None:
            raise ValueError("Task with the given ID does not exist.")
        task.mark_finished()

    def finished_orders(self):
        return [task for task in self.tasks if task.is_finished()]

    def unfinished_orders(self):
        return [task for task in self.tasks if not task.is_finished()]

    def status_of_programmer(self, programmer: str):
        tasks = [task for task in self.tasks if task.programmer == programmer]
        if not tasks:
            raise ValueError("No tasks found for the programmer.")
        
        finished_tasks = [task for task in tasks if task.is_finished()]
        unfinished_tasks = [task for task in tasks if not task.is_finished()]

        finished_count = len(finished_tasks)
        unfinished_count = len(unfinished_tasks)
        finished_workload = sum(task.workload for task in finished_tasks)
        unfinished_workload = sum(task.workload for task in unfinished_tasks)

        return (finished_count, unfinished_count, finished_workload, unfinished_workload)
