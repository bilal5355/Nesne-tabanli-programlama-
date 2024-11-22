import random
from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, name):
        self.name = name
        self.score = 0
    
    @abstractmethod
    def make_move(self):
        pass
    
    @abstractmethod
    def get_move(self):
        pass
    
    def win(self):
        self.score += 1

class ComputerPlayer(Player):
    def __init__(self, name="Bilgisayar"):
        super().__init__(name)
    
    @abstractmethod
    def make_move(self):
        pass

# 2. Alt Sınıfların Tanımlanması

class HumanPlayer(Player):
    def __init__(self, name):
        super().__init__(name)
    
    def make_move(self):
        print("\nSeçim yapın:")
        print("1. Taş\n2. Kağıt\n3. Makas")
        choice = input("Taş, Kağıt, Makas (1.2.3): ").strip().lower()
        if choice == '1':
            self._move = 'Taş'
        elif choice == '2':
            self._move = 'Kağıt'
        elif choice == '3':
            self._move = 'Makas'
        else:
            print("Geçersiz seçim taş olarak kabul edildi.")
            self._move = 'Taş'
    
    def get_move(self):
        return self._move

class RandomComputerPlayer(ComputerPlayer):
    def __init__(self, name="Bilgisayar"):
        super().__init__(name)
    
    def make_move(self):
        self._move = random.choice(['Taş', 'Kağıt', 'Makas'])
    
    def get_move(self):
        return self._move


def determine_winner(player_move, computer_move):
    if player_move == computer_move:
        return "Beraberlik!"
    
    winning_combos = {
        ('Taş', 'Makas'): "Taş, Makas'ı kırar. Kazandınız!",
        ('Kağıt', 'Taş'): "Kağıt, Taş'ı sarar. Kazandınız!",
        ('Makas', 'Kağıt'): "Makas, Kağıt'ı keser. Kazandınız!"
    }
    
    if (player_move, computer_move) in winning_combos:
        return winning_combos[(player_move, computer_move)]
    else:
        return f"{computer_move} {player_move}'i yener. Kaybettiniz."


def main():
    print("Melike Oyununa Hoşgeldiniz!")  # Oyunun adı değiştirildi
    player_name = input("Oyuncu adı girin: ").strip()
    computer_name = input("Bilgisayar adı girin: ").strip() or "Bilgisayar"  # Boş girilirse "Bilgisayar" olacak
  
    player = HumanPlayer(player_name)
    computer = RandomComputerPlayer(computer_name)

    game_history = []
    
    while True:
        print("\n--- Yeni Tur ---")
        player.make_move()  
        computer.make_move()  

        
        player_move = player.get_move()
        computer_move = computer.get_move()
        print(f"{player.name} seçimi: {player_move}")
        print(f"{computer.name} seçimi: {computer_move}")
        
    
        result = determine_winner(player_move, computer_move)
        print(result)

        if "Kazandınız" in result:
            player.win()
        elif "Kaybettiniz" in result:
            computer.win()

        print(f"\n{player.name}'ın Puanı: {player.score}")
        print(f"{computer.name}'ın Puanı: {computer.score}")
        
        
        game_history.append(f"{player.name}: {player_move} vs {computer.name}: {computer_move} -> {result}")

        
        continue_game = input("\nBir başka tur oynamak ister misiniz? (Evet/Hayır): ").strip().lower()
        if continue_game != 'evet':
            break


    print("\n--- Oyun Bitti ---")
    print(f"Final Skorları: {player.name}: {player.score} - {computer.name}: {computer.score}")
    print("\nOyun Geçmişi:")
    for entry in game_history:
        print(entry)
    
    print("Teşekkürler! Oynamayı tekrar bekleriz.")

if __name__ == "__main__":
    main()