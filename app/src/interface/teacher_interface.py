from abc import abstractmethod, ABC
from src.models.teacher_model import Teacher

class TeacherInterface(ABC):
    @abstractmethod
    def create_teacher(self, teacher: Teacher):
        pass

    @abstractmethod
    def get_teacher(self, id: int):
        pass

    @abstractmethod
    def get_all_teachers(self):
        pass

    @abstractmethod
    def update_teacher(self, teacher: Teacher):
        pass

    @abstractmethod
    def delete_teacher(self, teacher: Teacher):
        pass