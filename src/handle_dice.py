from die import Die

class Dice_handler:
    dice = [[]]
    colors = [(255,100,0),(0,255,200),(0,255,100),(100,100,200),(0,255,255),(0,0,255)]
    numbers = ['?','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']

    def __init__(self, width, height, origin):
        self.width=width
        self.height=height
        self.origin=origin
        self.total=0

    def pos_constroler(self):
        y_distance=self.height/(len(self.dice)+1)
        y_o=self.origin[1]+y_distance
        for row in self.dice:
            if len(row)!=0:
                x_distance=self.width/(len(row)+1)
                x_o=self.origin[0]+ x_distance
                for die in row:
                    die.center= (x_o,y_o)
                    die.cordenates()
                    x_o+=x_distance
                y_o+=y_distance    

    def create_die(self, n_faces):
        index=0
        if n_faces!=4 and n_faces!=20:
            n_sides=n_faces-2
            index=(n_faces-4)//2
        elif n_faces==4:
            n_sides=3
            index=(n_faces-4)//2
        else:
            n_sides=5
            index=5
        tem_die = Die(n_sides,self.numbers,100,100,self.colors[index],n_faces)
        for row in self.dice:
            if len(row)!=4:
                row.append(tem_die)
                break
        else:
            self.dice.append([tem_die])           
        self.pos_constroler()

    def delete_die(self, die):
        for row in self.dice:
            if die in row:
                row.remove(die)
            if len(row)==0:
                self.dice.remove(row)    

    def roll_dice(self):
        self.total=0
        for row in self.dice:
            for die in row:
                self.total+=die.roll()
                
        return self.total               