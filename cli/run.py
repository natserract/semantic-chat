from extensions.storage.supabase_storage import SupabaseStorage
from extractor.extractor_processor import ExtractorProcessor
from helpers.file import get_base_path

if __name__ == "__main__":
    # supabase_storage = SupabaseStorage()
    # response = supabase_storage.client.table('documents').select("*").execute()
    # print("Hello", response)

    run_extractor = ExtractorProcessor()
    markdown_path = get_base_path('datasets/archive.md')
    print(run_extractor.extract(markdown_path))
