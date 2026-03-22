from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Engine 
engine = create_engine("postgresql://postgres:EventConnectSanjay@db.cwejlpzhdljrcxzmmwgu.supabase.co:5432/postgres?sslmode=require" , pool_pre_ping=True)
# Session maker
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


from supabase import create_client
import uuid

SUPABASE_URL = "https://cwejlpzhdljrcxzmmwgu.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImN3ZWpscHpoZGxqcmN4em1td2d1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzE4MjgzMTcsImV4cCI6MjA4NzQwNDMxN30.sg54aSYZxy0ecnq1azjQkbsBwnVpaXNg-NSPrqnGXxI"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
