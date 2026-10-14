"""
Created on Sunday 18.07.2026
Extended on Tuesday 14.10.2026

@author: Kamila Dudzińska

This file initializes the game window, loads image, and manages user interaction.
It serves as the entry point for the project and can be run directly by .exe. file.

Libraries:
threading - lib. to achieve concurency by running miltiple threads simultaneously.
pygema - open source lib. designed for multimedia app and teo-dimensial games.
Tkinter - buil-in GUI toolkit. To create desktop app with windows, menu, buttons.

"""

# functions & preparations
# built-in (standard)
import os
import sys
import threading
import queue
import tkinter as tk
import tkinter.font as tkfont

# third-party modules
import pygame
from pygame import Rect

# background:
# PyInstaller unpacks resources to when running from .exe
katalog = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))

# size
WIDTH = 940
HEIGHT = 630

# click tolerance around each difference, in pixels
MARGINES = 10
def trafiony(region, pos):
    return region.inflate(2 * MARGINES, 2 * MARGINES).collidepoint(pos)

# area of differences level 1 
# I used Rect to define the area
region11 = Rect((60, 250), (50,50))
region12 = Rect((500, 250), (50,50))

region21 = Rect((80,400), (50,50))
region22 = Rect((520,400), (50,50))

region31 = Rect((250,460), (60,50))
region32 = Rect((680,460), (60,50))

# area of differences - level 2 (china.jpg): 
# right picture is 442 px to the right of the left one
offset_2 = 442
size_rect_2 = 40
 
def para(x, y):
    # square area centered on (x, y) on the left picture + the same area on the right picture
    left = Rect((x - size_rect_2 // 2, y - size_rect_2 // 2), (size_rect_2, size_rect_2))
    return left, left.move(offset_2, 0)
 
# levels: image + list of pairs (left area, right area)
POZIOMY = [
    {"obrazek": "dif.png", "icon": "sweet.png", "icon_name": "Sweet",
     "regiony": [(region11, region12), 
                 (region21, region22), 
                 (region31, region32)]},
    {"obrazek": "china.jpg", "icon": "happiness.png", "icon_name": "Happiness",
     "regiony": [para(197, 220),    # ornament on the forehead
                 para(152, 252),    # mole on the cheek
                 para(380, 144),    # golden hairpin
                 para(422, 237),    # end of the earring
                 para(377, 401),    # "100" sign
                 para(419, 450),    # sign on the sleeve
                 para(279, 506),    # sign on the skirt
                 para(73, 538)]},   # embroidered circle in the corner
]
 
# the path to file was hidden due to safety reasons.
backgrounds = [pygame.image.load(os.path.join(katalog, 'images', p["obrazek"])) for p in POZIOMY]
 
# current level
poziom = 0
regiony = POZIOMY[poziom]["regiony"]
background = backgrounds[poziom]
 
# list of points
lista = [False] * len(regiony)

# close game
zdarzenia = queue.Queue() 
new_window = threading.Event()

def show_ending(gamer_result, num_differences, is_next, icon, icon_name):

    def window_tk():
        window = tk.Tk()
        window.title("Game over!")

        wid = 450
        hh = 250
        screen_el = f"{wid}x{hh}+{int(window.winfo_screenwidth()/2 - wid/2)}+{int(window.winfo_screenheight()/2 - hh/2)}"
        window.geometry(screen_el)
        window.configure(bg="#2C3E50")
        font_header = tkfont.Font(root=window, family="Helvetica", size=22, weight="bold")
        fontt = tkfont.Font(root=window, family="Helvetica", size=14)
        font_button = tkfont.Font(root=window, family="Helvetica", size=14, weight="bold")

        label_header = tk.Label(window,
                                text="WOW! You win!",
                                fg="#1ABC9C",           #dim light green
                                bg="#2C3E50",           #dim dark grey
                                font=font_header)
        label_header.pack(pady=(20, 10))

        text_result = f"Found {gamer_result}/{num_differences} elements!"
        label_result = tk.Label(window,
                               text=text_result,
                               fg="#ECF0F1",            #light grayish
                               bg="#2C3E50",            #dim dark grey
                               font=fontt)
        label_result.pack(pady=10)

        # reward icon won on this level (627 px PNG, subsample(4) makes it ~157 px)
        # master=window - the image must belong to this window's Tk (this runs in a separate thread)
        icon_img = tk.PhotoImage(master=window, file=os.path.join(katalog, 'images', icon)).subsample(4)
        label_icon = tk.Label(window, 
                              image=icon_img, 
                              bg="#2C3E50")
        label_icon.image = icon_img                     # keep a reference, otherwise the image disappears
        label_icon.pack()

        label_reward = tk.Label(window,
                                text=f"Your reward: {icon_name}",
                                fg="#1ABC9C",           #dim light green
                                bg="#2C3E50",           #dim dark grey
                                font=fontt)
        label_reward.pack(pady=(5, 0))

        frame = tk.Frame(window, bg="#2C3E50")          #dim dark grey
        frame.pack(pady=20)

        
        def play_again():
            zdarzenia.put('next' if is_next else 'restart')
            window.destroy()

        
        def exit_game():
            zdarzenia.put('exit')
            window.destroy()
            
        # closing with X works like Exit
        window.protocol("WM_DELETE_WINDOW", exit_game)

        
        btn_restart = tk.Button(
            frame,
            text="Next level" if is_next else "Play again",
            command=play_again,
            bg="#2ECC71",                   #lime green
            fg="#ECF0F1",                   #light grayish
            font=font_button,
            activebackground="#27AE60",     #dark lime green
            activeforeground="white",
            bd=0, padx=15, pady=8
        )
        
        btn_restart.pack(side=tk.LEFT, padx=10)

        btn_wyjscie = tk.Button(
            frame,
            text="Exit",
            command=exit_game,
            bg="#E74C3C",                   #bright red
            fg="#ECF0F1",
            font=font_button,
            activebackground="#C0392B",     #strong red
            activeforeground="#ECF0F1",     #light grayish
            bd=0, padx=15, pady=8
        )
        btn_wyjscie.pack(side=tk.LEFT, padx=10)

        # window height adjusted to the content (icon, Windows display scaling)
        window.update_idletasks()
        hh = window.winfo_reqheight()
        screen_el = f"{wid}x{hh}+{int(window.winfo_screenwidth()/2 - wid/2)}+{int(window.winfo_screenheight()/2 - hh/2)}"
        window.geometry(screen_el)

        window.mainloop()

    new_window.set()
    thread = threading.Thread(target=window_tk)
    thread.daemon = True
    thread.start()
    
def intro():
    # okno intro uruchamiane przed Pygame, bez wątków
    window = tk.Tk()
    window.title("Find the differences – intro")

    wid = 520
    hh = 360
    screen_el = f"{wid}x{hh}+{int(window.winfo_screenwidth() / 2 - wid / 2)}+{int(window.winfo_screenheight() / 2 - hh / 2)}"
    window.geometry(screen_el)
    window.configure(bg="#2C3E50")

    font_header = tkfont.Font(root=window, family="Helvetica", size=18, weight="bold")
    fontt = tkfont.Font(root=window, family="Helvetica", size=12)
    font_button = tkfont.Font(root=window, family="Helvetica", size=14, weight="bold")

    # Header
    label_header = tk.Label(
        window,
        text="Find the differences!",
        fg="#1ABC9C",
        bg="#2C3E50",
        font=font_header
    )
    label_header.pack(pady=(20, 10))

    # Description (tekst wewnątrz okna, nie w tytule)
    description = (
        "Your task:\n"
        "- Look carefully at both images\n"
        "- Find all possible differences in the picture\n"
        "- Click on the spots where the images differ - right picture\n\n"
        "Image description:\n"
        "Two Nigerian women in vivid yellow and green traditional dresses, "
        "with large golden earrings and long beaded necklaces.\n"
        "Their heads are wrapped in 'Gele' - a festive, sculpted headwrap "
        "worn for weddings and celebrations."
    )

    label_desc = tk.Label(
        window,
        text=description,
        fg="#ECF0F1",                   #Light grayish
        bg="#2C3E50",                   #dark desaturated blue.
        font=fontt,
        justify="left",
        wraplength=480  # zawija tekst, żeby nie wychodził poza okno
    )
    label_desc.pack(pady=10)

    # Play button
    def start_game():
        window.quit()


    # wide button with a rounded (squoval) shape - tk.Button can't round corners,
    # so the shape is drawn on a Canvas
    btn_w = 168                                # width in pixels (280 minus 20% on each side)
    btn_h = 60                                 # height in pixels
    r = 26                                     # how round the corners are
    btn_start = tk.Canvas(window, width=btn_w, height=btn_h,
                          bg="#2C3E50", highlightthickness=0, cursor="hand2")
    points = [r, 0, r, 0, btn_w - r, 0, btn_w - r, 0, btn_w, 0,
              btn_w, r, btn_w, r, btn_w, btn_h - r, btn_w, btn_h - r, btn_w, btn_h,
              btn_w - r, btn_h, btn_w - r, btn_h, r, btn_h, r, btn_h, 0, btn_h,
              0, btn_h - r, 0, btn_h - r, 0, r, 0, r, 0, 0]
    shape = btn_start.create_polygon(points, smooth=True, fill="#2ECC71")   #lime green
    btn_start.create_text(btn_w // 2, btn_h // 2, text="Play",
                          fill="#ECF0F1", font=font_button)               #Light grayish

    # hover and click
    btn_start.bind("<Enter>", lambda event: btn_start.itemconfig(shape, fill="#27AE60"))  #dark lime green
    btn_start.bind("<Leave>", lambda event: btn_start.itemconfig(shape, fill="#2ECC71"))
    btn_start.bind("<Button-1>", lambda event: start_game())
    btn_start.pack(pady=(10, 20))


    # window height adjusted to the content (Window scaling)
    window.update_idletasks()
    hh = window.winfo_reqheight()
    screen_el = f"{wid}x{hh}+{int(window.winfo_screenwidth() / 2 - wid / 2)}+{int(window.winfo_screenheight() / 2 - hh / 2)}"
    window.geometry(screen_el)

    window.protocol("WM_DELETE_WINDOW", start_game)
    window.mainloop()
    window.destroy()
 

#NTRO WINDOW 
intro()    


# MAIN GAME LOOP — PURE PYGAME
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Find the differences")
clock = pygame.time.Clock()
pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)
font_hud = pygame.font.SysFont("Helvetica", 
                               24, 
                               bold=True)
time_start = pygame.time.get_ticks()
time = 0
miss = 0

running = True

while running:
    while not zdarzenia.empty():
        action = zdarzenia.get()
        new_window.clear()
        if action == "next":
            poziom += 1
        elif action == "restart":
            poziom = 0
        if action in ("next", "restart"):
            regiony = POZIOMY[poziom]["regiony"]
            background = backgrounds[poziom]
            lista = [False] * len(regiony)
            time_start = pygame.time.get_ticks()
            miss = 0
        if action == "exit":
            running = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # mouse click
        if event.type == pygame.MOUSEBUTTONDOWN and not new_window.is_set():
            pos = event.pos     # exact point where the player clicked
            strike = False
            for i, (left, right) in enumerate(regiony):
                if trafiony(left, pos) or trafiony(right, pos):
                    print(f"{i + 1} Element found!")
                    lista[i] = True
                    strike = True

            if not strike:
                miss += 1
                
            if all(lista):
                print("You win!")
                show_ending(sum(lista), len(lista), poziom + 1 < len(POZIOMY),
                            POZIOMY[poziom]["icon"], POZIOMY[poziom]["icon_name"])
                

    # draw background
    screen.blit(background, (0,0))

    # draw found regions
    for i, (left, right) in enumerate(regiony):
        if lista[i]:
            pygame.draw.rect(screen, (255,0,0), left, 3)
            pygame.draw.rect(screen, (255,0,0), right, 3)

    if not all(lista):
        time = (pygame.time.get_ticks() - time_start) // 1000
    text = f"Level {poziom + 1}   Found: {sum(lista)}/{len(lista)}   Time: {time}s   Misses: {miss}"
    sign = font_hud.render(text, True, (255, 255, 255))
    tlo = sign.get_rect(topleft=(10, 10)).inflate(12, 6)
    pygame.draw.rect(screen, (0, 0, 0), tlo)
    screen.blit(sign, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

