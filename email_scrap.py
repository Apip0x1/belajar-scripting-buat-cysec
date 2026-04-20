import requests
import re

url = input("input url target : ")

def EmailScrap(target_url):
    try:
        #kirim request ke web
        print(f"[*] Try to connect {target_url}...")
        response = requests.get(target_url, timeout=5)

        # Cari pola email menggunakan Regex
        # Pola ini mencari: teks + @ + teks + . + teks
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

        #ekstrak email dari response
        found_emails = re.findall(email_pattern, response.text)

        #hapus duplikat email
        unique_emails = set(found_emails)
        if unique_emails:
            print(f"\n[*] Ditemukan {len(unique_emails)} email :")
            for email in unique_emails:
                print(f" - {email}")
        else:
            print("\n[*] Tidak ditemukan email.")
    except Exception as e:
        print(f"eror: {e}") 
EmailScrap(url)