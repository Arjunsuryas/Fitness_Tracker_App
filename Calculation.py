from dataclasses import dataclass
from typing import Literal

# Data types
ActivityType = Literal['workout', 'run', 'walk', 'cycle', 'swim', 'yoga', 'other']
ActivityLevel = Literal['sedentary', 'light', 'moderate', 'active', 'very_active']

@dataclass
class UserProfile:
    weight: float  # in kg
    height: float  # in cm
    age: int
    activityLevel: ActivityLevel

@dataclass
class Activity:
    type: ActivityType
    duration_minutes: float  # duration in minutes

# Fitness calculations
class FitnessCalculations:
    @staticmethod
    def calculate_bmr(profile: UserProfile) -> float:
        """
        Calculate BMR using Harris-Benedict formula (male by default)
        """
        return 88.362 + (13.397 * profile.weight) + (4.799 * profile.height) - (5.677 * profile.age)

    @staticmethod
    def calculate_daily_calories(profile: UserProfile) -> int:
        """
        Calculate daily calorie needs based on activity level
        """
        bmr = FitnessCalculations.calculate_bmr(profile)
        activity_multipliers = {
            "sedentary": 1.2,
            "light": 1.375,
            "moderate": 1.55,
            "active": 1.725,
            "very_active": 1.9,
        }
        multiplier = activity_multipliers.get(profile.activityLevel, 1.2)
        return round(bmr * multiplier)

    @staticmethod
    def calculate_calories_burned(activity: Activity, weight: float) -> float:
        """
        Calculate calories burned for a given activity and user weight
        """
        met_values = {
            "workout": 8.0,
            "run": 11.0,
            "walk": 3.8,
            "cycle": 9.5,
            "swim": 10.0,
            "yoga": 3.0,
            "other": 5.0,
        }
        met = met_values.get(activity.type, 5.0)
        duration_hours = activity.duration_minutes / 60
        # Calories burned = MET * weight(kg) * duration(hr)
        return round(met * weight * duration_hours, 2)

# Example usage
profile = UserProfile(weight=70, height=175, age=30, activityLevel="moderate")
activity = Activity(type="run", duration_minutes=45)

print(FitnessCalculations.calculate_bmr(profile))
print(FitnessCalculations.calculate_daily_calories(profile))
print(FitnessCalculations.calculate_calories_burned(activity, profile.weight))
