import mysql.connector

# 1. Свързваме се с твоя MySQL сървър
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",      # паролата, която настроихме
    database="igri_db"       # базата данни, която направихме
)

cursor = connection.cursor()

# 2. Изпълняваме същата SQL заявка, която правеше в Workbench!
cursor.execute("SELECT * FROM igri WHERE platforma = 'PS4'")

# 3. Прибираме всички резултати и ги обхождаме с цикъл for (който вече знаеш)
games = cursor.fetchall()

print("Твоите игри за PS4 от Python:")
for game in games:
    print(f"ID: {game[0]} | Игра: {game[1]} | Платформа: {game[2]}")

# 4. Винаги затваряме връзката след работа
cursor.close()
connection.close()