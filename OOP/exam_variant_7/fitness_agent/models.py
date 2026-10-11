from abc import ABC, abstractmethod


class Exercise(ABC):
    """Абстрактний клас для вправ."""

    def __init__(self, name: str, duration_min: int):
        self.name = name
        self.duration_min = duration_min

    @abstractmethod
    def calories_burned(self) -> float:
        """Повертає кількість спалених калорій."""
        pass

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, duration_min={self.duration_min})"


class CardioExercise(Exercise):
    """Кардіо вправа з коефіцієнтом інтенсивності (1.0–2.0)."""

    def __init__(self, name: str, duration_min: int, intensity: float = 1.0):
        super().__init__(name, duration_min)
        if not (1.0 <= intensity <= 2.0):
            raise ValueError("intensity має бути в діапазоні 1.0–2.0")
        self.intensity = intensity

    def calories_burned(self) -> float:
        return self.duration_min * 8 * self.intensity


class StrengthExercise(Exercise):
    """Силова вправа з вагою обтяження."""

    def __init__(self, name: str, duration_min: int, weight_kg: float = 0.0):
        super().__init__(name, duration_min)
        self.weight_kg = weight_kg

    def calories_burned(self) -> float:
        return self.duration_min * 5 + self.weight_kg * 0.5


class Workout:
    """Тренування — збирає вправи та рахує загальні калорії."""

    def __init__(self):
        self.__exercises: list[Exercise] = []

    def add(self, exercise: Exercise) -> None:
        if not isinstance(exercise, Exercise):
            raise TypeError("Можна додавати лише об'єкти Exercise")
        self.__exercises.append(exercise)

    def total_calories(self) -> float:
        return sum(ex.calories_burned() for ex in self.__exercises)

    def summary(self) -> dict:
        exercises_info = [
            {
                "name": ex.name,
                "type": ex.__class__.__name__,
                "duration_min": ex.duration_min,
                "calories": round(ex.calories_burned(), 2),
            }
            for ex in self.__exercises
        ]
        return {
            "exercises": exercises_info,
            "total_calories": round(self.total_calories(), 2),
        }
    
    @property
    def exercises(self) -> list:
        """Копія списку вправ — зовні не можна змінити внутрішній стан."""
        return list(self.__exercises)
    
    @property
    def exercise_count(self) -> int:
        """Кількість вправ у тренуванні."""
        return len(self.__exercises)