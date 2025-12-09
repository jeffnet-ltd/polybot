#!/usr/bin/env python3
"""
MongoDB Seeding Script for Module A1.7: Places in Town & Directions
Populates the lessons collection with the structured A1.7 module.
"""

import os
import sys
import asyncio
from pathlib import Path
from motor.motor_asyncio import AsyncIOMotorClient
from datetime import datetime

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

# MongoDB connection
MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "polybot_database")

# Import from main module data file to keep in sync
try:
    from a1_7_module_data import MODULE_A1_7_LESSONS
except ImportError:
    # Fallback if import fails (for testing)
    import sys
    sys.path.insert(0, str(Path(__file__).parent.parent))
    from a1_7_module_data import MODULE_A1_7_LESSONS

# Note: MODULE_A1_7_LESSONS is now imported from a1_7_module_data.py
# This ensures the seed script stays in sync with the main module data

async def seed_module_a1_7():
    """Seed Module A1.7 into MongoDB."""
    try:
        client = AsyncIOMotorClient(MONGO_URL, serverSelectionTimeoutMS=5000)
        db = client[DB_NAME]
        
        # Check connection
        await client.admin.command('ping')
        print("✅ Connected to MongoDB")
        
        # Insert or update module
        collection = db.modules  # New collection for structured modules
        
        # Check if module already exists
        existing = await collection.find_one({"module_id": "A1.7"})
        
        if existing:
            # Update existing module
            result = await collection.update_one(
                {"module_id": "A1.7"},
                {"$set": {**MODULE_A1_7_LESSONS, "updated_at": datetime.utcnow()}}
            )
            print(f"✅ Updated Module A1.7 (matched: {result.matched_count}, modified: {result.modified_count})")
        else:
            # Insert new module
            result = await collection.insert_one({
                **MODULE_A1_7_LESSONS,
                "created_at": datetime.utcnow(),
                "updated_at": datetime.utcnow()
            })
            print(f"✅ Inserted Module A1.7 (id: {result.inserted_id})")
        
        # Also update the lessons collection for backward compatibility
        # Store individual lessons for easy access
        lessons_collection = db.lessons
        for lesson in MODULE_A1_7_LESSONS["lessons"]:
            lesson_doc = {
                **lesson,
                "module_id": "A1.7",
                "created_at": datetime.utcnow(),
                "updated_at": datetime.utcnow()
            }
            await lessons_collection.update_one(
                {"lesson_id": lesson["lesson_id"]},
                {"$set": lesson_doc},
                upsert=True
            )
            print(f"  ✓ Upserted lesson: {lesson['lesson_id']} - {lesson['title']}")
        
        print(f"\n🎉 Module A1.7 seeding complete!")
        print(f"   - Module document in 'modules' collection")
        print(f"   - {len(MODULE_A1_7_LESSONS['lessons'])} lessons in 'lessons' collection")
        
        client.close()
        
    except Exception as e:
        print(f"❌ Error seeding Module A1.7: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    print("=" * 60)
    print("PolyBot MongoDB Seeding Script - Module A1.7")
    print("=" * 60)
    asyncio.run(seed_module_a1_7())
