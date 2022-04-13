import pygame
import colors_rgb as cl
import random
import os

DIR = os.path.dirname(__file__)

pygame.init()
class SpaceGame:
    def __init__(self):
        """Initial Variables"""
        self.SCREEN_WIDTH=1200 # The Screen Width of the window
        self.SCREEN_HEIGHT=600 # The Screen Height of the window
        self.title="SpaceGame"
        self.Score=0
        
        self.help_window=True
        self.End_window=True
        self.WindowScreen=pygame.display.set_mode((self.SCREEN_WIDTH,self.SCREEN_HEIGHT))
        pygame.display.set_caption(self.title)
        # fonts sizes
        self.GTxt=pygame.font.SysFont("arial", 100, bold=False, italic=False)
        self.MTxt=pygame.font.SysFont("arial", 60, bold=False, italic=False)
        self.NTxt=pygame.font.SysFont("arial", 25, bold=False, italic=False)
        # background
        self.Bg=pygame.transform.scale(pygame.image.load(os.path.join(DIR,"bg1.jpg")),(self.SCREEN_WIDTH,self.SCREEN_HEIGHT))
        self.Bg_x=0
        self.Bg_y=0
        self.Bg_vel=3
        # Player
        self.ShipSize=100
        self.Player=pygame.transform.scale(pygame.image.load(os.path.join(DIR,"ship1.png")),(self.ShipSize,self.ShipSize))
        self.Player_mask=pygame.mask.from_surface(self.Player)
        self.Play_x=int(self.SCREEN_WIDTH/2)
        self.Play_y=int(self.SCREEN_HEIGHT-120)
        self.Play_vel=0
        # enemy size
        self.en_height=100
        self.en_widht=80
        # enemy
        self.E1=pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join(DIR,"ship2.png")),(self.en_widht,self.en_height)),180)
        self.E2=pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join(DIR,"ship2.png")),(self.en_widht,self.en_height)),180)
        self.E3=pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join(DIR,"ship2.png")),(self.en_widht,self.en_height)),180)
        self.E4=pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join(DIR,"ship2.png")),(self.en_widht,self.en_height)),180)
        self.E5=pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join(DIR,"ship2.png")),(self.en_widht,self.en_height)),180)
        self.E6=pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join(DIR,"ship2.png")),(self.en_widht,self.en_height)),180)
        # mask enemy
        self.e1_mask=pygame.mask.from_surface(self.E1)
        self.e2_mask=pygame.mask.from_surface(self.E2)
        self.e3_mask=pygame.mask.from_surface(self.E3)
        self.e4_mask=pygame.mask.from_surface(self.E4)
        self.e5_mask=pygame.mask.from_surface(self.E5)
        self.e6_mask=pygame.mask.from_surface(self.E6)
        # enemy initial location
        self.Ex1,self.Ey1=random.randint(0,self.SCREEN_WIDTH-self.en_widht),0
        self.Ex2,self.Ey2=random.randint(0,self.SCREEN_WIDTH-self.en_widht),-300
        self.Ex3,self.Ey3=random.randint(0,self.SCREEN_WIDTH-self.en_widht),-600
        self.Ex4,self.Ey4=random.randint(0,self.SCREEN_WIDTH-self.en_widht),-900
        self.Ex5,self.Ey5=random.randint(0,self.SCREEN_WIDTH-self.en_widht),-1200
        self.Ex6,self.Ey6=random.randint(0,self.SCREEN_WIDTH-self.en_widht),-1500
        # enemy speed
        self.en_speed=2
        # bullet
        self.Bullet=pygame.transform.scale(pygame.image.load(os.path.join(DIR,"laser_bullet.png")),(8,50))
        self.Mask_bullet=pygame.mask.from_surface(self.Bullet)
        self.Bullet_x=0
        self.Bullet_y=self.Play_y
        self.Bullet_state=False
        self.Bullet_vel=0
        # clock
        self.clk=pygame.time.Clock()
        # window screen title
        self.Bgtitle=pygame.transform.scale(pygame.image.load(os.path.join(DIR,"Window.png")),(int(self.SCREEN_WIDTH/2),int(self.SCREEN_HEIGHT/2)))
        pass

    def StopWindow(self):
        """When Game is Stop"""
        self.Stop_WINDOW = True
        while self.Stop_WINDOW:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.Stop_WINDOW = False
            self.WindowScreen.fill(cl.black)
            self.T3=self.GTxt.render(f"Score = {self.Score}",True,cl.green)
            self.WindowScreen.blit(self.T3,(int(self.SCREEN_WIDTH/3),int(self.SCREEN_HEIGHT/4)))
            pygame.display.update()

    def MainGame(self):
        """Starts the Game"""
        self.StartGame=True
        # Start Game
        self.Start=True
        while self.StartGame:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    self.StartGame=False
                    self.Start=False
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_LEFT:
                        self.Play_vel=-5
                    if event.key==pygame.K_RIGHT:
                        self.Play_vel=5
                    if event.key==pygame.K_DOWN:
                        self.Play_vel=0
                    if event.key==pygame.K_TAB:
                        self.Start=False
                    if event.key==pygame.K_RETURN:
                        self.Start=True
                    if event.key==pygame.K_LSHIFT:
                        self.Bullet_state=True
                        self.Bullet_vel=5
                        self.Bullet_x=self.Play_x
                        self.Bullet_y=self.Play_y
                if event.type==pygame.KEYUP:
                    if event.key==pygame.K_LEFT:
                        self.Play_vel=0
                    if event.key==pygame.K_RIGHT:
                        self.Play_vel=0
                    pass
            # background
            self.WindowScreen.blit(self.Bg,(self.Bg_x,self.Bg_y))
            self.WindowScreen.blit(self.Bg,(self.Bg_x,self.Bg_y-self.SCREEN_HEIGHT))
            if self.Start==True:
                self.Bg_y+=self.Bg_vel
                if self.Bg_y>=self.SCREEN_HEIGHT:
                    self.Bg_y=0
                # Player
                self.Play_x+=self.Play_vel
                if self.Play_x<=0:
                    self.Play_vel=0
                if self.Play_x>=self.SCREEN_WIDTH-self.ShipSize:
                    self.Play_vel=0
                self.WindowScreen.blit(self.Player,(self.Play_x,self.Play_y))
                # enemies
                self.Ey1+=self.en_speed
                self.Ey2+=self.en_speed
                self.Ey3+=self.en_speed
                self.Ey4+=self.en_speed
                self.Ey5+=self.en_speed
                self.Ey6+=self.en_speed

                if self.Ey1>=self.SCREEN_HEIGHT:
                    self.Ey1=-1200
                    self.Ex1=random.randint(0,self.SCREEN_WIDTH-self.en_widht)
                if self.Ey2>=self.SCREEN_HEIGHT:
                    self.Ey2=-1200
                    self.Ex2=random.randint(0,self.SCREEN_WIDTH-self.en_widht)
                if self.Ey3>=self.SCREEN_HEIGHT:
                    self.Ey3=-1200
                    self.Ex3=random.randint(0,self.SCREEN_WIDTH-self.en_widht)
                if self.Ey4>=self.SCREEN_HEIGHT:
                    self.Ey4=-1200
                    self.Ex4=random.randint(0,self.SCREEN_WIDTH-self.en_widht)
                if self.Ey5>=self.SCREEN_HEIGHT:
                    self.Ey5=-1200
                    self.Ex5=random.randint(0,self.SCREEN_WIDTH-self.en_widht)
                if self.Ey6>=self.SCREEN_HEIGHT:
                    self.Ey6=-1200
                    self.Ex6=random.randint(0,self.SCREEN_WIDTH-self.en_widht)

                self.WindowScreen.blit(self.E1,(self.Ex1,self.Ey1))
                self.WindowScreen.blit(self.E2,(self.Ex2,self.Ey2))
                self.WindowScreen.blit(self.E3,(self.Ex3,self.Ey3))
                self.WindowScreen.blit(self.E4,(self.Ex4,self.Ey4))
                self.WindowScreen.blit(self.E5,(self.Ex5,self.Ey5))
                self.WindowScreen.blit(self.E6,(self.Ex6,self.Ey6))
                # Bullet
                if self.Bullet_state==True:
                    self.Bullet_y-=self.Bullet_vel
                    if self.Bullet_y<=0:
                        self.Bullet_state=False
                        self.Bullet_y=self.Play_y
                        self.Bullet_vel=0
                    self.WindowScreen.blit(self.Bullet,(self.Bullet_x+45,self.Bullet_y))
                # bullets collision
                self.bullet_offset1=(int(self.Bullet_x-self.Ex1-20),int(self.Bullet_y-self.Ey1))
                self.bullet_offset2=(int(self.Bullet_x-self.Ex2-20),int(self.Bullet_y-self.Ey2))
                self.bullet_offset3=(int(self.Bullet_x-self.Ex3-20),int(self.Bullet_y-self.Ey3))
                self.bullet_offset4=(int(self.Bullet_x-self.Ex4-20),int(self.Bullet_y-self.Ey4))
                self.bullet_offset5=(int(self.Bullet_x-self.Ex5-20),int(self.Bullet_y-self.Ey5))
                self.bullet_offset6=(int(self.Bullet_x-self.Ex6-20),int(self.Bullet_y-self.Ey6))

                self.coll1_bullet=self.Mask_bullet.overlap(self.e1_mask,self.bullet_offset1)
                if self.coll1_bullet:
                    self.Ey1=-1200
                    self.Score=self.Score+1

                self.coll2_bullet=self.Mask_bullet.overlap(self.e2_mask,self.bullet_offset2)
                if self.coll2_bullet:
                    self.Ey2=-1200
                    self.Score=self.Score+1

                self.coll3_bullet=self.Mask_bullet.overlap(self.e3_mask,self.bullet_offset3)
                if self.coll3_bullet:
                    self.Ey3=-1200
                    self.Score=self.Score+1

                self.coll4_bullet=self.Mask_bullet.overlap(self.e4_mask,self.bullet_offset4)
                if self.coll4_bullet:
                    self.Ey4=-1200
                    self.Score=self.Score+1

                self.coll5_bullet=self.Mask_bullet.overlap(self.e5_mask,self.bullet_offset5)
                if self.coll5_bullet:
                    self.Ey5=-1200
                    self.Score=self.Score+1

                self.coll6_bullet=self.Mask_bullet.overlap(self.e6_mask,self.bullet_offset6)
                if self.coll6_bullet:
                    self.Ey6=-1200
                    self.Score=self.Score+1
                
                # SHIP COLLISION ITSELF 
                self.itself_coll_offset1=(int(self.Ex1-self.Ex2),int(self.Ey1-self.Ey2))
                self.itself_coll_offset2=(int(self.Ex2-self.Ex3),int(self.Ey2-self.Ey3))
                self.itself_coll_offset3=(int(self.Ex3-self.Ex4),int(self.Ey3-self.Ey4))
                self.itself_coll_offset4=(int(self.Ex4-self.Ex5),int(self.Ey4-self.Ey5))
                self.itself_coll_offset5=(int(self.Ex5-self.Ex6),int(self.Ey5-self.Ey6))
                self.itself_coll_offset6=(int(self.Ex2-self.Ex4),int(self.Ey2-self.Ey4))
                self.itself_coll_offset7=(int(self.Ex2-self.Ex5),int(self.Ey2-self.Ey5))
                self.itself_coll_offset8=(int(self.Ex2-self.Ex6),int(self.Ey2-self.Ey6))
                self.itself_coll_offset9=(int(self.Ex3-self.Ex1),int(self.Ey3-self.Ey1))
                self.itself_coll_offset10=(int(self.Ex3-self.Ex5),int(self.Ey3-self.Ey5))
                self.itself_coll_offset11=(int(self.Ex3-self.Ex6),int(self.Ey3-self.Ey6))
                self.itself_coll_offset12=(int(self.Ex4-self.Ex1),int(self.Ey4-self.Ey1))
                self.itself_coll_offset13=(int(self.Ex4-self.Ex2),int(self.Ey4-self.Ey2))
                self.itself_coll_offset14=(int(self.Ex4-self.Ex6),int(self.Ey4-self.Ey6))
                self.itself_coll_offset15=(int(self.Ex5-self.Ex1),int(self.Ey5-self.Ey1))
                self.itself_coll_offset16=(int(self.Ex5-self.Ex2),int(self.Ey5-self.Ey2))
                self.itself_coll_offset17=(int(self.Ex5-self.Ex3),int(self.Ey5-self.Ey3))
                self.itself_coll_offset18=(int(self.Ex6-self.Ex1),int(self.Ey6-self.Ey1))

                self.coll_itself1=self.e1_mask.overlap(self.e2_mask,self.itself_coll_offset1)
                if self.coll_itself1:
                    self.Ex1+=5
                self.coll_itself2=self.e2_mask.overlap(self.e3_mask,self.itself_coll_offset2)
                if self.coll_itself2:
                    self.Ex2+=5
                self.coll_itself3=self.e3_mask.overlap(self.e4_mask,self.itself_coll_offset3)
                if self.coll_itself3:
                    self.Ex3+=5
                self.coll_itself4=self.e4_mask.overlap(self.e5_mask,self.itself_coll_offset4)
                if self.coll_itself4:
                    self.Ex4+=5
                self.coll_itself5=self.e5_mask.overlap(self.e6_mask,self.itself_coll_offset5)
                if self.coll_itself5:
                    self.Ex5+=5
                self.coll_itself6=self.e2_mask.overlap(self.e4_mask,self.itself_coll_offset6)
                if self.coll_itself6:
                    self.Ex2+=5
                self.coll_itself7=self.e2_mask.overlap(self.e5_mask,self.itself_coll_offset7)
                if self.coll_itself7:
                    self.Ex2+=5
                self.coll_itself8=self.e2_mask.overlap(self.e6_mask,self.itself_coll_offset8)
                if self.coll_itself8:
                    self.Ex2+=5
                self.coll_itself9=self.e3_mask.overlap(self.e1_mask,self.itself_coll_offset9)
                if self.coll_itself9:
                    self.Ex3+=5
                self.coll_itself10=self.e3_mask.overlap(self.e5_mask,self.itself_coll_offset10)
                if self.coll_itself10:
                    self.Ex3+=5
                self.coll_itself11=self.e3_mask.overlap(self.e6_mask,self.itself_coll_offset11)
                if self.coll_itself11:
                    self.Ex3+=5
                self.coll_itself12=self.e4_mask.overlap(self.e1_mask,self.itself_coll_offset12)
                if self.coll_itself2:
                    self.Ex4+=5
                self.coll_itself13=self.e4_mask.overlap(self.e2_mask,self.itself_coll_offset13)
                if self.coll_itself13:
                    self.Ex4+=5
                self.coll_itself14=self.e4_mask.overlap(self.e6_mask,self.itself_coll_offset14)
                if self.coll_itself14:
                    self.Ex4+=5
                self.coll_itself15=self.e5_mask.overlap(self.e1_mask,self.itself_coll_offset15)
                if self.coll_itself15:
                    self.Ex5+=5
                self.coll_itself16=self.e5_mask.overlap(self.e2_mask,self.itself_coll_offset16)
                if self.coll_itself16:
                    self.Ex5+=5
                self.coll_itself17=self.e5_mask.overlap(self.e3_mask,self.itself_coll_offset17)
                if self.coll_itself17:
                    self.Ex5+=5
                self.coll_itself18=self.e6_mask.overlap(self.e1_mask,self.itself_coll_offset18)
                if self.coll_itself18:
                    self.Ex6+=5
                # collisions
                self.coll1_offset=(int(self.Play_x-self.Ex1),int(self.Play_y-self.Ey1))
                self.coll2_offset=(int(self.Play_x-self.Ex2),int(self.Play_y-self.Ey2))
                self.coll3_offset=(int(self.Play_x-self.Ex3),int(self.Play_y-self.Ey3))
                self.coll4_offset=(int(self.Play_x-self.Ex4),int(self.Play_y-self.Ey4))
                self.coll5_offset=(int(self.Play_x-self.Ex5),int(self.Play_y-self.Ey5))
                self.coll6_offset=(int(self.Play_x-self.Ex6),int(self.Play_y-self.Ey6))

                self.coll1=self.Player_mask.overlap(self.e1_mask,self.coll1_offset)
                if self.coll1:
                    self.StartGame=False
                    self.Start=False
                    self.StopWindow()
                self.coll2=self.Player_mask.overlap(self.e2_mask,self.coll2_offset)
                if self.coll2:
                    self.StartGame=False
                    self.Start=False
                    self.StopWindow()
                self.coll3=self.Player_mask.overlap(self.e3_mask,self.coll3_offset)
                if self.coll3:
                    self.StartGame=False
                    self.Start=False
                    self.StopWindow()
                self.coll4=self.Player_mask.overlap(self.e4_mask,self.coll4_offset)
                if self.coll4:
                    self.StartGame=False
                    self.Start=False
                    self.StopWindow()
                self.coll5=self.Player_mask.overlap(self.e5_mask,self.coll5_offset)
                if self.coll5:
                    self.StartGame=False
                    self.Start=False
                    self.StopWindow()
                self.coll6=self.Player_mask.overlap(self.e6_mask,self.coll6_offset)
                if self.coll6:
                    self.StartGame=False
                    self.Start=False
                    self.StopWindow()
            pygame.display.update()
            self.clk.tick(120)
        pass

    def InitialWindow(self):
        self.initial_window=True
        while self.initial_window:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    self.initial_window=False
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        self.MainGame()
                        self.initial_window=False
            self.WindowScreen.blit(self.Bg,(self.Bg_x,self.Bg_y))
            self.WindowScreen.blit(self.Bgtitle,(int(self.SCREEN_WIDTH/4),int(self.SCREEN_HEIGHT/4)))
            self.T1=self.NTxt.render("Press ENTER to Start",True,cl.green)
            self.WindowScreen.blit(self.T1,(int(self.SCREEN_WIDTH/2),int(self.SCREEN_HEIGHT-200)))
            pygame.display.update()
        pass
    pass

Game=SpaceGame()
Game.InitialWindow()