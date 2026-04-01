# from database.session import SessionLocal
# from sqlalchemy import text

from sqlalchemy import create_engine, text

DATABASE_URL = "postgresql://admin:kamukuwaka@db:5432/fastapi_db"

engine = create_engine(DATABASE_URL)

with engine.connect() as conn:
  result = conn.execute(text("SELECT 1"))
  print("✅ Banco OK, resultado: ", result.scalar())

# try:
#   result = db.execute(text("SELECT 1"))
#   print("Conexão OK", result.scalar())
# except Exception as e:
#   print("Erro na conexão:", e)
# finally:
#   db.close()
