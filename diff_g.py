"""
Created on Sun Jul 18 14:00:28 2026

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
import tkinter as tk
import tkinter.font as tkfont

# third-party modules
import pygame
from pygame import Rect

# background:
katalog = os.path.dirname(os.path.abspath(__file__))
#the path to file was hidden due to safety reasons. 
obrazek_path = os.path.join(r'\images', 'dif.png')
background = pygame.image.load(obrazek_path)

# size
WIDTH = 940
HEIGHT = 630

# area of differences
region11 = Rect((60, 250), (50,50))
region12 = Rect((500, 250), (50,50))

region21 = Rect((80,400), (50,50))
region22 = Rect((520,400), (50,50))

region31 = Rect((250,460), (60,50))
region32 = Rect((680,460), (60,50))

# cursor
kursor = Rect((0,0), (15,15))

# list of points
lista = [False, False, False]

# close game
close_game = False

def pokaz_zakonczenie(wynik_gracza, restart_game):

    def window_tk():
        window = tk.Tk()
        window.title("Game over!")

        wid = 450
        hh = 250
        screen_el = f"{wid}x{hh}+{int(window.winfo_screenwidth()/2 - wid/2)}+{int(window.winfo_screenheight()/2 - wid/2)}"
        window.geometry(screen_el)
        window.configure(bg="#2C3E50")
        font_header = tkfont.Font(family="Helvetica", size=22, weight="bold")
        fontt = tkfont.Font(family="Helvetica", size=14)
        font_button = tkfont.Font(family="Helvetica", size=14, weight="bold")

        label_header = tk.Label(window,
                                text="WOW! You win!",
                                fg="#1ABC9C",           #dim light green
                                bg="#2C3E50",           #dim dark grey
                                font=font_header)
        label_header.pack(pady=(20, 10))

        text_result = f"Found 3/3 elements!"
        label_result = tk.Label(window,
                               text=text_result,
                               fg="#ECF0F1",            #light grayish
                               bg="#2C3E50",            #dim dark grey
                               font=fontt)
        label_result.pack(pady=10)

        frame = tk.Frame(window, bg="#2C3E50")          #dim dark grey
        frame.pack(pady=20)

        def play_again():
            window.destroy()
            restart_game()

        def restart_game():
            global lista, kursor
            lista = [False, False, False]
            kursor = Rect((0,0), (15,15))

        def exit_game():
            global close_game
            window.destroy()
            close_game = True

        btn_restart = tk.Button(
            frame,
            text="Play again",
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

        window.mainloop()

    #
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

    font_header = tkfont.Font(family="Helvetica", size=18, weight="bold")
    fontt = tkfont.Font(family="Helvetica", size=12)
    font_button = tkfont.Font(family="Helvetica", size=12, weight="bold")

    # Header
    label_header = tk.Label(
        window,
        text="Find 3 differences!",
        fg="#1ABC9C",
        bg="#2C3E50",
        font=font_header
    )
    label_header.pack(pady=(20, 10))

    # Description (tekst wewnątrz okna, nie w tytule)
    opis = (
        "Your task:\n"
        "- Look carefully at both images\n"
        "- Find 3 differences\n"
        "- Click on the spots where the images differ - right picture\n\n"
        "Image description:\n"
        "Traditional women's clothes from Nigeria \n "
        "and a characteristic headwrap called 'Gele'."
    )

    label_desc = tk.Label(
        window,
        text=opis,
        fg="#ECF0F1",                   #Light grayish
        bg="#2C3E50",                   #dark desaturated blue.
        font=fontt,
        justify="left",
        wraplength=480  # zawija tekst, żeby nie wychodził poza okno
    )
    label_desc.pack(pady=10)

    # Play button
    def start_game():
        window.destroy()

    btn_start = tk.Button(
        window,
        text="Play",
        command=start_game,
        bg="#2ECC71",                          #lime green  
        fg="#ECF0F1",                          #Light grayish
        font=font_button,
        activebackground="#27AE60",            #dark lime green
        activeforeground="#ECF0F1",            #Light grayish
        bd=1
    )

    # wymuszenie wysokości i marginesów
    btn_start.pack(pady=(10, 10))
    btn_start.update_idletasks()  # odświeża geometrię
    btn_start.configure(height=8)  # zwiększa wysokość w jednostkach tekstowych


    window.mainloop()
 

#NTRO WINDOW 
intro()    


# MAIN GAME LOOP — PURE PYGAME
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Find the differences")
clock = pygame.time.Clock()

running = True

while running:
    if close_game:
        pygame.quit()
        sys.exit()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            if kursor.colliderect(region11) or kursor.colliderect(region12):
                print("1 Element found!")
                lista[0] = True
            if kursor.colliderect(region21) or kursor.colliderect(region22):
                print("2 Element found!")
                lista[1] = True
            if kursor.colliderect(region31) or kursor.colliderect(region32):
                print("3 Element found!")
                lista[2] = True

            if lista == [True, True, True]:
                print("You win!")
                pokaz_zakonczenie(3, lambda: None)

    # update cursor position
    mouse_pos = pygame.mouse.get_pos()
    kursor.topleft = mouse_pos

    # draw background
    screen.blit(background, (0,0))

    # draw found regions
    if lista[0]:
        pygame.draw.rect(screen, (255,0,0), region11, 3)
        pygame.draw.rect(screen, (255,0,0), region12, 3)
    if lista[1]:
        pygame.draw.rect(screen, (255,0,0), region21, 3)
        pygame.draw.rect(screen, (255,0,0), region22, 3)
    if lista[2]:
        pygame.draw.rect(screen, (255,0,0), region31, 3)
        pygame.draw.rect(screen, (255,0,0), region32, 3)

    # draw cursor
    pygame.draw.rect(screen, (255,255,255), kursor)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
