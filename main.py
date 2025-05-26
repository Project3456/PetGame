class Pet:
    def __init__(self, name, hunger, happiness):
        self.name = name
        self.hunger = hunger if isinstance(hunger, int) and 0 <= hunger <= 100 else 50
        self.happiness = happiness if isinstance(happiness, int) and 0 <= happiness <= 100 else 50
        

    def eat(self, amount):
        if isinstance(amount, int) and amount > 0:
            self.hunger = max(self.hunger - amount, 0)
        else:
            return "Ошибка: количество еды должно быть положительным числом!"
        return f"{self.name} поел, голод: {self.hunger}!"

    def play(self):
        self.happiness = min(self.happiness + 10, 100)
        return f"{self.name} счастлив: {self.happiness}!"
    
    def say(self):
        if self.happiness >= 50:
            return f"{self.name} говорит: Гав-Гав, я рад! "
        elif self.happiness >= 40:
            return f"{self.name} говорит: Может погуляем?"
        elif self.happiness >= 30:
            return f"{self.name} говорит: Я хочу играть!"
        elif self.happiness >= 20:
            return f"{self.name} говорит: Мне грустно,я хочу много гулять"
        elif self.happiness >= 10:
            return f"{self.name} говорит: Срочно гулять!"
        else:
            return f"{self.name} говорит: у меня депрессия!"
        

# test
bobik = Pet("Бобик", 80, 30)
print(bobik.happiness)  
print(bobik.eat(20))
print(bobik.say())
print(bobik.play())    

