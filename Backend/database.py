from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Engine 
engine = create_engine("postgresql://neondb_owner:npg_htm5iqz8cwlu@ep-fragrant-mouse-aikclkvf-pooler.c-4.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require" , pool_pre_ping=True)
# Session maker
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

