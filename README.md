# 🎮 Gra „Znajdź różnice”


Projekt to prosta gra logiczna typu „znajdź różnice ”, w której gracz porównuje dwa niemal identyczne obrazy i wskazuje miejsca, w których obrazki różnią się od siebie.
Powstała jako ćwiczenie w nauce Python, Tkinter, threading oraz tworzeniu pliku wykonywalnego .exe. Gra ma na celu rozwijanie spostrzegawczości💡


Technologie: Python, 


Modules: os, sys, threading, tkinter, pygame


⚙️ 1. Jak uruchomić

🔹 Wersja 1 — plik .exe
 ** Pobierz folder projektu.

** Uruchom plik find_differences.exe.

** Gra otworzy się w oknie — klikaj różnice na obrazach, aby zdobywać punkty.




🔹 Wersja 2 — kod w Python (IDE)
** Otwórz projekt w ulubionym IDE (np. VS Code, PyCharm).

** Upewnij się, że masz zainstalowany Python ≥ 3.10 oraz bibliotekę Tkinter.

** Uruchom:

```bash
python main.py
```
Gra wystartuje w oknie Tkinter.


🕹️ 2. Zasady gry
Porównaj dwa obrazy obok siebie.

Kliknij miejsca, w których zauważysz różnice.

Po znalezieniu wszystkich różnic przechodzisz do kolejnego poziomu.* (będzie w wersji rozszwerzonej)




🧱 3. Struktura projektu

Game/

│

├── build/               # Pliki pomocnicze tworzone przy kompilacji do .exe

│

├── dist/                # Folder z gotowym plikiem wykonywalnym gry (.exe)

│   └── diff.exe         # Plik .exe gry

│

├── images/              # Obrazy używane w grze

│

├── dif_game_grid.py     # Skrypt z siatką (gridem) do kalibracji współrzędnych różnic

├── diff.py              # Główny skrypt porównujący obrazy i obsługujący logikę gry

└── diff.spec            # Specyfikacja dla PyInstaller (tworzenie pliku .exe)




🔍 4. Lessons learned
Podczas tworzenia projektu nauczyłam się kilku kluczowych rzeczy:

* Dodanie skryptu z gridem — stworzyłam siatkę współrzędnych, która pomogła mi precyzyjnie określić parametry różnic na obrazach. Dzięki temu kliknięcia gracza są dokładnie weryfikowane.

* Poznanie Tkintera — zrozumiałam, jak działa pętla zdarzeń, obsługa przycisków i Canvas.

* Threading — wykorzystałam wątek do mierzenia czasu gry i zapisu wyników bez blokowania interfejsu.

* Debugowanie i eksport do .exe — po kilku próbach z pyinstaller udało się poprawnie zapisać grę jako plik wykonywalny, rozwiązując błędy z zasobami i ścieżkami.



🧩 5. Dalszy rozwój
W wolnym czasie planuję:

Dodać kolejne levele z nowymi parami zdjęć.

Wprowadzić system punktacji i ranking graczy.

Rozszerzyć projekt o tryb multiplayer lub czasowe wyzwania.

Ulepszyć interfejs — np. animacje przy znalezieniu różnicy 🎉.


6. 💡 Co pokazuje ten projekt
Ten projekt jest świetnym przykładem połączenia:

* Tkinter – do zarządzania oknami aplikacji

* Pygame Zero – do renderowania i interakcji

* Przetwarzania obrazów – do zaznaczania różnic

* Debugowania geometrii GUI

* Pakowania aplikacji Python do pliku .exe

* Tworzenia narzędzi pomocniczych (np. siatki nakładanej na obraz) wspierających proces tworzenia



Code snippet: 

Code snippet: 

<hr style="border:3px solid #AEC6CF;">


### Contact:
[![Kamila Dudzińska](https://img.shields.io/badge/Kamila%20Dudzińska-ff69b4?style=for-the-badge)](mailto:kamila.dudzinska@onet.pl)
[![Email](https://img.shields.io/badge/Email-555555?style=for-the-badge)](mailto:kamila.dudzinska@onet.pl)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge)](https://www.linkedin.com/flagship-web/in/kamila-dudzi%C5%84ska-856bb31b8/)

<br></br>













