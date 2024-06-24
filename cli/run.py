from extensions.storage.supabase_storage import SupabaseStorage

if __name__ == "__main__":
    supabase_storage = SupabaseStorage()
    response = supabase_storage.client.table('documents').select("*").execute()
    print("Hello", response)
