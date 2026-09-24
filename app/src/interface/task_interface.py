from abc import abstractmethod, ABC
from src.models.task_model import Task

class TaskInterface(ABC):
    @abstractmethod
    def create_task(self, task: Task):
        pass

    @abstractmethod
    def get_task(self, id: int):
        pass

    @abstractmethod
    def get_all_tasks(self):
        pass

    @abstractmethod
    def update_task(self, task: Task):
        pass

    @abstractmethod
    def update_task_by_id_and_student_id(self, task: Task):
        pass

    @abstractmethod
    def delete_task(self, id: int):
        pass

    @abstractmethod
    def delete_task_by_id_and_student_id(self, task: Task):
        pass