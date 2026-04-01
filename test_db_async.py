import asyncio
from database.session import AsyncSessionLocal
from sqlalchemy import text

async def test_connection():
  async with AsyncSessionLocal() as db:
    result = await db.execute(text("SELECT 1"))
    valor = result.scalar()
    print(f"✅ Banco OK (async), resultado: {valor}")
    
if __name__ == "__main__":
    asyncio.run(test_connection())