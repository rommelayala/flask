import requests


def data_cripto():
    # API de Binance para obtener precios
    url_binance = "https://api.binance.com/api/v3/ticker/price"

    try:
        response = requests.get(url_binance)
        response.raise_for_status()  # Lanza excepción si hay errores
        return response.json()  # Retorna los datos como JSON
    except requests.RequestException as e:
        print(f"Error al obtener datos: {e}")
        return {"error": "No se pudieron obtener los datos"}
