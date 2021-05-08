import pygame, random, sys, time

class Manusia:
    def __init__(self):
        self.x = random.randint(90,400)
        self.y = 540
        self.orang = pygame.image.load('manusia1.png')
        self.orang = pygame.transform.scale(self.orang,(60,110))
        self.kanan = False
        self.kiri = False
        self.sisaNyawa = 3

    def move(self):
        if self.kanan == True:
            if self.x > 570:
                self.x = -20
            else:
                self.x += Permainan.kecepatan
        elif self.kiri == True:
            if self.x < -20:
                self.x = 570
            else:
                self.x -= Permainan.kecepatan
        self.position = [self.x,self.y]

class Number:
    def __init__(self,jenis):
        image = [pygame.image.load('mv0.png'),
                 pygame.image.load('mv1.png'),
                 pygame.image.load('mv2.png'),
                 pygame.image.load('mv3.png'),
                 pygame.image.load('mv4.png'),
                 pygame.image.load('mv5.png'),
                 pygame.image.load('mv6.png'),
                 pygame.image.load('mv7.png'),
                 pygame.image.load('mv8.png'),
                 pygame.image.load('mv9.png')]
        ganjil = [1,3,5,7,9]
        genap = [0,2,4,6,8]
        prima = [1,2,3,5,7]
        pilih = random.randint(0,4)
        if jenis == 'ganjil':
            indeks = ganjil[pilih]
            if pilih == 4:
                self.type = 'ganjil'
            else:
                self.type = 'ganjilPrim'
        elif jenis == 'genap':
            indeks = genap[pilih]
            if pilih == 1:
                self.type = 'genapPrim'
            else:
                self.type = 'genap'
        elif jenis == 'prima':
            indeks = prima[pilih]
            if pilih == 1:
                self.type = 'prima2'
            else:
                self.type = 'prima1'
        self.x = random.randint(9,569)
        self.y = 40
        self.Number = pygame.transform.scale(image[indeks],(30,52))

    def turun(self):
        self.y += Permainan.kecepatan
        self.position = [self.x,self.y]

class Permainan:
    kecepatan = 2
    def __init__(self):
        pygame.init()
        self.font = pygame.font.SysFont('SegoePrint',18)
        self.fontBig = pygame.font.SysFont('SegoePrint',50)
        self.fontBigSmall = pygame.font.SysFont('SegoePrint',23)
        self.window = pygame.display.set_mode((600,650))
        self.window.fill((255,255,255))
        self.bg = pygame.image.load('bg.jpg')
        self.bg = pygame.transform.scale(self.bg,(600,650))
        self.window.blit(self.bg,(0,0))
        self.skorTinggi = 0
        self.st = False
        self.clock = pygame.time.Clock()
        self.window.blit(self.bg,(0,0))
        
    def nyawa(self):
        self.jantung = pygame.image.load('heart.png')
        self.jantung = pygame.transform.scale(self.jantung,(25,25))
        Nyawa = self.font.render('Life :',True,(0,0,0))
        self.window.blit(Nyawa,(445,4))
        life = 1
        poNyawa = 495
        while life <= self.Human.sisaNyawa:
            self.window.blit(self.jantung,(poNyawa,8))
            poNyawa += 32
            life += 1
        poNyawa = 517
        if self.Human.sisaNyawa == 0:
            self.over()
            
    def over(self):
        self.window.fill((0,0,0))
        pygame.draw.rect(self.window,(255,255,255),(0,200,600,170))
        gameOver = self.fontBig.render('GAME OVER',True,(0,0,0))
        self.window.blit(gameOver,(135,195))
        if self.st == True:
            over = self.fontBigSmall.render('SCORE : %d'%self.skor,True,(0,0,0))
            self.window.blit(over,(235,280))
            over = self.fontBigSmall.render('NEW HIGHSCORE : %d'%self.skorTinggi,True,(0,0,0))
            self.window.blit(over,(170,320))
        else:
            over = self.fontBigSmall.render('TINGKATKAN KECEKATAN ANDA',True,(0,0,0))
            self.window.blit(over,(100,280))
            over = self.fontBigSmall.render('HIGHSCORE : %d'%self.skorTinggi,True,(0,0,0))
            self.window.blit(over,(195,320))
        pygame.display.update()
        time.sleep(4)
        self.menu()
    
    def start(self,mission):
        self.window.fill((0,0,0))
        pygame.draw.rect(self.window,(255,255,255),(0,200,600,170))
        if mission == 1:
            gameOver = self.font_judul.render('~~~ MISI ANDA ~~~',True,(0,0,0))
            self.window.blit(gameOver,(130,210))
            over = self.fontBigSmall.render('Tangkap Bilangan Genap,',True,(0,0,0))
            self.window.blit(over,(15,265))
            over = self.fontBigSmall.render('dan Hindari Bilangan Ganjil Kalau Kau Bisa.',True,(0,0,0))
            self.window.blit(over,(15,305))
        elif mission == 2:
            gameOver = self.font_judul.render('~~~ MISI ANDA ~~~',True,(0,0,0))
            self.window.blit(gameOver,(130,210))
            over = self.fontBigSmall.render('Ambil Bilangan Ganjil,',True,(0,0,0))
            self.window.blit(over,(15,265))
            over = self.fontBigSmall.render('dan Hindari Bilangan Genap.',True,(0,0,0))
            self.window.blit(over,(15,305))
        elif mission == 3:
            gameOver = self.font_judul.render('~~~ MISI ANDA ~~~',True,(0,0,0))
            self.window.blit(gameOver,(130,210))
            over = self.fontBigSmall.render('Misimu adalah menangkap bilangan Prima,',True,(0,0,0))
            self.window.blit(over,(15,265))
            over = self.fontBigSmall.render('dan Buktikan Bahwa Kamu Bisa.',True,(0,0,0))
            self.window.blit(over,(15,305))
        elif mission == 4:
            pygame.quit()
            sys.exit()
        else:
            for i in range(3):
                print("There is a problem")
        pygame.display.update()
        time.sleep(5)
        self.main()

    def menu(self):
        font_menu = pygame.font.SysFont('SegoePrint',25)
        self.font_judul = pygame.font.SysFont('SegoePrint',30)
        panah = pygame.image.load('panahMerah.png')
        panah = pygame.transform.scale(panah,(80,30))
        yPanah = [208,253,298,343]
        self.window.blit(self.bg,(0,0))
        self.window.blit(panah,(50,208))
        pygame.display.update()
        loop = True
        self.pilih = 1
        pilih = False
        while loop == True:
            self.window.blit(self.bg,(0,0))
            judul = self.font_judul.render('~ Mathematic Mission ~',True,(0,0,0))
            menu = font_menu.render('MENU >>>',True,(0,0,0))
            mission1 = font_menu.render('1. Misi Genap',True,(0,0,0))
            mission2 = font_menu.render('2. Misi Ganjil',True,(0,0,0))
            mission3 = font_menu.render('3. Misi Prima',True,(0,0,0))
            mission4 = font_menu.render('4. Keluar',True,(0,0,0))
            self.window.blit(judul,(100,60))
            foot = self.font.render('Version 2.5',True,(0,0,0))
            self.window.blit(foot,(475,610))
            self.window.blit(menu,(30,150))
            self.window.blit(mission1,(140,200))
            self.window.blit(mission2,(140,245))
            self.window.blit(mission3,(140,290))
            self.window.blit(mission4,(140,335))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.menu()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.pilih -= 1
                        if self.pilih < 1:
                            self.pilih = 4
                        if self.pilih > 0 and self.pilih < 5:
                            pilih = True
                            self.window.blit(panah,(50,yPanah[self.pilih-1]))
                    if event.key == pygame.K_DOWN:
                        self.pilih += 1
                        if self.pilih > 4:
                            self.pilih = 1
                        if self.pilih > 0 and self.pilih < 5:
                            pilih = True
                            self.window.blit(panah,(50,yPanah[self.pilih-1]))
                    if event.key == pygame.K_RETURN:
                        loop = False
                        self.start(self.pilih)
            self.window.blit(panah,(50,yPanah[self.pilih-1]))
            pygame.display.update()
        

    def mSkor(self):
        if self.pilih == 1:
            berkas = open('skorM1','r')
            for i in berkas:
                self.skorTinggi = int(i)
            if self.skor > self.skorTinggi:
                file = open('skorM1','w')
                file.write('%d'%self.skor)
                self.st = True
        elif self.pilih == 2:
            berkas = open('skorM2','r')
            for i in berkas:
                self.skorTinggi = int(i)
            if self.skor > self.skorTinggi:
                file = open('skorM2','w')
                file.write('%d'%self.skor)
                self.st = True
        elif self.pilih == 3:
            berkas = open('skorM3','r')
            for i in berkas:
                self.skorTinggi = int(i)
            if self.skor > self.skorTinggi:
                file = open('skorM3','w')
                file.write('%d'%self.skor)
                self.st = True
        elif self.pilih == 4:
            pygame.quit()
            sys.exit()
        else:
            print('ada masalah ==> self.pilih =',self.pilih)
        s = self.font.render('Score : %d'%self.skor,True,(0,0,0))
        h = self.font.render('HighScore : %d'%self.skorTinggi,True,(0,0,0))
        self.window.blit(s,(8,0))
        self.window.blit(h,(8,26))

    def main(self):
        Permainan.kecepatan = 2
        fontError = pygame.font.SysFont('SegoePrint',30)
        nyawaBerkurang = False
        self.Human = Manusia()
        self.skor = 0
        self.Human.sisaNyawa = 3
        self.food = []
        isi = ['genap','ganjil','prima']
        self.food.append(Number(isi[random.randint(0,2)]))
        while True:
            self.clock.tick(50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.over()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.Human.kiri = True
                    if event.key == pygame.K_RIGHT:
                        self.Human.kanan = True
                elif event.type == pygame.KEYUP:
                    if (event.key == pygame.K_LEFT) or (event.key == pygame.K_RIGHT):
                        self.Human.kanan = False
                        self.Human.kiri = False
            for k in self.food:
                if k.y > 650:
                    self.food.remove(k)
            if len(self.food) == 0:
                self.food.append(Number(isi[random.randint(0,2)]))
            if self.food[len(self.food)-1].y > 90:
                x = random.randint(0,2)
                self.food.append(Number(isi[x]))
            for j in self.food:
                j.turun()
                self.window.blit(j.Number,(j.x,j.y))
            pygame.display.update()
            self.Human.move()
            self.window.blit(self.bg,(0,0))
            self.window.blit(self.Human.orang,(self.Human.x,self.Human.y))
            for q in self.food:
                if q.position[1]+30 > self.Human.position[1] and q.position[1] < self.Human.position[1]+110:
                    if q.position[0] < self.Human.position[0]+60 and q.position[0]+30 > self.Human.position[0]:
                        if self.pilih == 1: # UNTUK MISI 1
                            if q.type == 'genap' or q.type == 'prima2' or q.type == 'genapPrim':
                                self.food.remove(q)
                                self.skor += 10
                            elif q.type == 'ganjil' or q.type == 'prima1' or q.type == 'ganjilPrim':
                                self.food.remove(q)
                                self.Human.sisaNyawa -= 1
                                nyawaBerkurang = True
                        elif self.pilih == 2: # UNTUK MISI 2
                            if q.type == 'ganjil' or q.type == 'prima1' or q.type == 'ganjilPrim':
                                self.food.remove(q)
                                self.skor += 10
                            elif q.type == 'genap' or q.type == 'prima2' or q.type == 'genapPrim':
                                self.food.remove(q)
                                self.Human.sisaNyawa -= 1
                                nyawaBerkurang = True
                        elif self.pilih == 3: # UNTUK MISI 3
                            if q.type == 'prima2' or q.type == 'prima1' or q.type == 'genapPrim' or q.type == 'ganjilPrim':
                                self.food.remove(q)
                                self.skor += 10
                            elif q.type == 'genap' or q.type == 'ganjil':
                                self.food.remove(q)
                                self.Human.sisaNyawa -= 1
                                nyawaBerkurang = True
                if nyawaBerkurang == True and self.Human.sisaNyawa > 0:
                    for i in range(4):
                        self.window.blit(self.bg,(0,0))
                        self.mSkor()
                        self.nyawa()
                        pygame.display.update()
                        time.sleep(0.5)
                        warning = fontError.render('NYAWA ANDA BERKURANG',True,(255,0,0))
                        self.window.blit(self.bg,(0,0))
                        self.window.blit(warning,(75,80))
                        self.mSkor()
                        self.nyawa()
                        self.window.blit(self.Human.orang,(self.Human.x,self.Human.y))
                        pygame.display.update()
                        time.sleep(1)
                    nyawaBerkurang = False
                    self.food = []
                self.nyawa()
            Permainan.kecepatan += 0.009
            self.mSkor()
        
if __name__ == '__main__':
    start = Permainan()
    start.menu()
