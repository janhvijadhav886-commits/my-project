import os
from dotenv import load_dotenv

# Load variables from .env if present
load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "ntro-darkweb-intel-dev-secret-key-2026")
    
    # Check standard and Next.js style Supabase environment variable names
    SUPABASE_URL = (
        os.getenv("SUPABASE_URL") or 
        os.getenv("NEXT_PUBLIC_SUPABASE_URL", "")
    ).strip()
    
    SUPABASE_KEY = (
        os.getenv("SUPABASE_KEY") or 
        os.getenv("NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY") or 
        os.getenv("NEXT_PUBLIC_SUPABASE_ANON_KEY") or 
        os.getenv("SUPABASE_ANON_KEY", "")
    ).strip()
    
    FLASK_ENV = os.getenv("FLASK_ENV", "development")
    DEBUG = os.getenv("DEBUG", "True").lower() in ("true", "1", "yes")
    PORT = int(os.getenv("PORT", 5000))
    
    # Check if live Supabase is active
    @classmethod
    def is_supabase_configured(cls) -> bool:
        return bool(
            cls.SUPABASE_URL 
            and cls.SUPABASE_KEY 
            and cls.SUPABASE_URL.startswith("http") 
            and not "your-project" in cls.SUPABASE_URL
        )
