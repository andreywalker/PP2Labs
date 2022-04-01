import pygame
pygame.init()
#screen
WIN = pygame.display.set_mode((500, 170))
pygame.display.set_caption("Music Player")

#var
songs = ["music.mp3", "crossoff.mp3"]
song_num = 0
isPlay = False
clock = pygame.time.Clock()
ended = pygame.USEREVENT + 0
BLUE = (106, 199, 209)
GREEN = (187, 233, 178)
DARK_GREEN = (142, 175, 135)
font1 = pygame.font.SysFont("Arial", 36)
font = pygame.font.SysFont("Arial", 36)
volume = 0.1
text1 = "PLAY"
text2 = "PAUSE"
text3 = "NEXT"
text4 = "BACK"
pt = text1
pp = (215, 55)
volume_c = False
volume_s = 0.02

#func
def song_pl(num):
    pygame.mixer.music.load(songs[num])
    pygame.mixer.music.play(0)

def ch_num(num):
    global song_num
    if song_num + num >= len(songs):
        song_num = 0
    elif song_num + num < 0:
        song_num = len(songs) - 1
    else:
        song_num += num

def vol_draw():
    pygame.draw.line(WIN, DARK_GREEN, (50, 155), (450, 155), 6)
    pygame.draw.line(WIN, GREEN, (50, 155), (400*volume + 50, 155), 8)
    pygame.draw.circle(WIN, GREEN, (400*volume + 50, 155), 10)

class button:
    def __init__(self, acolor, icolor, pos, rad):
        self.acolor = self.ac = acolor
        self.icolor = self.ic = icolor
        self.pos = pos
        self.rad = rad

    def draw(self, win, text, b_pos, change = False):
        if change:
            self.change_color()
        else:
            self.acolor = self.ac
            self.icolor = self.ic
        pygame.draw.circle(win, self.acolor, self.pos, self.rad)
        txt = font.render(text, True, self.icolor)
        win.blit(txt, b_pos)
    
    def change_color(self):
        cashe_color = self.acolor
        self.acolor = self.icolor
        self.icolor = cashe_color

play_but = button(GREEN, DARK_GREEN, (250, 75), 60)
next_but = button(GREEN, DARK_GREEN, (360, 75), 45)
back_but = button(GREEN, DARK_GREEN, (140, 75), 45)

def play():
    global isPlay, pt, pp
    if isPlay:
        isPlay = False
        pygame.mixer.music.pause()
        pt = text1
        pp = (215, 55)
    else:
        isPlay = True
        pygame.mixer.music.unpause()
        pt = text2
        pp = (200, 55)

#start con
pygame.mixer.music.load(songs[song_num])
pygame.mixer.music.play()
pygame.mixer.music.pause()
pygame.mixer.music.set_endevent(ended)

run = True
while run:
    WIN.fill(BLUE)
    play_but.draw(WIN, pt, pp)
    next_but.draw(WIN, text3, (320, 55))
    back_but.draw(WIN, text4, (100, 55))
    pygame.mixer.music.set_volume(volume)
    clock.tick(60)
    vol_draw()
    m_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                next_but.draw(WIN, text3, (320, 55), True)
                isPlay = True
                ch_num(1)
                song_pl(song_num)
                pt = text2
                pp = (200, 55)
            if event.key == pygame.K_LEFT:
                back_but.draw(WIN, text4, (100, 55), True)
                ch_num(-1)
                song_pl(song_num)
                pt = text2 
                isPlay = True
                pp = (200, 55)
            if event.key == pygame.K_SPACE:
                play_but.draw(WIN, pt, pp, True)
                play()
        if event.type == ended:
            ch_num(1)
            song_pl(song_num)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and 190<m_pos[0]<310 and 15<m_pos[1]<135:
                play_but.draw(WIN, pt, pp, True)
                play()
            if event.button == 1 and 95<m_pos[0]<185 and 30<m_pos[1]<120:
                back_but.draw(WIN, text4, (100, 55), True)
                ch_num(-1)
                song_pl(song_num)
                pt = text2 
                isPlay = True
                pp = (200, 55)
            if event.button == 1 and 315<m_pos[0]<405 and 30<m_pos[1]<120:
                next_but.draw(WIN, text3, (320, 55), True)
                ch_num(1)
                song_pl(song_num)
                pt = text2
                isPlay = True
                pp = (200, 55)
            if event.button == 1 and 145<m_pos[1]<165 and 50<m_pos[0]<450:
                volume_c = True
        if event.type == pygame.MOUSEBUTTONUP:
            volume_c = False

    if volume_c and 50<m_pos[0]<450:
        volume = (m_pos[0]-50)/400

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        if volume + volume_s > 1:
            volume = 1
        else:
            volume += volume_s
    if keys[pygame.K_DOWN]:
        if volume - volume_s < 0:
            volume = 0
        else:
            volume -= volume_s
    pygame.display.update()
        

pygame.quit()

