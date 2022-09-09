def setup ():
    size(500, 500)
    background(0)
    
def draw ():
    pass
    
def keyPressed ():    
    background(0)
    for x in [0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500]:
        for y in [0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500]:
            
            stroke(255,255,255)

            side = int(random(1, 3))
            
            print(side)
            
            if (side == 1):
                line(x+5, y+5, x+45, y+5)
                line(x+5, y+45, x+5, y+5)
            
            if (side == 2):
                line(x+45, y+5, x+45, y+45)
                line(x+5, y+45, x+45, y+45)
                
