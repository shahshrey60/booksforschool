import pygame,random,time
import pandas as pd
from pygame.locals import *
pygame.init()
from datetime import datetime
dt = datetime.now()

xi = dt.weekday()
class button():
    def __init__(self, color, x,y,width,height, text=''):
        global w
        w=width
        global h
        h=height
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            #pygame.draw.rect(win, outline, (self.x,self.y,self.width,self.height),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont('comicsansms', 20)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))
            
    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
                
        return False
def textwrite(you_said,cl,f_size,x_co,y_co):
    font = pygame.font.Font('freesansbold.ttf', f_size) 
    texti = font.render(you_said, True, cl) 
    textRect = texti.get_rect()  
    textRect.center = (x_co,y_co) 
    win.blit(texti, textRect) 

week=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
t=int(xi)+int(1)
print(week[t])
my_df =  pd.read_csv("timetable.csv")
my_df = my_df[my_df['Days']==week[t]]
books = pd.read_csv("timetable.csv")
subjects=[]
books = books['AllBooks']
books_take=[]
for i in range(0,5):
   subjects.append(my_df['s'+str(i+1)][t])

   for j in books:
     
       if(subjects[i].lower() in j.lower() and ('tut' not in (subjects[i].lower() and j.lower()))):
           books_take.append(j)
       elif(subjects[i].lower() in j.lower() and 'tut' in subjects[i].lower() and 'tut' in j.lower()):
           books_take.append(j)
print(books_take)
while True:
    win = pygame.display.set_mode((900, 700))
    win.fill((255,255,255))
    pygame.display.update()
    textwrite("Howdy Kido! It's "+week[t]+" Tomorrow",(0, 220, 128),50,450,100)
    textwrite("Subjects You Have",(0,50,140),40,200,300)
    textwrite("Books to Take",(0,50,140),40,710,300)
    pygame.draw.line(win,(0,0,0),(0,150),(900,150),7)
    pygame.display.update()
    j=300+50
    pygame.display.update()
    for i in subjects:
        textwrite(i,(0,0,0),22,180,j)
        #time.sleep(1)
        pygame.display.update()
        j+=50
    j=300+50
    for i in books_take:
        textwrite(i,(0,0,0),22,700,j)
        pygame.display.update()
        j+=50
    
    time.sleep(20)
    pygame.display.quit()
    
    exit()
    
