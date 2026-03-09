from dotenv import load_dotenv
import os 

load_dotenv()

print("Postgress DB ",os.getenv("POSTGRES_DB"))
print("Redis Host :  ",os.getenv("REDIS_HOST"))
