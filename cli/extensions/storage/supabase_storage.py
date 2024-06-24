from supabase import create_client, Client
from extensions.storage.base_storage import BaseStorage
from config import Config

class SupabaseStorage(BaseStorage):
   """Implementation for supabase storage.
    """
   def __init__(self):
      super().__init__()

      supabase_url = Config.SUPABASE_URL
      supabase_key = Config.SUPABASE_API_KEY
      self.client = create_client(supabase_url, supabase_key)


