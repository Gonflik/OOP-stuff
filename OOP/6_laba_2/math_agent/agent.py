from google.adk.agents.llm_agent import Agent
import math
def calculate_rectangle_area(width: float, height: float) -> float:
    """
    Обчислює площу прямокутника.
    
    Args:
        width: ширина прямокутника
        height: висота прямокутника
    
    Returns:
        float: площа прямокутника
    """
    return width * height

def calculate_circle_area(radius: float) -> float:
    """
    Обчислює площу кола.
    
    Args:
        radius: радіус кола
    
    Returns:
        float: площа кола
    """
    import math
    return math.pi * radius ** 2

def calculate_cube_volume(side: float) -> float:
    """
    Обчислює об'єм куба.
    
    Args:
        side: довжина ребра куба
    
    Returns:
        float: об'єм куба
    """
    return side ** 3

def calculate_triangle_area(side1: float, side2: float, side3: float) -> float:
    """
    Обчислює площу трикутника

    Args:
        side1: перша сторона трикутника
        side2: друга сторона трикутника
        side3: третя сторона трикутника

    Returns:
        float: S(площа трикутника)
    """
    p = (side1+side2+side3) / 2
    S = math.sqrt(p * (p - side1) * (p - side2) * (p - side3))
    return S

# Створюємо математичного агента
root_agent = Agent(
    model='gemini-2.5-flash',
    name='math_agent',
    description="Виконує математичні обчислення геометричних фігур.",
    instruction="""
    Ти експертний математичний асистент який допомагає з обчисленнями.
    У тебе є інструменти для обчислення площі прямокутника,площі трикутника площі кола та об'єму куба.
    Використовуй ці інструменти коли потрібно виконати розрахунки.
    Відповідай українською мовою та поясни хід обчислень.
    """,
    tools=[calculate_rectangle_area, calculate_circle_area, calculate_cube_volume, calculate_triangle_area],
)