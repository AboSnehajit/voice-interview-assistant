import asyncio
from app.db.postgres import connect_postgres

async def test():
    
    conn=await connect_postgres()
    
    result=await conn.fetch("SELECT 1")
    
    print("PostGres  working ", result)
    
    await conn.close()
    
asyncio.run(test())    