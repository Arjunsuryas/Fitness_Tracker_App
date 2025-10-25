import json
import asyncio
from pathlib import Path
from dataclasses import dataclass, asdict
from typing import List

# Define your data types
@dataclass
class Activity:
    id: str
    name: str
    duration_minutes: int

@dataclass
class Food:
    id: str
    name: str
    calories: int

@dataclass
class UserProfile:
    id: str
    name: str
    age: int

# Storage file paths
STORAGE_PATH = Path("./storage")
STORAGE_PATH.mkdir(exist_ok=True)

STORAGE_KEYS = {
    "ACTIVITIES": STORAGE_PATH / "fitness_activities.json",
    "FOODS": STORAGE_PATH / "fitness_foods.json",
    "PROFILE": STORAGE_PATH / "fitness_profile.json",
}

class StorageService:
    @staticmethod
    async def _read_file(file_path: Path):
        if not file_path.exists():
            return []
        try:
            async with aiofiles.open(file_path, "r") as f:
                content = await f.read()
                return json.loads(content)
        except Exception as e:
            print(f"Error reading {file_path.name}: {e}")
            return []

    @staticmethod
    async def _write_file(file_path: Path, data):
        try:
            async with aiofiles.open(file_path, "w") as f:
                await f.write(json.dumps(data, indent=2))
        except Exception as e:
            print(f"Error writing {file_path.name}: {e}")

    # Activities
    @staticmethod
    async def get_activities() -> List[Activity]:
        data = await StorageService._read_file(STORAGE_KEYS["ACTIVITIES"])
        return [Activity(**item) for item in data]

    @staticmethod
    async def save_activity(activity: Activity):
        activities = await StorageService.get_activities()
        existing_index = next((i for i, a in enumerate(activities) if a.id == activity.id), None)
        if existing_index is not None:
            activities[existing_index] = activity
        else:
            activities.append(activity)
        await StorageService._write_file(STORAGE_KEYS["ACTIVITIES"], [asdict(a) for a in activities])
