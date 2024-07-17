
# Followed (following.txt) ve Takipçiler (followers.txt) dosyalarını oku
with open("../following.txt", "r", encoding="UTF-8") as file:
    following_list = file.read().splitlines()

with open("../followers.txt", "r", encoding="UTF-8") as file:
    followers_list = file.read().splitlines()

# Following listesinde olup Followers listesinde olmayan kişileri bul
not_following_back = [user for user in following_list if user not in followers_list]

# Sonuçları not_following_back.txt dosyasına yaz
with open("../not_following_back.txt", "w", encoding="UTF-8") as file:
    for user in not_following_back:
        file.write(user + "\n")

print(f"Toplam {len(not_following_back)} kişi sizi takip etmiyor.")
