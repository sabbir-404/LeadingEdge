import requests
import os

# ==========================
# SUPABASE CONFIG
# ==========================

SUPABASE_URL = "https://rehivhbkyaopgsvaibdu.supabase.co"
SUPABASE_ANON_KEY = "sb_publishable_GTOdd2NG9DJzPRHcPrrFeA_kNtv8YGO"

# Full path inside the bucket (IMPORTANT: must match storage exactly)
OBJECT_PATH = "portfolio-images/wedding/farabi-tisha/holud/001.jpg"

# ==========================
# BUILD URL
# ==========================

url = f"{SUPABASE_URL}/storage/v1/object/public/{OBJECT_PATH}"

headers = {
    "apikey": SUPABASE_ANON_KEY,
    "Authorization": f"Bearer {SUPABASE_ANON_KEY}",
    "Accept": "image/*",
    "User-Agent": "Supabase-Python-Debugger"
}

print("🔍 Requesting:")
print(url)
print()

# ==========================
# REQUEST
# ==========================

response = requests.get(url, headers=headers, stream=True)

print("Status Code:", response.status_code)
print("Content-Type:", response.headers.get("Content-Type"))
print("Content-Length:", response.headers.get("Content-Length"))

if response.status_code == 200:
    os.makedirs("downloads", exist_ok=True)
    file_path = "downloads/test.jpg"

    with open(file_path, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

    print("✅ Image downloaded successfully!")
    print("Saved as:", file_path)

else:
    print("❌ Failed to download image")
    try:
        print("Response JSON:", response.json())
    except Exception:
        print("Raw response:", response.text)
