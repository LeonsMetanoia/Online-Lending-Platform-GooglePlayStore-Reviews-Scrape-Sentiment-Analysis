from google_play_scraper import Sort, reviews
import pandas as pd

# Coba dengan app ID yang pasti ada review-nya
app_id = 'com.julofinance.juloapp'

# Ambil review
result, _ = reviews(
    app_id,
    lang='id',
    country='id',
    sort=Sort.NEWEST,
    count=1000,
)

# Jika hasil kosong, tampilkan pesan error
if not result:
    print("⚠️ Tidak ada review yang berhasil diambil. Periksa app ID atau koneksi internet.")
else:
    df = pd.DataFrame(result)
    print("\n✅ Kolom yang tersedia:", df.columns.tolist())

    df_clean = df[['userName', 'score', 'content', 'at']]
    df_clean.to_csv('Julo_reviews_1000.csv', index=False, encoding='utf-8-sig')
    print(f"\n✅ {len(df_clean)} review berhasil disimpan ke 'adakami_reviews.csv'")
