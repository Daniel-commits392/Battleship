#TASK 1: setting ariables
#Characters
wizard='Wizard'
elf='Elf'
human='Human'
#Hp
wizard_hp=70
elf_hp=100
human_hp=150
#damage
wizard_damage=150
elf_damage=100
human_damage=20
#dragon
dragon_hp=300
dragon_damage=50

#TASK 2 : prompting players
class User:
    def __init__(self,wizard,elf,human,wizard_hp,elf_hp,human_hp,wizard_damage,elf_damage,human_damage,dragon_hp,dragon_damage):
        self.wizard=wizard
        self.human=human
        self.elf=elf

        self.wizard_hp=wizard_hp
        self.elf_hp=elf_hp
        self.human_hp=human_hp

        self.wizard_damage=wizard_damage
        self.elf_damage=elf_damage
        self.human_damage=human_damage

        self.dragon_hp=dragon_hp
        self.dragon_damage=dragon_damage

    def  choose_character(self):
       while True:
        print('Choose your character')
        print('For this game, you have to chose one of these characters:')
        print(f'(1) {self.wizard}   HP: {self.wizard_hp},   Damage: {self.wizard_damage} ')
        print(f'(2) {self.elf}      HP: {self.elf_hp} ,     Damage: {self.elf_damage} ')
        print(f'(3) {self.human}    HP: {self.human_hp},    Damage: {self.human_damage}')
        
        character_choice=input('Choose either 1, 2 or 3 : ')

        if character_choice == '1':
         self.character=self.wizard
         self.character_hp=self.wizard_hp
         self.character_damage=self.wizard_damage
         print(f'You have chosen {self.character} Your HP:{self.character_hp} Your Damage: {self.character_damage}')
         break

        elif character_choice=='2':
           self.character=self.elf
           self.character_hp=self.elf_hp
           self.character_damage=self.elf_damage
           print(f'You have chosen {self.character} Your HP:{self.character_hp} Your Damage: {self.character_damage}')
           break

        elif character_choice=='3':
            self.character=self.human
            self.character_hp=self.human_hp
            self.character_damage=self.human_damage
            print(f'You have chosen {self.character} Your HP:{self.character_hp} Your Damage: {self.character_damage}')
            break
        else:
           print('Wrong choice.Choose as instructed') 


       while True:
          
          self.dragon_hp = self.dragon_hp-self.character_damage
          print(f'The {self.character} has damaged the 🐉dragon🐉. ')

          if self.dragon_hp <=0:
             print('The 🐉dragon🐉 has lost the battle!')
             break
          
          self.character_hp = self.character_hp - self.dragon_damage
          print(f'The 🐉dragon🐉 has damaged the {self.character}')

          if self.character_hp<=0:
            print(f'The {self.character} has lost the battle!')
            break
               
        
player = User(wizard, elf, human, wizard_hp, elf_hp, human_hp, wizard_damage, elf_damage, human_damage, dragon_hp, dragon_damage)
player.choose_character()

        
      

