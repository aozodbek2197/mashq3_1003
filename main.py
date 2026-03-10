# 1-masala
class Song:
    def __init__(self, name: str, artist: str, duration: int):
        if duration < 0:
            raise ValueError("Davomiylik manfiy bo'lishi mumkin emas")

        self.__name = name
        self.__artist = artist
        self.__duration = duration

    @property
    def name(self):
        return self.__name

    @property
    def artist(self):
        return self.__artist

    @property
    def duration(self):
        return self.__duration

    def __str__(self):
        return f"{self.__name} - {self.__artist} ({Player.format_time(self.__duration)})"


class Player:
    total_plays = 0

    def __init__(self):
        self.__current_song = None
        self.__queue = []
        self.__favorites = []

    def add_song(self, song: Song):
        self.__queue.append(song)

    def add_favorite(self, song: Song):
        self.__favorites.append(song)

    def show_queue(self):
        if not self.__queue:
            print("Navbat bo'sh")
            return

        for i, song in enumerate(self.__queue, 1):
            print(i, song)

    def next_song(self):
        if not self.__queue:
            print("Navbat bo'sh")
            return None

        self.__current_song = self.__queue.pop(0)
        return self.__current_song

    @staticmethod
    def format_time(seconds: int) -> str:
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes}:{seconds:02}"

    def play(self):
        raise NotImplementedError("Farzand klasslarda yozilishi kerak")


class OnlinePlayer(Player):

    def play(self, quality: str = "320kbps"):
        song = self.next_song()

        if song:
            Player.total_plays += 1
            print(f"Online play: {song}")
            print(f"Sifat: {quality}")


class OfflinePlayer(Player):

    def play(self, path: str):
        song = self.next_song()

        if song:
            Player.total_plays += 1
            print(f"Offline play: {song}")
            print(f"Fayl joyi: {path}")


s1 = Song("Believer", "Imagine Dragons", 204)
s2 = Song("Perfect", "Ed Sheeran", 260)

online = OnlinePlayer()
offline = OfflinePlayer()

online.add_song(s1)
offline.add_song(s2)

online.play("256kbps")
offline.play("D:/music/")

print("Jami tinglanishlar:", Player.total_plays)
# 2-masala
from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: int
    group: str
    average_score: float

    def has_scholarship(self):
        return self.average_score >= 4.5


s = Student("Ali", 20, "CS-101", 4.7)

print(s.has_scholarship())
# 3-masala
from dataclasses import dataclass

@dataclass
class Book:
    name: str
    author: str
    pages: int
    price: float

    def apply_discount(self):
        self.price = self.price * 0.9


b = Book("Python", "Guido", 300, 100)

b.apply_discount()

print(b.price)
# 4-masala
from dataclasses import dataclass

@dataclass
class Car:
    brand: str
    model: str
    year: int
    speed: int

    def increase_speed(self):
        self.speed += 10

    def decrease_speed(self):
        self.speed -= 10


c = Car("Toyota", "Camry", 2020, 60)

c.increase_speed()
print(c.speed)

c.decrease_speed()
print(c.speed)
# 5-masala
from dataclasses import dataclass

@dataclass
class UserProfile:
    username: str
    email: str
    password: str
    last_login: str

    def is_password_valid(self):
        return len(self.password) > 8


u = UserProfile("ali123", "ali@mail.com", "password123", "2026-03-07")

print(u.is_password_valid())
# 6-masala
from dataclasses import dataclass

@dataclass
class Product:
    name: str
    quantity: int
    price: float

    def total_price(self):
        return self.quantity * self.price


p = Product("Telefon", 2, 500)

print(p.total_price())
