import redis
import os
from dotenv import load_dotenv

load_dotenv()

r=redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=int(os.getenv("REDIS_PORT", "6379")),
    decode_responses=True
)



def test_redis():
    r.set("test_key","redis_working")
    
    return r.get("test_key")