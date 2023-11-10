import requests


API_KEY = '309947f7514ba097f09fdcb57949059f'


def havanasil(il):
    base_url = "http://api.weatherstack.com/current"
    complete_url = f"{base_url}?access_key={API_KEY}&query={il}"

    response = requests.get(complete_url)

    data = response.json()

    if "current" in data:
        current_data = data["current"]
        sicaklik = current_data["temperature"]
        nem = current_data["humidity"]
        havadurumu = current_data["weather_descriptions"][0]

        print(f"Hava durumu: {havadurumu}")
        print(f"Sıcaklık: {sicaklik} °C")
        print(f"Nem: {nem}%")
    else:
        print("Şehir bulunamadı ya da hava durumu bilgileri alınamadı.")


if __name__ == "__main__":
    il = input("Hangi ilin hava durumunu öğrenmek istediğinizi girin: ")
    havanasil(il)