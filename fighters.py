class Fighter:
    
    def __init__(self,key,name,type,speed,attack,life):
        
        self.key = key
        self.name = name
        self.type = type
        self.speed = speed
        self.attack = attack
        self.life = life

    def Attack(self):
        print(f'attack: ')

    def swap(self):
        print('Swap')

'''
Main
'''

def main():

    F = Fighters()

    
    


if __name__ == "__main__":
    main()