from abc import abstractmethod, ABC
from src.models.student_model import Student

class StudentInterface(ABC):
    @abstractmethod
    def create_student(self, student: Student):
        pass

    @abstractmethod
    def get_student(self, id: int):
        pass

    @abstractmethod
    def get_all_students(self):
        pass

    @abstractmethod
    def update_student(self, student: Student):
        pass

    @abstractmethod
    def delete_student(self, student: Student):
        pass