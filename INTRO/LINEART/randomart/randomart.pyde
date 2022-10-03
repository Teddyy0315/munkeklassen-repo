
data = []

def setup ():
    size(500, 500)
        
def diagLft (x,y):
    line(x*25,y*25, x*25+25,y*25+25)
    
def diagRght (x,y):
    line(x*25+25,y*25, x*25,y*25+25)
    
def crossIn (x,y):
    diagRght(x,y)
    diagLft(x,y)
    
def draw ():
    pass
            
def keyPressed ():
    for x in range(20):
        for y in range(20):
            
            stroke(0)
            fill(int(random(100,255)),int(random(100,255)),int(random(100,255)))
        
            randInt = int(random(0,4))
            
            square(x * 25, y * 25, 25)    
            
            if(randInt == 1):
                crossIn(x,y)
            if(randInt == 2):
                diagLft(x,y)
            if(randInt == 3):
                diagRght(x,y)
                
def mousePressed ():
    x = int(mouseX / 25)
    y = int(mouseY / 25)
    
    fill(int(random(100,255)),int(random(100,255)),int(random(100,255)))
    
    square(x * 25, y * 25, 25)
    
    randInt = int(random(0,4))
    
    if(randInt == 1):
        crossIn(x,y)
    if(randInt == 2):
        diagLft(x,y)
    if(randInt == 3):
        diagRght(x,y)
    
    print(x,y)
    
    
                
                
           
