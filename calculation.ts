import { Activity, Food, UserProfile } from '@/types/fitness';

export const FitnessCalculations = {
  // Calculate BMR (Basal Metabolic Rate) using Harris-Benedict equation
  calculateBMR(profile: UserProfile): number {
    const { weight, height, age } = profile;
    // Using male formula as default, can be enhanced with gender selection
    return 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age);
  },

  // Calculate daily calorie needs
  calculateDailyCalories(profile: UserProfile): number {
    const bmr = this.calculateBMR(profile);
    const activityMultipliers = {
      sedentary: 1.2,
      light: 1.375,
      moderate: 1.55,
      active: 1.725,
      very_active: 1.9,
    };
    
    return Math.round(bmr * activityMultipliers[profile.activityLevel]);
  },

  // Calculate calories burned for activity
  calculateCaloriesBurned(activity: Activity, weight: number): number {
    const metValues = {
      workout: 8.0,
      run: 11.0,
      walk: 3.8,
      cycle: 9.5,
      swim: 10.0,
      yoga: 3.0,
      other: 5.0,
    };
    
    const met = metValues[activity.type];
    const hours = activity.duration / 60;
    return Math.round(met * weight * hours);
  },

  // Get today's activities
  getTodaysActivities(activities: Activity[]): Activity[] {
    const today = new Date().toDateString();
    return activities.filter(activity => 
      new Date(activity.date).toDateString() === today
    );
  },

  // Get today's foods
  getTodaysFoods(foods: Food[]): Food[] {
    const today = new Date().toDateString();
    return foods.filter(food => 
      new Date(food.date).toDateString() === today
    );
  },

  // Calculate total calories consumed today
  getTodaysCaloriesConsumed(foods: Food[]): number {
    const todaysFoods = this.getTodaysFoods(foods);
    return todaysFoods.reduce((total, food) => total + food.calories, 0);
  },

  // Calculate total calories burned today
  getTodaysCaloriesBurned(activities: Activity[]): number {
    const todaysActivities = this.getTodaysActivities(activities);
    return todaysActivities.reduce((total, activity) => total + activity.calories, 0);
  },

  // Calculate macronutrient totals
  getMacronutrients(foods: Food[]): { protein: number; carbs: number; fat: number } {
    const todaysFoods = this.getTodaysFoods(foods);
    return todaysFoods.reduce(
      (totals, food) => ({
        protein: totals.protein + food.protein,
        carbs: totals.carbs + food.carbs,
        fat: totals.fat + food.fat,
      }),
      { protein: 0, carbs: 0, fat: 0 }
    );
  },
};
