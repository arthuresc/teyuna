from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from core.config import settings

engine = create_async_engine(settings.DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
AsyncSessionLocal = async_sessionmaker(autocommit=False, autoflush=False, bind=engine)

#REVIEW Entender a função desse Base aqui
# Base = declarative_base()


async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()