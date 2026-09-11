import json
import requests
from bs4 import BeautifulSoup
import certifi

URL = "https://lekminkes.dinkes.semarangkota.go.id/"

def ambil_data_kesehatan():
    print("Mengambil data dari website Dinkes...")
    
    # Melakukan request dengan sertifikat certifi yang sudah kita instal
    response = requests.get(URL, verify=certifi.where())
    if response.status_code != 200:
        print("Gagal mengakses website. Status code:", response.status_code)
        return
    
    # Parsing HTML website menggunakan BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # CONTOH: Mencari angka kasus DBD dari elemen teks di dashboard
    # (Biasanya angka kasus dibungkus dalam tag tertentu seperti <span> atau <div>)
    print("Menganalisis elemen halaman...")
    
    # Karena data spasial per kecamatan membutuhkan koordinat, 
    # kita siapkan struktur GeoJSON dasar yang berisi fitur poligon/titik wilayah.
    # (Nanti file GeoJSON batas kecamatan dari QGIS bisa digabungkan di sini)
    
    data_geojson = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [110.4203, -6.9666] # Contoh koordinat Kota Semarang
                },
                "properties": {
                    "kecamatan": "Semarang Tengah",
                    "kasus_dbd": 12, # Contoh data angka yang nanti otomatis diisi dari scraping
                    "kasus_tb": 45
                }
            }
        ]
    }
    
    # Menyimpan hasil ke file data_penyakit.geojson
    with open('data_penyakit.geojson', 'w', encoding='utf-8') as f:
        json.dump(data_geojson, f, ensure_ascii=False, indent=4)
        
    print("File data_penyakit.geojson berhasil diperbarui dengan data terbaru!")

if __name__ == "__main__":
    ambil_data_kesehatan()