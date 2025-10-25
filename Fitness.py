from dataclasses import dataclass
from typing import Literal, Optional

# Activity type
ActivityType = Literal['workout', 'run', 'walk', 'cycle', 'swim', 'yoga', 'other']

@dataclass
class Activity:
    id: str
    type: ActivityType
    name: str
    duration: int  # in minutes
    calories: int
    date: str
    notes: Optional[str] = None
    distance: Optional[float] = None  # in km

# Food type
MealType = Literal['breakfast', 'lunch', 'dinner', 'snack']

@dataclass
class Food:
    id: str
    name: str
    calories: int
    protein: float
    carbs: float
    fat: float
    quantity: float
    unit: str
    date: str
    mealType: MealType

# Goal type
GoalType = Literal['calories', 'workouts', 'steps', 'weight']
PeriodType = Literal['daily', 'weekly', 'monthly']

@dataclass
class Goal:
    id: str
    type: GoalType
    target: float
    current: float
    unit: str
    period: PeriodType

# UserProfile
@dataclass
class UserProfile:
    name: str
    age: int
