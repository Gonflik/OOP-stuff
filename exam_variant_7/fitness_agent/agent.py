from google.adk.agents import Agent

from .models import CardioExercise, StrengthExercise, Workout


def calculate_workout(exercises: list) -> dict:
    """
    Розраховує калорії для тренування.

    Args:
        exercises: Список словників з полями:
            - type (str): "cardio" або "strength"
            - name (str): назва вправи
            - duration_min (int): тривалість у хвилинах
            - intensity (float, опц.): інтенсивність 1.0–2.0 для кардіо
            - weight_kg (float, опц.): вага обтяження для силових вправ

    Returns:
        dict з ключами "exercises" (список з деталями) та "total_calories".
    """
    workout = Workout()

    for item in exercises:
        ex_type = item.get("type", "").lower()
        name = item.get("name", "Без назви")
        duration_min = int(item.get("duration_min", 0))

        if ex_type == "cardio":
            intensity = float(item.get("intensity", 1.0))
            exercise = CardioExercise(name=name, duration_min=duration_min, intensity=intensity)
        elif ex_type == "strength":
            weight_kg = float(item.get("weight_kg", 0.0))
            exercise = StrengthExercise(name=name, duration_min=duration_min, weight_kg=weight_kg)
        else:
            raise ValueError(f"Невідомий тип вправи: {ex_type!r}. Використовуйте 'cardio' або 'strength'.")

        workout.add(exercise)

    return workout.summary()

root_agent = Agent(
    name="fitness_trainer",
    model="gemini-2.5-flash",
    description="Персональний фітнес-тренер. Розраховує калорії та дає поради щодо навантаження.",
    instruction="""
Ти — досвідчений персональний фітнес-тренер.
Спілкуєшся виключно українською мовою.

Твої завдання:
1. Розраховувати кількість спалених калорій для тренувань за допомогою інструмента calculate_workout.
2. Аналізувати отримані результати та надавати конкретні рекомендації.
3. Враховувати тип вправ (кардіо / силові), інтенсивність та тривалість.
4. Давати практичні поради щодо коригування навантаження для досягнення цілей.

При розрахунку тренування завжди:
- Викликай інструмент calculate_workout з правильно сформованим списком вправ.
- Після отримання результатів коментуй кожну вправу.
- Давай загальну оцінку тренування та рекомендації.

Формули:
- Кардіо: duration_min × 8 × intensity (intensity: 1.0–2.0)
- Силові: duration_min × 5 + weight_kg × 0.5
""",
    tools=[calculate_workout],
)