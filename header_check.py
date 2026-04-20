import requests

target_url = input("input url : ")

def check_headers(url):
    try:
        response = requests.get(url, timeout=5)
        headers = response.headers

        print(f"\n--- Analisis Header untuk: {url} ---")

        security_headers = [
            'Content-Security-Policy', 
            'X-Frame-Options', 
            'X-Content-Type-Options'
        ]

        for h in security_headers:
            if h in headers:
                print(f"{h}: Ditemukan")
            else:
                print(f"{h}: None")

    except Exception as e:
        print(f"eror: {e}")
check_headers(target_url)