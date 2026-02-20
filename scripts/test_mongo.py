from pymongo import MongoClient

uri = "mongodb+srv://bigdata:databig@cluster0.lqy5mbb.mongodb.net/?appName=Cluster0"

try:
    client = MongoClient(uri)
    print("Koneksi berhasil!")
    print(client.list_database_names())
except Exception as e:
    print("Koneksi gagal:", e)