class Fighter:
    
    def __init__(self,name,type,speed,attack,life):
        
        self.name = name
        self.type = type
        self.speed = speed
        self.attack = attack
        self.life = life

    def attack(self):
        print(f'attack: {self.attack}')

    def swap(self):
        print('Swap')

'''
Main
'''

def main():

    F = Fighters()

    
    


if __name__ == "__main__":
    main()