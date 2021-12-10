import pygame as pg
import random
import sys
from os import path
from settings import *
from object import *
import time
import socket
import threading as xianchen
class Game:
    def __init__(self):
        # initalize game window, etc...
        pg.init()
        pg.mixer.init()
        #self.music=pg.mixer.music.load("image/1.mp3")
        #self.music=pg.mixer.music.load("image/2.mp3")
        self.screen = pg.display.set_mode((800,600))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        # Let the key press down
        pg.key.set_repeat(500, 100)
        #main interface
        self.mian_jiemian=pg.image.load("image/mainground.png")
        self.chuangjian_fj1=pg.image.load("BNB/xz1.png")
        self.chuangjian_fj2=pg.image.load("BNB/xz2.png")
        self.room=pg.image.load("BNB/room.png")
        self.black=pg.image.load("BNB/black.png")
        #
        #create the room and initialize as a room owner
        self.thread=None#server thread!!!!!!!!!!!!!
        self.sever=None
        self.client=None
        self.msg=""
        self.lianjie=False
        self.box_msg=""
        self.playing=False
        self.player_index=None
        #chat+command system
        self.chat_box=None
        #room player content
        self.player_msg_list=[]
        #gamr role info
        self.play_imformation_list=[]
        self.player_play_list=[]
   
        self.zhen=255
        #send data to sever
        self.play_imformation_kuang=pg.image.load("image/play_imformation/play information box.png")
        self.wall_list=[]
        self.daoju_list=[]# item
        self.robot_list=[]# robot
        self.robot_bomb=[]# robot's bomb
        self.box_list=[]# box

        self.running = True
        self.bomb=[]#player's bomb
        self.cunfang=""
        self.bomb_shuliang=0
        self.jiemian=0
        #player's skin info
        self.player_play_list.append(Player(1,1,self.screen,1))
        self.name=""
        self.x=0
        self.jishu=0
        self.choice_name()
    
        self.player_msg_list.append(player_icons(self.screen, self.player_play_list[0].pifu,self.name,0,"fang zhu"))
        #32x24
        #pg.mixer.music.play(-1)
 
    def clear(self):
        self.wall_list=[]
        self.daoju_list=[]
        self.robot_list=[]
        self.robot_bomb=[]
        self.box_list=[]
        self.bomb=[]
        self.play_imformation_list=[]
        self.player_play_list=[]
    def choice_name(self):
        self.name=random.choice(["Clever ","Naughty ","Handsome "," violent ","rich ","low-key ","steady ","Jovial"])+random.choice(["Duck","pig","froggy","John Doe","Passerby B","Bystander C","Xiao Ming","Xiao Hong","Xiao Zhang","Xiao Pao"])
    def receive(self):
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server.bind((socket.gethostbyname(socket.gethostname()), 2001))
            self.server.listen(5)
            self.client, ip = self.server.accept()
            self.lianjie=True
            print("ok")
            while True:
                try:
                    #1 is move, 2 is to set the bomb, 3 is the robot location, 4 is the monster bob
                    #5 is to refresh the items, 6 it to pick items, 7 it to destroy the wall
                    msg = self.client.recv(1024).decode("utf-8")
                    if msg.split("|")[0] == "1":
                        print(msg)
                        self.player_play1.x = int(msg.split("|")[1].split(",")[0])
                        self.player_play1.y = int(msg.split("|")[1].split(",")[1])
                    elif msg.split("|")[0] == "2":
                        
                        if len(msg.split("|")[1].split("*"))-1!=self.robot_bomb:
                            self.map_data[int(msg.split("|")[1].split(",")[1])] = self.map_data[int(msg.split("|")[1].split(",")[1])][:int(msg.split("|")[1].split(",")[0])] + "3" + self.map_data[int(msg.split("|")[1].split(",")[1])][int(msg.split("|")[1].split(",")[0]) + 1:]
                            self.bomb.append(Bomb(int(msg.split("|")[1].split(",")[0]), int(msg.split("|")[1].split(",")[1]), self.screen, self.map_data, int(msg.split("|")[1].split(",")[2]), "123"))
                    elif msg.split("|")[0]== "3":
                        for i in range(0,len(msg.split("|")[1].split("."))):
                            self.robot_list[i].x=int(msg.split("|")[1].split(".")[i].split(",")[0])
                            self.robot_list[i].y=int(msg.split("|")[1].split(".")[i].split(",")[1])
                    elif msg.split("|")[0]=="4":
                        self.map_data[int(msg.split("|")[1].split(",")[1])] = self.map_data[int(msg.split("|")[1].split(",")[1])][:int(msg.split("|")[1].split(",")[0])] + "3" + self.map_data[int(msg.split("|")[1].split(",")[1])][int(msg.split("|")[1].split(",")[0]) + 1:]
                        self.robot_bomb.append(Bomb(int(msg.split("|")[1].split(",")[0]), int(msg.split("|")[1].split(",")[1]), self.screen, self.map_data, int(msg.split("|")[1].split(",")[2]), "guaishou"))
                        print("ok")
                    elif msg.split("|")[0]=="5":
                        self.daoju_list.append(Daoju(self.screen,int(msg.split("|")[1].split(",")[0]),int(msg.split("|")[1].split(",")[1]),int(msg.split("|")[1].split(",")[2])))
                    elif msg.split("|")[0]=="6":
                        del self.daoju_list[int(msg.split("|")[1])]                    
                    elif msg.split("|")[0]=="7":
                        del self.box_list[int(msg.split("|")[1])]
                except:
                    pass
    def connect(self):
        pass
    def load_data(self):
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder,'image')
        self.background1 = pg.image.load("image/background1.png").convert_alpha()
        self.background2 = pg.image.load("image/background2.png").convert_alpha()
        self.map_data = []
        with open('map/map.txt', 'rt') as f:
            for line in f:
                self.map_data.append(line[:-1])
    def new(self):
        #    y    x
        for row, tiles in enumerate(self.map_data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    self.wall_list.append(Wall(self.screen,col,row,"wall"))
                elif tile == "a":
                    self.box_list.append(Box(self.screen,col,row,self.sever.duixiang_index[1],"box"))
                    self.sever.box_msg+=str(self.sever.duixiang_index[1])+"."
                    self.sever.duixiang_index[1]+=1
    def single_new(self):
        for row, tiles in enumerate(self.map_data):
            for col, tile in enumerate(tiles):
                if tile == '2':
                    self.wall_list.append(Wall(self.screen,col,row,"stone"))
                elif tile == "b":
                    self.box_list.append(Box(self.screen,col,row,1,"orange_box"))
                elif tile=="c":
                    self.box_list.append(Box(self.screen,col,row,1,"red_box"))
    def main_jiemian(self):
        #self.music=pg.mixer.music.load("image/1.mp3")
        #pg.mixer.music.play(-1)
        self.screen = pg.display.set_mode((800, 600))
        self.jiemian=0
        while True:
                if self.zhen>=0:
                    self.zhen-=0.5
                    self.black.set_alpha(self.zhen)
                    self.screen.blit(self.mian_jiemian, (0, 0))
                    self.screen.blit(self.black,(0,0))
                else:
                    self.screen.blit(self.mian_jiemian, (0, 0))
                    self.screen.blit(self.black,(0,0))
                    mousex, mousey = pg.mouse.get_pos()
                    for event in pg.event.get():
                        # check for closing the window
                        if event.type == pg.QUIT:
                            quit()
                        if event.type == pg.MOUSEBUTTONDOWN:
                            # 74 366 342 444
                            # 74 750 342 552
                            if 74 <= mousex <= 342 and 366 <= mousey <= 444:
                                self.jiemian = 1
                                break
                            elif 74 <= mousex <= 342 and 474 <= mousey <= 553:
                                self.jiemian = 2
                                break
                    if self.jiemian!=0:break
                pg.display.update()
    def game_room(self):
        self.screen = pg.display.set_mode((1202, 900))
        self.jiemian=-1
        if self.thread == None:
            self.thread=xianchen.Thread(target=Sever, args=(socket.gethostbyname(socket.gethostname()),self,))
            self.thread.setDaemon(True)
            self.thread.start()
        self.index=0
        self.zhen=280
        # set the thread
        while True:
            if self.zhen >= 0:
                self.zhen -= 3
                self.black.set_alpha(self.zhen)
                self.screen.blit(self.room, (0, 0))
                if len(self.player_msg_list)>0:
                    for i in self.player_msg_list:
                        i.update()
                self.screen.blit(self.black, (0, 0))
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        quit()
            else:
                self.screen.blit(self.room, (0, 0))
                mousex, mousey = pg.mouse.get_pos()
                if len(self.player_msg_list)>0:
                    for i in self.player_msg_list:
                        i.update()
                for event in pg.event.get():
                    # check for closing the window
                    if event.type == pg.QUIT:
                        quit()
                    if event.type == pg.MOUSEBUTTONDOWN:
                        len_player=0
                        if 773<=mousex<=1057 and 467<=mousey<=824:
                            for i in range(0,len(self.sever.js_xinxi.split("|")[2].split(".")) - 1):
                                if str(self.sever.js_xinxi.split("|")[2].split(".")[i]).split(",")[2]=="ready":
                                    len_player+=1
                            if len(self.sever.g_conn_pool)==len_player:
                                xuhao = 0
                                self.sever.clear()
                                self.clear()
                                self.player_play_list.append(Player(1, 1, self.screen, 1))
                                for i in range(0,len(self.sever.js_xinxi.split("|")[2].split("."))-1):
                                    if self.sever.js_xinxi.split("|")[2].split(".")[i]!="-1,no name,no ready":
                                        if i!=0:
                                            self.player_play_list.append(Player(1,1,self.screen,int(self.sever.js_xinxi.split("|")[2].split(".")[i].split(",")[0])))
                                            #                        x y   skin_value   initial_bomb_range    name
                                        #initialize the data
                                        self.sever.play_player_move+="1,1."
                                        self.sever.player_imformation_msg+=self.sever.js_xinxi.split("|")[2].split(".")[i].split(",")[0]+self.sever.js_xinxi.split("|")[2].split(".")[i].split(",")[1]+"."
                                        self.sever.play_player_msg+="1,1,"+self.sever.js_xinxi.split("|")[2].split(".")[i].split(",")[0]+","+"1,"+self.sever.js_xinxi.split("|")[2].split(".")[i].split(",")[1]+","+str(i)+"."
                                        self.sever.play_life_msg+="0."
                                        self.play_imformation_list.append(Play_imformation(self.screen,int(self.sever.js_xinxi.split("|")[2].split(".")[i].split(",")[0]),self.sever.js_xinxi.split("|")[2].split(".")[i].split(",")[1],i))
                                        xuhao += 1
                                    else:
                                        self.play_imformation_list.append(None)
                                self.sever.send_player("1|Enter game|")
                                self.sever.send_player(self.sever.play_player_msg)
                                msg="2|move|"
                                for i in range(0,len(self.player_play_list)):
                                    msg+="1,1."
                                self.sever.send_player(msg)
                                self.playing=True
                                self.jiemian=4
                if self.jiemian != -1: break
            self.clock.tick(FPS)
            pg.display.update()
    def create_room(self):
        self.screen = pg.display.set_mode((800, 600))
        xuanze=0
        self.jiemian=-1
        while True:
            self.screen.blit(self.mian_jiemian, (0, 0))
            if xuanze==0:
                self.screen.blit(self.chuangjian_fj1,(130,63))
            else:
                self.screen.blit(self.chuangjian_fj2,(131,63))
            mousex, mousey = pg.mouse.get_pos()
            for event in pg.event.get():
                # check for closing the window
                if event.type == pg.QUIT:
                    quit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    # 130  63   762 478
                    if 165 <= mousex <=288 and 135 <= mousey <=304:
                        xuanze=1
                    elif xuanze==1 and 320 <= mousex <=427 and 424 <= mousey <=461:
                        self.jiemian=3
                        break
                    elif 433 <= mousex <=538 and 424 <= mousey <=461:
                        self.jiemian=0
                        break
                    # 130  63   762 478
            if self.jiemian!=-1:break
            pg.display.update()
    def duoren(self):

        self.load_data()
        self.screen = pg.display.set_mode((1280, 768))
        self.chat_box=chat_box(self.screen,self,self.sever,"sever")
        self.new()
        self.shu_ying = False
        self.end_kuang = None
        self.end_time = 350
        self.zhen=280
        while True:
            if not self.shu_ying:
                if self.zhen >= 0:
                    self.zhen -= 3
                    self.black.set_alpha(self.zhen)
                    self.draw()
                    self.update()
                    self.screen.blit(self.black, (0, 0))
                    for event in pg.event.get():
                        if event.type == pg.QUIT:
                            quit()
                else:
                    self.events()
                    self.draw()
                    self.update()
            else:
                self.draw()
                self.update()
                self.end_kuang.update()#end game image
                if self.end_time>=0:
                    self.end_time-=1
                else:
                    if self.zhen>=280:
                        self.playing=False
                        self.jiemian=3
                        break
                    self.zhen+=2.5
                    self.black.set_alpha(self.zhen)
                    self.screen.blit(self.black, (0, 0))
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        quit()
            self.clock.tick(FPS)
            pg.display.update()
    def run(self):
        #interface running
        # Game loop
        while True:
            if self.jiemian==0:
                self.main_jiemian()
            elif self.jiemian==1:
                self.danren()
            elif self.jiemian==2:
                self.create_room()
            elif self.jiemian==3:
                self.game_room()
            elif self.jiemian==4:
                self.duoren()
    def update(self):

        for i in self.wall_list:
            i.update()
        self.screen.blit(self.play_imformation_kuang,(1024,0))
        for i in self.play_imformation_list:
            if i!=None:
                i.update()
        self.chat_box.update()
    def events(self):
        # Game loop - events
        for event in pg.event.get():
        # check for closing the window
            if event.type == pg.QUIT:
                quit()
            if event.type == pg.KEYDOWN:
                move=None
                self.chat_box.event(event.key)
                if not self.chat_box.useing:
                    if self.player_play_list[0].die == 0:
                        if event.key==pg.K_SPACE:
                            shifang=False
                            if len(self.bomb)>0:
                                for i in self.bomb:
                                    if i.x==self.player_play_list[0].x and i.y==self.player_play_list[0].y:
                                        shifang=True
                                                                        
                            if not shifang :
                                self.sever.bomb_msg+=str(self.sever.duixiang_index[0])+","+str(self.player_play_list[0].x)+","+str(self.player_play_list[0].y)+","+str(self.player_play_list[0].fanwei)+"."
                                self.sever.send_player(self.sever.bomb_msg)
                                self.bomb.append(Bomb(self.player_play_list[0].x,self.player_play_list[0].y,self.screen,self.map_data,self.player_play_list[0].fanwei,"paopao",self.sever.duixiang_index[0]))
                                self.sever.duixiang_index[0]+=1
                        if event.key == pg.K_LEFT:
                            if len(self.bomb)>0:
                                for i in self.bomb:
                                    if i.x == self.player_play_list[0].x-1 and i.y == self.player_play_list[0].y:
                                        move=True
                            if not move and self.map_data[self.player_play_list[0].y][self.player_play_list[0].x-1]=="." or self.map_data[self.player_play_list[0].y][self.player_play_list[0].x-1]=="3":
                                self.player_play_list[0].move (dx=-1)
                        elif event.key == pg.K_RIGHT:
                            if len(self.bomb) > 0:
                                for i in self.bomb:
                                    if i.x == self.player_play_list[0].x + 1 and i.y == self.player_play_list[0].y:
                                        move = True
                            if not move and self.map_data[self.player_play_list[0].y][self.player_play_list[0].x + 1] =="." or self.map_data[self.player_play_list[0].y][self.player_play_list[0].x + 1] =="3":
                                    self.player_play_list[0].move (dx=1)
                        elif event.key == pg.K_UP:
                            if len(self.bomb) > 0:
                                for i in self.bomb:
                                    if i.x == self.player_play_list[0].x  and i.y == self.player_play_list[0].y-1:
                                        move = True
                            if not move and self.map_data[self.player_play_list[0].y-1][self.player_play_list[0].x ] =="." or self.map_data[self.player_play_list[0].y-1][self.player_play_list[0].x ] =="3":
                                    self.player_play_list[0].move (dy=-1)
                        elif event.key == pg.K_DOWN:
                            if len(self.bomb) > 0:
                                for i in self.bomb:
                                    if i.x == self.player_play_list[0].x  and i.y == self.player_play_list[0].y+1:
                                        move = True
                            if not move and self.map_data[self.player_play_list[0].y+1][self.player_play_list[0].x ] =="." or self.map_data[self.player_play_list[0].y+1][self.player_play_list[0].x ] =="3":
                                    self.player_play_list[0].move (dy=1)
                    # players movement as x,y,1.(x and y and bomb range)
                    #print("self.sever.play_player_msg"+self.sever.play_player_msg)
                    if len(self.daoju_list)>0:
                        daoju_msg = "2|property|"
                        zhi = -1
                        for index, daoju in enumerate(self.daoju_list):
                            if self.player_play_list[0].x == daoju.x and self.player_play_list[0].y == daoju.y:
                                zhi = index
                            else:
                                daoju_msg += str(daoju.x) + "," + str(daoju.y) + ",1," + str(daoju.index) + "."
                        if zhi != -1:
                            del self.daoju_list[zhi]
                        if self.sever.daoju_msg!=daoju_msg:
                            self.sever.send_player(daoju_msg)
                            self.sever.daoju_msg=daoju_msg
                    msg="2|move|"+str(self.player_play_list[0].x)+","+str(self.player_play_list[0].y)+"."
                    for i in range(1,len(self.sever.play_player_move.split("|")[2].split("."))-1):
                        if self.sever.play_player_move.split("|")[2].split(".")[i]=="None":
                            msg+="None."
                        else:
                            msg+=self.sever.play_player_move.split("|")[2].split(".")[i].split(",")[0]+","+self.sever.play_player_move.split("|")[2].split(".")[i].split(",")[1]+"."
                    self.sever.play_player_move=msg
                    for i in self.sever.g_conn_pool:
                        i.sendall(self.sever.play_player_move.encode("utf8"))
    def draw_grid(self):
        pass

    def draw(self):
        # Game loop - draw
        # Draw / render
        #self.screen.fill(DARKGREY)
        self.screen.blit(self.background1,[0,0])
        box_baozha=False
        if len(self.box_list)>0:
            for index,i in enumerate(self.box_list):
                if i!=None:
                    i.update()
                    if i.die==2:
                        box_baozha=True
                        if Daoju.jiance(i.daoju):
                            self.daoju_list.append(Daoju(self.screen,i.x,i.y,i.daoju,self.sever.duixiang_index[2]))
                            self.sever.daoju_msg+=str(i.x)+","+str(i.y)+","+str(i.daoju)+","+str(self.sever.duixiang_index[2])+"."
                            self.sever.duixiang_index[2]+=1
                            self.sever.send_player(self.sever.daoju_msg)
                        self.box_list[index]=None
                        self.map_data[i.y] = self.map_data[i.y][:i.x] + "." + self.map_data[i.y][i.x + 1:]
            else:
                if box_baozha:
                    box_msg = "2|box|"
                    for i in self.box_list:
                        if i==None:
                            box_msg+="No."
                        else:
                            box_msg+=str(i.xuhao)+"."
                    self.sever.box_msg=box_msg
                    self.sever.send_player(self.sever.box_msg)
        if len(self.bomb) > 0:#玩家炸弹
            for index,i in enumerate(self.bomb):
                i.update()
                if i.time==60:
                    box_die_pd=False
                    box_die_msg ="2|box_xinxi|"
                    for x, y in i.baozha_list:
                        for box in self.box_list:
                            if box!=None:
                                if x==box.x and y==box.y:
                                    #delete the box after the animination
                                    box_die_pd=True
                                    box.die=1
                                    box_die_msg +=str(box.xuhao)+"."
                                    break
                    if box_die_pd:
                        self.sever.send_player(box_die_msg)
                   
                    # delete the bomb with time 0
                if i.time == 0:
                    bomb_msg="2|bomb|"
                    self.bomb.remove(i)
                    for i in self.bomb:
                        bomb_msg+=str(i.index)+","+str(i.x)+","+str(i.y)+","+str(i.fanwei)+"."
                    if self.sever.bomb_msg!=bomb_msg:
                        self.sever.bomb_msg=bomb_msg
                        self.sever.send_player(self.sever.bomb_msg)
        if len(self.daoju_list)>0:
            for i in self.daoju_list:
                i.update()
        life_msg = "2|life|"
        people_shu=0
        for index,i in enumerate(self.player_play_list):
            if i == None:
                life_msg+="None."
            else:
                if self.map_data[i.y][i.x]=="3" and i.die==0:
                    i.die = 1
                    life_msg += "1."
                    self.play_imformation_list[index].zhuang_tai=i.die
                else:
                    life_msg+=str(i.die)+"."
                    if i.die==0:
                        people_shu+=1
                i.update()
        else:
            if people_shu<=1 and self.shu_ying == False:
                win_xuhao=None
                for index,i in enumerate(self.play_imformation_list):
                    if i!=None:
                        if i.zhuang_tai==0:
                            win_xuhao=index
                self.shu_ying=True
                self.end_kuang = end_kuang(self.screen, self.play_imformation_list,win_xuhao,0)
                self.sever.send_player("2|end|" + str(win_xuhao))
            if life_msg != self.sever.play_life_msg:
                self.sever.play_life_msg = life_msg
                self.sever.send_player(self.sever.play_life_msg)
        self.draw_grid()
    def danren(self):
        #self.music=pg.mixer.music.load("image/2.mp3")
        #pg.mixer.music.play(-1)
        self.screen = pg.display.set_mode((561, 495))
        self.wall_list=[]
        self.box_list=[]
        self.daoju_list=[]
        self.guaishou_list=[]
        self.single_load_information()
        self.single_new()
        for i in range(0,6):
            self.guaishou_list.append(ghost(self.screen,self.map_data))
        self.zhen=280
        self.shu_ying=False
        self.end_time=300
        while True:
            if not self.shu_ying:
                if self.zhen >= 0:
                    self.zhen -= 3
                    self.black.set_alpha(self.zhen)
                    self.single_update()
                    self.single_draw()
                    self.screen.blit(self.black, (0, 0))
                    for event in pg.event.get():
                        if event.type == pg.QUIT:
                            quit()
                else:
                    self.single_events()
                    self.single_update()
                    self.single_draw()
            else:
                self.single_update()
                self.single_draw()
                if self.end_time>=0:
                    self.end_time-=1
                else:
                    if self.zhen>=280:
                        self.jiemian=0
                        break
                    self.zhen+=2.5
                    self.black.set_alpha(self.zhen)
                    self.screen.blit(self.black, (0, 0))
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        quit()
            self.clock.tick(FPS)
            pg.display.update()
    def single_load_information(self):
        self.map_data = []
        with open('map/single_map.txt', 'rt') as f:
            for line in f:
                self.map_data.append(line[:-1])
        self.player=Player(1,1,self.screen,1)
        self.background2 = pg.image.load("image/background2.png").convert_alpha()
    def single_events(self):
        for event in pg.event.get():
            # check for closing the window
            if event.type == pg.QUIT:
                quit()
            if event.type == pg.KEYDOWN:
                move = None
                if self.player.die == 0:
                    if event.key == pg.K_SPACE:
                        shifang = False
                        if len(self.bomb) > 0:
                            for i in self.bomb:
                                if i.x == self.player.x and i.y == self.player.y:
                                    shifang = True
                        if not shifang:
                            self.bomb.append(Bomb(self.player.x, self.player.y, self.screen,self.map_data, self.player.fanwei, "paopao",1))
                    if event.key == pg.K_LEFT:
                        if len(self.bomb) > 0:
                            for i in self.bomb:
                                if i.x == self.player.x - 1 and i.y == self.player.y:
                                    move = True
                        if not move and self.map_data[self.player.y][self.player.x - 1] == "." or self.map_data[self.player.y][self.player.x - 1] == "3":
                            self.player.move(dx=-1)
                    elif event.key == pg.K_RIGHT:
                        if len(self.bomb) > 0:
                            for i in self.bomb:
                                if i.x == self.player.x + 1 and i.y == self.player.y:
                                    move = True
                        if not move and self.map_data[self.player.y][self.player.x + 1] == "." or self.map_data[self.player.y][self.player.x + 1] == "3":
                            self.player.move(dx=1)
                    elif event.key == pg.K_UP:
                        if len(self.bomb) > 0:
                            for i in self.bomb:
                                if i.x == self.player.x and i.y == self.player.y - 1:
                                    move = True
                        if not move and self.map_data[self.player.y - 1][self.player.x] == "." or self.map_data[self.player.y - 1][self.player.x] == "3":
                            self.player.move(dy=-1)
                    elif event.key == pg.K_DOWN:
                        if len(self.bomb) > 0:
                            for i in self.bomb:
                                if i.x == self.player.x and i.y == self.player.y + 1:
                                    move = True
                        if not move and self.map_data[self.player.y + 1][self.player.x] == "." or self.map_data[self.player.y + 1][self.player.x] == "3":
                            self.player.move(dy=1)
                    if len(self.daoju_list)>0:
                        zhi = -1
                        for index, daoju in enumerate(self.daoju_list):
                            if self.player.x == daoju.x and self.player.y == daoju.y:
                                zhi = index
                        if zhi != -1:
                            del self.daoju_list[zhi]
    def single_update(self):
        self.screen.blit(self.background2,(0,0))
        if len(self.box_list)>0:
            for index,i in enumerate(self.box_list):
                if i!=None:
                    i.update()
                    if i.die==2:
                        if Daoju.jiance(i.daoju):
                            self.daoju_list.append(Daoju(self.screen,i.x,i.y,i.daoju,1))
                        self.box_list[index]=None
                        self.map_data[i.y] = self.map_data[i.y][:i.x] + "." + self.map_data[i.y][i.x + 1:]
        if len(self.bomb) > 0:#玩家炸弹
            for index,i in enumerate(self.bomb):
                i.update()
                if i.time==60:
                    for x, y in i.baozha_list:
                        for box in self.box_list:
                            if box != None:
                                if x == box.x and y == box.y:
                                
                                    box.die = 1
                                    break
            
                if i.time == 0:
                    self.bomb.remove(i)
        self.player.update()
        if len(self.daoju_list)>0:
            for i in self.daoju_list:
                i.update()
        if self.map_data[self.player.y][self.player.x]=="3" and self.player.die==0:
            self.shu_ying=True
            self.player.die=1
    def single_draw(self):
        if len(self.guaishou_list)>0:
            for i in self.guaishou_list:
                i.update()
                if self.player.y==i.y and self.player.x==i.x and self.player.die==0:
                    self.player.die=1
                    self.player.die_zhen=17
                    self.player.time=0
                    self.shu_ying = True
                if i.die==2:
                    self.guaishou_list.remove(i)
                    print("当前怪兽数量"+str(len(self.guaishou_list)))
        else:
            self.shu_ying=True
        for i in self.wall_list:
            i.update()
    def wait_room(self):
        #房间................
        pass
    def show_start_screen(self):
        # Game start screen
        pass
    def show_go_screen(self):
        # Game over screen
        pass
    def jiexi(self,str1):
        self.player_msg_list=[]
        for i in range(0, len(str1.split("|")[2].split(".")) - 1):
            if str1.split("|")[2].split(".")[i]!="-1,no name,no ready":
                self.player_msg_list.append(player_icons(self.screen, int(str1.split("|")[2].split(".")[i].split(",")[0]), str1.split("|")[2].split(".")[i].split(",")[1], i,str1.split("|")[2].split(".")[i].split(",")[2]))
    def bomb_jiexi(self,x,y,fanwei,index):
        print("ok")
        self.bomb.append(Bomb(int(x),int(y),self.screen,self.map_data,int(fanwei),"paopao",index))
        print("ok")
class Sever():
    def __init__(self,ADDRESS,duixiang):
        self.duixiang=duixiang
        self.duixiang.sever=self
        print(self.duixiang.sever)
        self.ADDRESS =(ADDRESS,5000)  # SET THE ADDRESS HERE("x.xxx.xxx.xxx",5000)
        self.g_socket_server = None  # the listening socket
        self.g_conn_pool = []  #the connect pool
        #
        self.js_xinxi="1|msg|"# player's info
        self.js_xinxi+=str(self.duixiang.player_play_list[0].pifu)+","+self.duixiang.name+","+"no ready"+"."
        #             role info, name, ready?
        self.js_xinxi+= "-1,no name,no ready.-1,no name,no ready.-1,no name,no ready.-1,no name,no ready.-1,no name,no ready.-1,no name,no ready.-1,no name,no ready."
        self.play_msg_list=[]
        #
        #1 is when not entering the game,2 is when entering the game

        self.play_player_msg="2|js|"
        self.player_imformation_msg="2|imformation|"
        self.play_player_move="2|move|"
        self.play_life_msg="2|life|"
        self.bomb_msg="2|bomb|"
        self.daoju_msg = "2|property|" 
        self.box_msg = "2|box|"  
        #                 bomb_index,box_index,property_index
        self.duixiang_index=[0,0,0]
        self.init()
        self.accept_client()
    def init(self):
        # initialize the server
        self.g_socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.g_socket_server.bind(self.ADDRESS)
        self.g_socket_server.listen(5)
    def clear(self):
        self.play_player_msg="2|js|"
        self.player_imformation_msg="2|imformation|"
        self.play_player_move="2|move|"
        self.play_life_msg="2|life|"
        self.bomb_msg="2|bomb|"
        self.daoju_msg = "2|property|"  
        self.box_msg = "2|box|"  
        #                 bomb_index,box_index,property_index
        self.duixiang_index=[0,0,0]
    def return_g_conn_pool(self):
        pass
    def send_player(self,msg):
        print("msg"+msg)
        if len(self.g_conn_pool)>0:
            for i in self.g_conn_pool:
                i.sendall(msg.encode("utf8"))
                time.sleep(0.005)
    def accept_client(self):
        # accept the new connection
        join=False
        while True:
            client,ip = self.g_socket_server.accept()  #stop and wait for the server th connect
            # join the connect pool
            print('connect+'+str(self.duixiang.playing))
            if len(self.g_conn_pool)<=7 and not self.duixiang.playing :
                self.g_conn_pool.append(client)
                msg=client.recv(2048).decode(encoding="utf-8")
                js_xinxi = "1|msg|"  # role info
                biaoji=False
                xuhao=-10
                for i in range(0,len(self.js_xinxi.split("|")[2].split("."))-1):
                    if self.js_xinxi.split("|")[2].split(".")[i]=="-1,no name,no ready" and not biaoji:
                        xuhao=i
                        js_xinxi+=str(msg).split("|")[2]
                        biaoji=True
                        #js+=self.js.split("|")[2].split(".")[i]+"."
                    else:
                        js_xinxi+=self.js_xinxi.split("|")[2].split(".")[i]+"."
                self.js_xinxi=js_xinxi
                self.duixiang.jiexi(self.js_xinxi)
                thread = xianchen.Thread(target=self.message_handle, args=(client,xuhao))
                # thread setting
                thread.setDaemon(True)
                thread.start()
                self.send_player(js_xinxi)
            else:
                print("No")
                client.sendall("NO|".encode("utf8"))

    def message_handle(self,client,wz):
        while True:
            try:
                bytes = client.recv(2048).decode("utf8")  # receive the server
                print(bytes)
                if str(bytes).split("|")[0]=="1":
                    js_xinxi = "1|msg|"
                    for i in range(0,len(self.js_xinxi.split("|")[2].split("."))-1):
                        if i!=wz:
                            js_xinxi+=self.js_xinxi.split("|")[2].split(".")[i]+"."
                        else:
                            js_xinxi+=str(bytes).split("|")[2]
                    self.js_xinxi=js_xinxi
                    self.duixiang.jiexi(self.js_xinxi)
                    self.send_player(self.js_xinxi)
                elif str(bytes).split("|")[0]=="2":
                    if str(bytes).split("|")[1]=="move":
                        self.duixiang.player_play_list[int(str(bytes).split("|")[2].split(".")[0].split(",")[0])].x=int(str(bytes).split("|")[2].split(".")[0].split(",")[1])
                        self.duixiang.player_play_list[int(str(bytes).split("|")[2].split(".")[0].split(",")[0])].y=int(str(bytes).split("|")[2].split(".")[0].split(",")[2])
                        daoju_msg="2|property|"
                        zhi=-1
                        for index,daoju in enumerate(self.duixiang.daoju_list):
                            if int(str(bytes).split("|")[2].split(".")[0].split(",")[1])==daoju.x and int(str(bytes).split("|")[2].split(".")[0].split(",")[2])==daoju.y:
                                zhi=index
                            else:
                                daoju_msg+=str(daoju.x) + "," + str(daoju.y) + ",1," + str(daoju.index) + "."
                        if zhi!=-1:del self.duixiang.daoju_list[zhi]
                        if daoju_msg!=self.daoju_msg:
                            self.send_player(daoju_msg)
                            self.daoju_msg=daoju_msg
                        
                        js_xinxi = "2|move|"
                        for i in range(0,len(self.play_player_move.split("|")[2].split("."))-1):
                            if int(str(bytes).split("|")[2].split(",")[0])==i:
                                js_xinxi+=str(bytes).split("|")[2].split(".")[0].split(",")[1]+","+str(bytes).split("|")[2].split(".")[0].split(",")[2]+"."
                            else:
                                if self.play_player_move.split("|")[2].split(".")[i]=="None":
                                    js_xinxi+="None."
                                else:
                                    js_xinxi+=self.play_player_move.split("|")[2].split(".")[i]+"."
                        self.play_player_move=js_xinxi
                        self.send_player(self.play_player_move)
                        print("move："+self.play_player_move)
                    elif str(bytes).split("|")[1]=="bomb":
                        print("receive:"+bytes)
                        self.bomb_msg+=str(self.duixiang_index[0])+","+str(bytes).split("|")[2].split(",")[0]+","+str(bytes).split("|")[2].split(",")[1]+","+str(bytes).split("|")[2].split(",")[2]+"."
                        self.duixiang.bomb_jiexi(int(str(bytes).split("|")[2].split(",")[0]),int(str(bytes).split("|")[2].split(",")[1]),int(str(bytes).split("|")[2].split(",")[2]),self.duixiang_index[0])
                        #self.duixiang.bomb(Bomb(int(str(bytes).split("|")[2].split(",")[0]),int(str(bytes).split("|")[2].split(",")[1]),self.duixiang.screen,self.duixiang.map_data,str(bytes).split("|")[2].split(",")[2],"paopao",self.duixiang_index[0]))
                        self.duixiang_index[0]+=1
                        print("use")
                        self.send_player(self.bomb_msg)
                    elif str(bytes).split("|")[1]=="chat":
                        self.duixiang.chat_box.add_information(str(bytes).split("|")[2])
                        self.send_player(bytes)
            except :
                
                if not self.duixiang.playing:#in the room
                    js_xinxi = "1|msg|"
                    for i in range(0,len(self.js_xinxi.split("|")[2].split("."))-1):
                        if i!=wz:
                            js_xinxi+=self.js_xinxi.split("|")[2].split(".")[i]+"."
                        else:
                            js_xinxi+="-1,no name,no ready."
                    self.js_xinxi=js_xinxi
                    self.duixiang.jiexi(self.js_xinxi)
                    self.g_conn_pool.remove(client)
                    self.send_player(self.js_xinxi)
                else:#in the game
                    print("Off line")
                    self.g_conn_pool.remove(client)
                    js_xinxi = "1|msg|"
                    for i in range(0,len(self.js_xinxi.split("|")[2].split("."))-1):
                        if i==wz:
                            js_xinxi+="-1,no name,no ready."
                        else:
                            js_xinxi+=self.js_xinxi.split("|")[2].split(".")[i]+"."
                    self.js_xinxi=js_xinxi
                    self.duixiang.jiexi(self.js_xinxi)
                    print("js_xinxi"+self.js_xinxi)
                    play_player_msg = "2|js|"  
                    player_imformation_msg = "2|imformation|"  
                    play_player_move = "2|move|"  
                    play_life_msg = "2|life|"  
                    for i in range(0,len(self.play_player_msg.split("|")[2].split("."))-1):
                        if self.play_player_msg.split("|")[2].split(".")[i]=="None" :
                            play_player_msg += "None."
                            player_imformation_msg += "None."
                            play_player_move += "None."
                            play_life_msg += "None."
                        else:
                            if int(self.play_player_msg.split("|")[2].split(".")[i].split(",")[5]) == wz:
                                self.duixiang.player_play_list[i] = None
                                self.duixiang.play_imformation_list[i] = None
                                play_player_msg += "None."
                                player_imformation_msg += "None."
                                play_player_move += "None."
                                play_life_msg += "None."
                            else:
                                play_player_msg += self.play_player_msg.split("|")[2].split(".")[i]+"."
                                player_imformation_msg += self.player_imformation_msg.split("|")[2].split(".")[i]+"."
                                play_player_move += self.play_player_move.split("|")[2].split(".")[i]+"."
                                play_life_msg += self.play_life_msg.split("|")[2].split(".")[i]+"."
                    self.play_player_msg=play_player_msg
                    self.play_player_move=play_player_move
                    self.player_imformation_msg=player_imformation_msg
                    self.play_life_msg=play_life_msg
                    if self.duixiang.shu_ying==False:
                        shu = 0
                        for i in range(0,len(self.play_life_msg.split("|")[2].split("."))-1):
                            if self.play_life_msg.split("|")[2].split(".")[i]!="None" and self.play_life_msg.split("|")[2].split(".")[i]!="1"  and self.play_life_msg.split("|")[2].split(".")[i]!="2":
                                shu+=1
                        if shu<=1:
                            self.duixiang.end_kuang=end_kuang(self.duixiang.screen,self.duixiang.play_imformation_list,0,0)
                            self.duixiang.shu_ying=True
                            self.send_player("2|end|")
                    self.send_player(play_player_msg)
                break

g = Game()
g.show_start_screen()
while g.running:
    g.run()
    g.show_go_screen()

pg.quit()

