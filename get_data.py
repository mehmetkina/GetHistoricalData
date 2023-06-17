import config
from binance.client import Client
import pandas as pd

# Binance API anahtarlarını config dosyasından al
api_key = config.API_KEY
api_secret = config.API_SECRET

# Binance istemcisini oluştur
client = Client(api_key, api_secret, requests_params={'timeout': 10})

# Tarih aralığı
start_date = "2022-01-01"
end_date = "2023-06-14"

# Kripto verilerini getir
def get_binance_data(start_date, end_date):
    klines = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1HOUR, start_date, end_date)
    df = pd.DataFrame(klines, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume', 'number_of_trades', 'taker_buy_base_volume', 'taker_buy_quote_volume', 'ignore'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df.set_index('timestamp', inplace=True)
    return df

# Verileri al ve CSV dosyasına kaydet
binance_data = get_binance_data(start_date, end_date)
binance_data.to_csv('BTCUSDT-1HOUR.csv')

# Verilerin başarıyla kaydedildiğini bildir
print("Veriler başarıyla kaydedildi.")
