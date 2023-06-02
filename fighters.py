class Fighter:
    
    def __init__(self,key,name,type,speed,attack,life):
        
        self.key = key
        self.name = name
        self.type = type
        self.speed = speed
        self.attack = attack
        self.life = life
            

    def Attack(self,fighter,defender):
        
        multiplier  = 1
        if fighter.type == 'paper':
            if defender.type == 'rock':
                multiplier =2
            if defender.type == 'scissors':
                multiplier = 0.5
        if fighter.type == 'rock':
            if defender.type == 'scissors':
                multiplier =2
            if defender.type == 'paper':
                multiplier = 0.5   
        if fighter.type == 'scissors':
            if defender.type == 'paper':
                multiplier =2
            if defender.type == 'rock':
                multiplier = 0.5     

        defender.life = defender.life - (fighter.attack*multiplier)
        


    


