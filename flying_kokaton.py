import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img,True,False) #練習8
    kk_img = pg.image.load("fig/3.png") #練習2－1
    kk_img = pg.transform.flip(kk_img,True,False) #練習2-2
    kk_rct = kk_img.get_rect() #練習10-1　Rectの抽出
    kk_rct.center = 300,200 #練習10-2 中心座標の設定
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        key_lst = pg.key.get_pressed() #練習10-3

        y=0
        z=0
        if key_lst[pg.K_UP]:
           y=0
           z=-1 #練習10-4
        if key_lst[pg.K_DOWN]:
            y=0
            z=1
        if key_lst[pg.K_LEFT]:
            y=-1
            z-0
        if key_lst[pg.K_RIGHT]:
            y=2
            z-0

        kk_rct.move_ip(-1+y,0+z)
        x = tmr%3200
        screen.blit(bg_img, [-x, 0]) #練習6
        screen.blit(bg_img2,[-x+1600,0]) #練習7
        screen.blit(bg_img,[-x+3200,0]) #練習9
        screen.blit(kk_img, kk_rct) #練習4/練習10-5
        pg.display.update()
        tmr += 1        
        clock.tick(200) #練習5


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()