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
        print('Choose your character')
        print('For this game, you have to chose one of these characters:')
        print(f'(1) {self.wizard}   HP: {self.wizard_hp},  Damage: {self.wizard_damage} ')
        print(f'(2) {self.elf}      HP: {self.elf_hp} ,    Damage: {self.elf_damage} ')
        print(f'(3) {self.human}    HP: {self.human_hp},   Damage: {self.human_damage}')
        character_choice=input('Choose your character : ')
        print(character_choice)

player = User(wizard, elf, human, wizard_hp, elf_hp, human_hp, wizard_damage, elf_damage, human_damage, dragon_hp, dragon_damage)
player.choose_character()


        
      

