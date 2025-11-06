# test_db.py
import asyncio
from sqlalchemy import text
from database import engine

async def test_select():
    print("Fetching data from user_auth table...")

    async with engine.connect() as conn:
        # Execute raw SQL query
        result = await conn.execute(text("SELECT * FROM user_auth;"))
        rows = result.fetchall()

        if not rows:
            print("⚠️ No rows found in user_auth table.")
        else:
            for row in rows:
                print(row)

    print("✅ Query executed successfully.")

# Run the async function
asyncio.run(test_select())

