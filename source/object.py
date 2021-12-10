import random
import pygame as pg
import pygame.image

from settings import *


class Player():
    def __init__(self, x, y,screen,pifu):
        self.screen = screen
        self.die_image=[]
        self.die=0#0表示活着 1表示在泡泡里 2表示死亡
        self.pifu=pifu
        """
        宝宝初始 泡泡个数 泡泡范围 1  1 完美是 5   7
        蓝蓝初始 泡泡个数 泡泡范围 2  1 完美是 7   5
        """
        self.image=None
        if self.pifu==1:
            self.die_image=[pygame.image.load("image/baobao/1.png"),pygame.image.load("image/baobao/1.png"),pygame.image.load("image/baobao/2.png"),pygame.image.load("image/baobao/3.png"),
                            pygame.image.load("image/baobao/2.png"),pygame.image.load("image/baobao/3.png"),pygame.image.load("image/baobao/2.png"),pygame.image.load("image/baobao/3.png"),
                            pygame.image.load("image/baobao/2.png"),pygame.image.load("image/baobao/3.png"),pygame.image.load("image/baobao/2.png"),pygame.image.load("image/baobao/3.png"),
                            pygame.image.load("image/baobao/2.png"), pygame.image.load("image/baobao/3.png"),pygame.image.load("image/baobao/2.png"), pygame.image.load("image/baobao/3.png"),
                            pygame.image.load("image/baobao/4.png"),pygame.image.load("image/baobao/5.png"),pygame.image.load("image/baobao/6.png"),pygame.image.load("image/baobao/8.png"),
                            None,pygame.image.load("image/baobao/7.png"),None,pygame.image.load("image/baobao/7.png"),None,pygame.image.load("image/baobao/7.png"),
                            None,pygame.image.load("image/baobao/7.png"),None,pygame.image.load("image/baobao/7.png"),None,pygame.image.load("image/baobao/7.png"),
                            None, pygame.image.load("image/baobao/7.png"), None, pygame.image.load("image/baobao/7.png"), None, pygame.image.load("image/baobao/7.png")]
            self.image = pg.image.load("image/player.png")
        elif self.pifu==2:
            self.die_image=[pygame.image.load("image/marid/1.png"),pygame.image.load("image/marid/1.png"),pygame.image.load("image/marid/2.png"),pygame.image.load("image/marid/3.png"),
                            pygame.image.load("image/marid/2.png"),pygame.image.load("image/marid/3.png"),pygame.image.load("image/marid/2.png"),pygame.image.load("image/marid/3.png"),
                            pygame.image.load("image/marid/2.png"),pygame.image.load("image/marid/3.png"),pygame.image.load("image/marid/2.png"),pygame.image.load("image/marid/3.png"),
                            pygame.image.load("image/marid/2.png"), pygame.image.load("image/marid/3.png"),pygame.image.load("image/marid/2.png"), pygame.image.load("image/marid/3.png"),
                            pygame.image.load("image/marid/4.png"),pygame.image.load("image/marid/5.png"),pygame.image.load("image/marid/6.png"),pygame.image.load("image/marid/8.png"),
                            None,pygame.image.load("image/marid/7.png"),None,pygame.image.load("image/marid/7.png"),None,pygame.image.load("image/marid/7.png"),
                            None,pygame.image.load("image/marid/7.png"),None,pygame.image.load("image/marid/7.png"),None,pygame.image.load("image/marid/7.png"),
                            None, pygame.image.load("image/marid/7.png"), None, pygame.image.load("image/marid/7.png"), None, pygame.image.load("image/marid/7.png")]
            self.image = pg.image.load("image/player3.png")
        #player 's outlook color etc
        #self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.hp = 2
        self.die_zhen=0
        self.shanshuo_zhen = 0
        self.cishu = 15
        self.time = 8
        self.fanwei = 5#炸弹范围
        self.shuliang = 1#炸弹数量
        self.pifu=pifu
        #17帧是被怪物和人撞到的效果
    # move the player function
    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy
    def hurt(self):
        self.shanshuo_zhen = 1
    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE
        if self.die<2:
            if self.die==0:
                if self.shanshuo_zhen == 1:
                    self.time -= 1
                    if self.time == 0:
                        self.cishu -= 1
                        self.time = 8
                        if self.cishu == 0:
                            self.shanshuo_zhen=0
                            self.cishu=15
                    if self.cishu % 2 == 1:
                        self.image.set_alpha(100)
                    else:
                        self.image.set_alpha(255)
                self.screen.blit(self.image, (self.rect.x,self.y * TILESIZE))
            elif self.die==1:
                if self.die_zhen+1==len(self.die_image):
                    self.die=2
                if self.time>=8:
                    self.die_zhen+=1
                    self.time=0
                self.time+=1
                if self.die_image[self.die_zhen] != None:
                    self.screen.blit(self.die_image[self.die_zhen], (self.rect.x,self.y * TILESIZE))
    def zuobiaox(self):
        return self.x
    def zuobiaoy(self):
        return self.y
class Wall():
    def __init__(self,screen, x, y,leixing):
        self.screen = screen
        if leixing=="stone":
            self.image = pygame.image.load("image/fangkuai/stone.png")
        elif leixing=="wall":
            self.image = pygame.image.load("image/fangkuai/wall.png")
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
    def update(self):
        self.screen.blit(self.image,(self.rect.x,self.rect.y))
class Play_imformation():
    def __init__(self,screen,js_leixing,name,xuhao):
        self.screen=screen
        self.zhuang_tai=0 #0为正常1为哭泣状态
        self.js=None
        self.js_die=None
        if js_leixing==1:
            self.js=pg.image.load("image/play_imformation/baobao_icon.png")
            self.js_die=pg.image.load("image/play_imformation/baobao_cry_icon.png")
        elif js_leixing==2:
            self.js=pg.image.load("image/play_imformation/lanlan_icon.png")
            self.js_die=pg.image.load("image/play_imformation/lanlan_cry_icon.png")
        self.dengji=pg.image.load("image/play_imformation/grade.png")
        self.my_font = pygame.font.SysFont('SimHei', 16)
        self.name=name
        self.name_message = self.my_font.render(self.name, True, (255,255,255), (12, 116, 208))
        self.xuhao=xuhao
    def update(self):
        if self.zhuang_tai==0:
            self.screen.blit(self.js,(1070,153+self.xuhao*64))
        else:
            self.screen.blit(self.js_die,(1070,153+self.xuhao*64))
        self.screen.blit(self.dengji,(1141,155+self.xuhao*64))
        self.screen.blit(self.name_message,(1138,181+self.xuhao*64))
class player_icons():
    def __init__(self,screen,pifu,name,xh,zhunbei):
        self.name=name
        self.my_font = pygame.font.SysFont('SimHei', 16)
        self.name_message = self.my_font.render(self.name, True, (255,255,255))
        self.ready_img=pygame.image.load("BNB/准备.png")
        self.ready=False
        if zhunbei=="ready":self.ready=True
        self.screen=screen
        self.xuhao=xh#表示位置
        if pifu==1:
            self.hero_icon=pygame.image.load("BNB/baobao.png")
        else:
            self.hero_icon=pygame.image.load("BNB/lanlan.png")
        self.rect = self.hero_icon.get_rect()
        self.rect.x = 45 + 159 * xh + 6
        self.rect.y = 280 + 220 * (self.xuhao //4) - self.rect.height
    def update(self):
        #名字和角色都渲染
        self.screen.blit(self.hero_icon,(self.rect.x,self.rect.y))
        self.screen.blit(self.name_message,(52+160*self.xuhao,300+220*(self.xuhao //4)))
        #74 327
        if self.ready:self.screen.blit(self.ready_img,(43+160*self.xuhao,323+220*(self.xuhao //4)))
class Box():
    def __init__(self, screen, x, y,xuhao,leixing):
        self.screen=screen
        self.xuhao=xuhao
        if leixing=="box":
            self.image = pg.image.load("image/fangkuai/box.png")
        elif leixing=="orange_box":
            self.image=pg.image.load("image/fangkuai/orange_box.png")
        elif leixing=="red_box":
            self.image=pg.image.load("image/fangkuai/red_box.png")
        self.die_image=[pg.image.load("image/box_Explosive effect/Explosive effect1.png"),pg.image.load("image/box_Explosive effect/Explosive effect2.png"),
                        pg.image.load("image/box_Explosive effect/Explosive effect3.png"),pg.image.load("image/box_Explosive effect/Explosive effect4.png"),
                        None,pg.image.load("image/box_Explosive effect/Explosive effect4.png"),None,pg.image.load("image/box_Explosive effect/Explosive effect4.png")]
        self.die_zhen=0
        self.time=0
        self.x = x
        self.y = y
        self.die=0# 0为正常 1为被水泡炸到后的效果 2为效果结束[删除]
        self.daoju=random.randint(1,6)
    def update(self):
        if self.die==0:
            self.screen.blit(self.image,(self.x*33,self.y*33))
        if self.die==1:
            if self.die_zhen + 1 == len(self.die_image):
                self.die = 2
            if self.time >= 8:
                self.die_zhen += 1
                self.time = 0
            self.time += 1
            if self.die_image[self.die_zhen] != None:
                self.screen.blit(self.die_image[self.die_zhen], (self.x*33,self.y*33))
class Bomb():
    def __init__(self,x,y,screen,ditu,fanwei,msg,index):
        self.ditu=ditu
        self.index=index
        self.screen=screen
        self.msg=msg
        self.bomb_image=[]
        self.baozha_image=[]
        a = random.randint(0, 3)
        if a==0:
            for i in range(1,5):
                self.bomb_image.append(pg.image.load("image/bomb/bomb"+str(i)+".png"))
        elif a==1:
            for i in range(1,5):
                self.bomb_image.append(pg.image.load("image/bomb/mqj_bomb"+str(i)+".png"))
        elif a==2:
            for i in range(1,5):
                self.bomb_image.append(pg.image.load("image/bomb/dimo_bomb"+str(i)+".png"))
        else:
            for i in range(1,5):
                self.bomb_image.append(pg.image.load("image/bomb/milk_bomb"+str(i)+".png"))
        for i in range(1,5):
            self.baozha_image.append(pg.image.load("image/xiaoguo-"+str(i)+".png"))
        self.donghua_time=0
        self.zhen=0#泡泡动画帧数
        self.time=250#爆炸time
        self.x=x
        self.y=y
        self.fanwei=fanwei#泡泡范围
        self.left=-self.fanwei
        self.right=self.fanwei+1
        self.top=-self.fanwei
        self.down=self.fanwei+1
        self.baozha_list=[]
        self.Indestructible_Cube="12456789"# 不可被炸方块 3是表示爆炸
        self.Explosive_Cube="abcdcfg"# 可被炸方块
        #self.baozha_list=[]
        #32x32
    def list(self):
        return self.baozha_list
    def update(self):
        #4边检查箱子就不要-1
        self.time-=1
        if self.time==60:
            for i in range(-1,-1*self.fanwei-1,-1):
                if self.ditu[self.y][self.x+i] in self.Indestructible_Cube:
                    self.left = i+1
                    break
                elif self.ditu[self.y][self.x+i] in self.Explosive_Cube:
                    self.left= i+1
                    self.baozha_list.append([self.x+i,self.y])
                    break
            for i in range(0,1*self.fanwei+1):
                if self.ditu[self.y][self.x+i] in self.Indestructible_Cube :
                    self.right = i
                    break
                elif self.ditu[self.y][self.x+i] in self.Explosive_Cube:
                    self.right= i
                    self.baozha_list.append([self.x+i,self.y])
                    break
            for i in range(-1,-1*self.fanwei-1,-1):
                if self.ditu[self.y+i][self.x] in self.Indestructible_Cube:
                    self.top = i+1
                    break
                elif self.ditu[self.y+i][self.x] in self.Explosive_Cube:
                    self.top= i+1
                    self.baozha_list.append([self.x,self.y+i])
                    break
            for i in range(0,1*self.fanwei+1):
                if self.ditu[self.y+i][self.x] in self.Indestructible_Cube :
                    self.down = i
                    break
                elif self.ditu[self.y+i][self.x] in self.Explosive_Cube:
                    self.down= i
                    self.baozha_list.append([self.x,self.y+i])
                    break
            for i in range(self.top,self.down):
                self.ditu[self.y+i]=self.ditu[self.y+i][:self.x]+"3"+self.ditu[self.y+i][self.x+1:]
            for i in range(self.left,self.right):
                if i!=0:
                    self.ditu[self.y]=self.ditu[self.y][:self.x+i]+"3"+self.ditu[self.y][self.x+i+1:]
        elif self.time==0:
            for i in range(self.top,self.down):
                if self.ditu[self.y+i][self.x]=="3":
                    self.ditu[self.y+i]=self.ditu[self.y+i][:self.x]+"."+self.ditu[self.y+i][self.x+1:]
            for i in range(self.left,self.right):
                if i!=0:
                    self.ditu[self.y]=self.ditu[self.y][:self.x+i]+"."+self.ditu[self.y][self.x+i+1:]
        elif 0<self.time<=60:
            for i in range(self.top,self.down):
                if self.ditu[self.y+i][self.x]!="3":
                    self.ditu[self.y+i]=self.ditu[self.y+i][:self.x]+"3"+self.ditu[self.y+i][self.x+1:]
            for i in range(self.left,self.right):
                if i!=0:
                    self.ditu[self.y]=self.ditu[self.y][:self.x+i]+"3"+self.ditu[self.y][self.x+i+1:]
            for i in range(self.top, self.down):
                if i <=0:
                    self.screen.blit(self.baozha_image[1], ((self.x) * 33, (self.y + i) * 33))
                else:
                    self.screen.blit(self.baozha_image[3], ((self.x) * 33, (self.y + i) * 33))
            for i in range(self.left, self.right):
                if i<0:
                    self.screen.blit(self.baozha_image[0], ((self.x + i) * 33, self.y * 33))
                else:
                    self.screen.blit(self.baozha_image[2], ((self.x + i) * 33, self.y * 33))
        else:
            self.donghua_time+=1
            if self.donghua_time==15:
                self.zhen+=1
                self.donghua_time=0
            if self.zhen>3:
                self.zhen=0
            self.screen.blit(self.bomb_image[self.zhen],(self.x*33,self.y*33))


class Robot():
    def __init__(self,screen,ditu,zt):#人机自带x,y不需要
        self.screen=screen
        self.ditu=ditu
        self.zt=zt#状态的话 1是 动的 2 是通过传输信息给人机位置
        self.y=random.randint(1,len(self.ditu)-1)
        self.image=pg.image.load("image/monster.png")
        self.image1=pg.image.load("image/monster1.png")
        self.hp=2#代表血量
        self.fx=0#表示方向
        self.time=100
        self.shanshuo_zhen = 0
        self.cishu = 15
        self.time1 = 8
        self.fanwei=2
        self.shuliang=1
        while True:
            self.x=random.randint(1,len(self.ditu)-1)
            if self.ditu[self.y][self.x] == ".":
                break
    def move(self,ditu):
        if self.zt !=2:
            self.time-=1
            if self.time==0:
                self.time=random.randint(50,120)
                self.fx=random.randint(1,4)
            if self.fx>0:
                self.ditu=ditu
                if self.fx==1:
                    if self.ditu[self.y][self.x-1]==".":
                        self.x-=1
                elif self.fx==2:
                    if self.ditu[self.y-1][self.x] == ".":
                        self.y -= 1
                elif self.fx==3:
                    if self.ditu[self.y][self.x+1] == ".":
                        self.x += 1
                elif self.fx==4:
                    if self.ditu[self.y+1][self.x] == ".":
                        self.y += 1
                self.fx=0
    def suiji(self):
        return random.randint(1,10)
    def fangzhi_zhadan(self):
        if self.zt!=2:
            a=random.randint(1,1000)
            if a == 1:
                return True
    def hurt(self):
        self.shanshuo_zhen=1
        self.hp-=1
    def update(self,ditu):
        self.move(ditu)
        if self.shanshuo_zhen == 1:
            self.time1 -= 1
            if self.time1 == 0:
                self.cishu -= 1
                self.time1 = 8
                if self.cishu == 0:
                    self.shanshuo_zhen=0
                    self.cishu=15
            if self.cishu % 2 == 1:
                self.screen.blit(self.image,(self.x*32,self.y*32))
            else:
                self.screen.blit(self.image1,(self.x*32,self.y*32))
        else:
            self.screen.blit(self.image, (self.x*32, self.y*32))
class Daoju():
    def __init__(self,screen,x,y,id,index):
        self.image=pg.image.load("image/道具.png")
        self.image1=pg.image.load("image/yaoshui.png")
        self.screen=screen
        self.index=index
        self.x=x
        self.y=y
        self.pianyi=0#y轴移动
        self.bianliang=0.15
        self.daoju=None
        self.id=id
        if self.id==1:#1为炸弹数量
            self.daoju=self.image
        elif self.id==2:#2为炸弹范围
            self.daoju=self.image1
    def update(self):
        if self.pianyi<=-15 or self.pianyi>=0:
            self.bianliang=-self.bianliang
        self.pianyi+=self.bianliang
        self.screen.blit(self.daoju,(self.x*33,self.y*33+self.pianyi))
    @staticmethod
    def jiance(id):
        if id<=2:
            return True
        else:
            return False

class chat_box():
    def __init__(self,screen,duixiang,sever,sf):
        self.sf=sf
        self.screen=screen#当前窗口
        self.sever=sever#绑定服务器实现指令传输
        self.duixiang=duixiang#游戏类
        self.ground=pg.image.load("image/black.png")
        self.chat_list=[]#记录信息update便利渲染
        self.name=self.duixiang.name #记录的是自己的游戏名字
        self.useing=False
        self.current_content=""
        self.content_update=None
        #初始化字体类型
        self.my_font = pygame.font.SysFont('SimHei', 35)
        self.time=100
    def update(self):
        if self.useing:
            self.screen.blit(self.ground,(0,718))
            self.screen.blit(self.content_update,(0,718))
        if len(self.chat_list)>0:
            for index,i in enumerate(self.chat_list):
                self.screen.blit(i,(10,index*35+500))
            self.time-=1
            if self.time==0:
                self.time=100
                del self.chat_list[0]
    def event(self,event_val):
        if event_val==13:
            if self.useing:
                if len(self.current_content)>0:
                    #根据指令信息判断
                    if self.sf=="sever":
                        if len(self.chat_list) < 6:
                            self.chat_list.append(
                                self.my_font.render(self.name + ":" + self.current_content, True, (0,0,139)))
                        else:
                            del self.chat_list[0]
                            self.chat_list.append(self.my_font.render(self.name + ":" + self.current_content, True, (0,0,139)))
                        self.sever.send_player("2|chat|" + self.name + ":" + self.current_content)
                    else:
                        self.sever.sendall(("2|chat|" + self.name + ":" + self.current_content).encode("utf8"))
                    self.current_content=""
                    self.time=100
                else:
                    self.useing=False
                    self.current_content=""
            else:
                self.useing=True
                self.current_content = ""
        if self.useing:
            if len(self.current_content)>0:
                if event_val==8:self.current_content=self.current_content[:-1]
            if 97<=event_val<=122:
                self.current_content+=chr(event_val)
            elif 1073741913<=event_val<=1073741922:
                self.current_content+=chr((48+event_val-1073741913))
            elif event_val==32:
                self.current_content+=" "
            self.content_update=self.my_font.render(self.current_content, True, (255, 255, 255), (12, 116, 208))
    def add_information(self,msg):
        if len(self.chat_list) < 6:
            self.chat_list.append(self.my_font.render(msg, True, (0,0,139)))
        else:
            del self.chat_list[0]
            self.chat_list.append(self.my_font.render(msg, True, (0,0,139)))
        self.time=100
class ghost():
    def __init__(self,screen,map):
        self.screen=screen
        self.map=map
        self.y=random.randint(1,len(self.map)-2)
        self.x=None
        while True:
            shu=random.randint(0,len(self.map[self.y])-1)
            if self.map[self.y][shu]==".":
                self.x=shu
                break
        self.born=False
        self.born_image=[]
        self.left_image=[]
        self.right_image=[]
        self.top_image=[]
        self.down_image=[]
        self.die_image=[]
        self.time=30
        self.zhen=0
        self.fx=0
        self.jineng_time=10#冲刺时间倒计时
        self.use_jineng=False
        self.chongci_donghua=False
        self.die=0
        for i in range(1,5):
            if i<=3:
                self.born_image.append(pg.image.load("image/ghost/youling_xiaoguo"+str(i)+".png"))
            self.left_image.append(pg.image.load("image/ghost/youling_zuo"+str(i)+".png"))
            self.right_image.append(pg.image.load("image/ghost/youling_you"+str(i)+".png"))
            self.top_image.append(pg.image.load("image/ghost/youling_shang"+str(i)+".png"))
            self.down_image.append(pg.image.load("image/ghost/youling_xia"+str(i)+".png"))
        self.use_image=self.down_image[0]#默认为正面
        for i in range(3,0,-1):
            self.die_image.append(pg.image.load("image/ghost/youling_xiaoguo"+str(i)+".png"))
    def update(self):
        if self.die==1:
            self.time -= 1
            self.screen.blit(self.die_image[self.zhen], (self.x * 33, self.y * 33))
            if self.time == 0:
                self.zhen += 1
                self.time = 12
            if self.zhen == 3:
                self.die=2
        else:
            if not self.born:
                self.time-=1
                self.screen.blit(self.born_image[self.zhen],(self.x*33,self.y*33))
                if self.time==0:
                    self.zhen+=1
                    self.time=12
                if self.zhen==3:
                    self.born=True
            else:
                if self.map[self.y][self.x]=="3":
                    self.zhen=0
                    self.die=1
                if self.use_jineng:
                    self.chongci()
                else:
                    if self.time==0:
                        self.time=30
                        while True:
                            shu=random.randint(0,3)
                            if shu==0:
                                if self.map[self.y][self.x-1]==".":
                                    self.x-=1
                                    self.use_image=self.left_image[0]
                            elif shu==1:
                                if self.map[self.y-1][self.x]==".":
                                    self.y-=1
                                    self.use_image=self.top_image[0]
                            elif shu==2:
                                if self.map[self.y][self.x+1]==".":
                                    self.x+=1
                                    self.use_image=self.right_image[0]
                            elif shu==3:
                                if self.map[self.y+1][self.x]==".":
                                    self.y+=1
                                    self.use_image=self.down_image[0]
                            break
                    if self.jineng_time==0:
                        self.zhen=0
                        self.jineng_time=300
                        self.chongci_donghua=False
                        self.use_jineng=True
                        self.fx=random.randint(0,3)
                    self.jineng_time-=1
                    self.screen.blit(self.use_image,(self.x*33,self.y*33))
                    self.time -= 1
    def chongci(self):
        if not self.chongci_donghua:
            self.time -= 1
            if self.fx==0:
                self.use_image=self.left_image[self.zhen]
            elif self.fx==1:
                self.use_image=self.top_image[self.zhen]
            elif self.fx==2:
                self.use_image=self.right_image[self.zhen]
            elif self.fx==3:
                self.use_image=self.down_image[self.zhen]
            if self.time == 0:
                self.time=15
                self.zhen += 1
            if self.zhen == 4:
                self.chongci_donghua = True
        else:
            if self.time==0:
                self.time=4
                if self.fx==0:
                    if self.map[self.y][self.x-1]==".":
                        self.x-=1
                    else:
                        self.use_jineng=False
                        self.zhen=0
                elif self.fx==1:
                    if self.map[self.y-1][self.x]==".":
                        self.y-=1
                    else:
                        self.use_jineng=False
                        self.zhen=0
                elif self.fx==2:
                    if self.map[self.y][self.x+1]==".":
                        self.x+=1
                    else:
                        self.use_jineng=False
                        self.zhen=0
                elif self.fx==3:
                    if self.map[self.y+1][self.x]==".":
                        self.y+=1
                    else:
                        self.use_jineng=False
                        self.zhen=0
            self.time-=1
        self.screen.blit(self.use_image, (self.x * 33, self.y * 33))
class end_kuang():
    def __init__(self,screen,people_list,xuhao,me_xuhao):
        self.people_list = people_list
        self.screen = screen
        if xuhao==None:
            self.win= False
        else:
            if xuhao==me_xuhao:
                self.win = True
            else:
                self.win= False# this is win player id
        self.win_index=xuhao
        self.x = 150
        self.y = 120
        #按顺序为 结束框 胜利 min胜利 失败 min失败
        self.End_Interface=pg.image.load("image/end/End Interface.png")
        self.victory=pg.image.load("image/end/victory.png")
        self.small_vicroty=pg.image.load("image/end/small_victory.png")
        self.defeat=pg.image.load("image/end/defeat.png")
        self.small_defeat=pg.image.load("image/end/small_defeat.png")
        self.grade=pg.image.load("image/end/grade.png")
        self.blue=pg.image.load("image/end/blue_tiao.png")
        self.end_list=[]
        for i in range(1,9):
            self.end_list.append(pg.image.load("image/end/"+str(i)+".png"))
        self.my_font = pygame.font.SysFont('SimHei', 16)
        self.name=""
    def update(self):
        self.screen.blit(self.End_Interface,(self.x,self.y))
        index=0
        i=0
        if self.win:
            self.screen.blit(self.victory,(self.x+220,20))
        else:
            self.screen.blit(self.defeat,(self.x+220,20))
        for index,i in enumerate(self.people_list):
            if i!=None:
                self.screen.blit(self.end_list[index],(self.x+32,self.y+63+index*30+3))
                self.name = self.people_list[index].name
                self.name_message = self.my_font.render(self.name, True, (255, 255, 255))
                if self.win_index==index:
                    self.screen.blit(self.small_vicroty,(self.x+59,self.y+63+index*30+1))
                else:
                    self.screen.blit(self.small_defeat,(self.x+59,self.y+63+index*30+1))
                self.screen.blit(self.grade,(self.x+171,self.y+63+index*30+6))
                self.screen.blit(self.name_message,(self.x+195,self.y+63+index*30+6))
