from os import system

#Classes
class gameArea:
    global bg_list
    def __init__(self,size=3,render='C') -> None:
        self.size = size
        self.render = render
        #self.bg = [['  '+str(self.render)+'  ' for i in range(size)] for j in range(size)]
    def layout(self,bg_list):
        size = self.size
        system('cls')
        for i in range(size):
            print('     |','     |','     ')#print('#####|','#####|','#####')
            print(bg_list[i][0]+'|',bg_list[i][1]+'|',bg_list[i][2])#print(self.bg[i][0]+'|',self.bg[i][1]+'|',self.bg[i][2])
            print('     |','     |','     ')#print('#####|','#####|','#####')
            if i == 0 or i==1:
                print('___________________')
        #print('\n')
    def updateLayout(self,render,location,bg_list):
        bg_list[location[0]][location[1]] = '  '+render+'  '
        self.layout(bg_list)

class player(gameArea):
    global bg_list
    height = 2
    def __init__(self,name='Computer',character='O'):
        gameArea.__init__(self,render=' ',size=3)
        self.name = name
        self.character = character
    
    def ChangeCharacter(self):
        if self.character=='X':
            self.character = 'O'
        elif self.character=='O':
            self.character='X'
        return None

    def play(self):
        render = self.character
        location = list(map(lambda x:int(x),(input('location:').split(','))))
        self.updateLayout(render,location,bg_list)
        return None


#Initializing the Game area
startGame = gameArea(3)
render = ' '
bg_list = [['  '+render+'  ' for i in range(3)] for j in range(3)]
startGame.layout(bg_list)

#Using player class to create player for our game
CPU=player()
player1 = player('Bhavneet','X')

#playing
for i in range(9):
    print('\n')
    print(player1.name,player1.character)
    print(CPU.name,CPU.character)
    #print('\n\n')
    if i in [0,2,4,6,8]:
        CPU.play()
    else:
        player1.play()