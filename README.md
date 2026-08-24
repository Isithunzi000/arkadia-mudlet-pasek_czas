# Pasek kalendarza Arkadii — Mudlet

Pakiet do Mudleta: pasek u góry okna z żywym kalendarzem i zegarem gry dla Arkadii MUD (domeny Ishtar i Imperium).

---

## Jak zainstalować

1. Pobierz `.mpackage` albo `.xml` z [najnowszego wydania](https://github.com/Isithunzi000/arkadia-mudlet-pasek_czas/releases/latest) (oba działają tak samo, wybierz który wolisz)
2. W Mudlecie: **Ustawienia → Menedżer pakietów → Zainstaluj** i wskaż pobrany plik
3. Gotowe — pasek pojawi się u góry okna; po zalogowaniu wpisz `czas` (albo kliknij pasek), żeby go zsynchronizować
4. Od wersji 1.6.3 przy każdym załadowaniu pakietu zobaczysz w oknie komunikat `[pasek_kalendarz] Pasek kalendarza v<wersja> zaladowany...` — to potwierdzenie, że pakiet działa (tak samo jak przy kalendarzach Ishtar i Imperium)

Plik [`pasek_kalendarz_arkadia.xml`](pasek_kalendarz_arkadia.xml) w korzeniu repo to źródło pakietu — możesz podejrzeć cały kod bez pobierania.

---

## Co pokazuje pasek

- godzinę gry — zegar chodzi na żywo między synchronizacjami
- dzień / noc z ikoną (☀ / ☾)
- datę: pora roku (Ishtar) albo miesiąc (Imperium) plus numer dnia roku
- wskaźnik **CIEMNO** — osobna „pigułka” dokładnie pod środkiem paska, zapala się tylko gdy postać nic nie widzi w ciemnym pomieszczeniu

## Jak to działa

- synchronizacja wyłącznie na świadome żądanie gracza: wpisz `czas`, kliknij pasek albo użyj komendy `/pasek` — plugin parsuje odpowiedź; **plugin nigdy nie wysyła komend samodzielnie** (wymóg pkt 2 Zasad Arkadii)
- zegar dokręca się przy każdym wschodzie i zachodzie słońca (z GMCP) — bez dodatkowych zapytań do serwera
- domena (Ishtar / Imperium) rozpoznawana automatycznie z GMCP
- kotwice czasu i ustawienia wyglądu zapisywane na dysku — po restarcie klienta wszystko chodzi dalej
- gdy odpowiedź `czas` jest niejednoznaczna (np. noc Geheimnisnacht), zegar nie zgaduje — zostaje ekstrapolacja z ostatniej pewnej kotwicy

## Komendy

**Od wersji 1.6.0 wszystkie komendy mają prefiks `/pasek`** (jak w pozostałych kalendarzach: `/ishtar`, `/imperium`). Stare formy bez ukośnika przestały działać.

**Czas:**

- `/pasek` — wymusza synchronizację (wysyła `czas`)
- `/pasek ustaw imperium 8 273` — ręczne ustawienie: domena, godzina 0–23, opcjonalnie dzień roku
- `/pasek reset` — czyści zapisane kotwice czasu

**Wygląd i pozycja** (wszystko zapisuje się na dysku i działa po restarcie):

- `/pasek pozycja X Y` — przesuwa pasek (pigułka CIEMNO sama podąża za paskiem)
- `/pasek wartosci` — pokazuje aktualne wartości: pozycję i kolory (w nawiasach fabryczne)
- `/pasek tlo R G B [A]` — kolor tła paska (opcjonalnie przezroczystość 0–255)
- `/pasek tekst R G B` — kolor tekstu paska
- `/pasek ciemno R G B [A]` — kolor pigułki CIEMNO
- `/pasek domyslne` — powrót do ustawień fabrycznych (pozycja + kolory)
- `/pasek pomoc` — ściągawka komend w oknie gry

**Aktualizacje:**

- `/pasek aktualizuj` — sprawdza i instaluje aktualizację z GitHub Releases

Kolory podaje się jako trzy liczby 0–255 (RGB), np. `/pasek tlo 40 0 60 180`. Kliknięcie paska też wysyła `czas`.

---

## Aktualizacje

Pakiet sam sprawdza aktualizacje: przy starcie klienta (nie częściej niż co 8 godzin) pyta o najnowsze wydanie na GitHubie i — jeśli jest nowsza wersja — wyświetla powiadomienie. Sam nic nie instaluje: aktualizację uruchamiasz świadomie komendą `/pasek aktualizuj`, która pobiera paczkę, podmienia ją i prosi o restart Mudleta.

> **Zmiana w 1.6.0 (łamiąca):** komendy przeszły na prefiks `/pasek` (stare formy bez ukośnika nie działają), a paczka ma nową nazwę `pasek_kalendarz_arkadia`. Przy pierwszej aktualizacji ze starszej wersji odinstaluj ręcznie starą paczkę `pasek kalendarz arkadia` w Menedżerze pakietów, żeby nie mieć dwóch kopii naraz.

Od wersji **1.6.2** oba assety wydania mają stałe nazwy (`pasek_kalendarz_arkadia.mpackage`, `pasek_kalendarz_arkadia.xml`), a aktualizator przed instalacją sprząta historyczne nazwy pakietów — jedna paczka zostaje w profilu zawsze pod nazwą `pasek_kalendarz_arkadia`.

### Mudlet web — jednorazowe czyszczenie

Starsze wydania na mudlet-web (Mudlet w przeglądarce) brały nazwę paczki od nazwy pliku. Po zainstalowaniu wersji 1.6.2 lub nowszej otwórz **Package Manager** i odinstaluj ręcznie wszystkie pozycje z poniższej listy, jeśli je widzisz (zostaw tylko `pasek_kalendarz_arkadia`):

- `pasek_kalendarz_update`
- `pasek_kalendarz_1_2_0`, `pasek_kalendarz_1_3_0`, `pasek_kalendarz_1_4_0`, `pasek_kalendarz_1_4_1`, `pasek_kalendarz_1_5_0`, `pasek_kalendarz_1_5_1`, `pasek_kalendarz_1_6_1`

To czyszczenie robisz tylko raz — kolejne aktualizacje sprzątają te nazwy samoczynnie.

> Jeśli po odinstalowaniu paczki w konsoli narasta błąd `timer "tick": ... attempt to index global 'pasek_kalendarz'`, to osierocony timer z poprzedniej wersji: wpisz w linii poleceń `lua killTimer("tick")` (powtórz, aż błędy ustaną). Od 1.6.2 timer sam sprząta się w tej sytuacji.

---

## Uwagi

- przelicznik czasu: 2 sekundy RL = 1 minuta IG (doba gry = 48 minut RL)
- kalendarz Ishtar: 360 dni (8 pór roku po 45 dni); Kalendarz Imperialny: 400 dni (17 pozycji ze świętami interkalarnymi)
- silnik kalendarza przeniesiony 1:1 z pluginów Dargoth ([ishtar_cal / imperium_cal](https://github.com/Isithunzi000/arkadia-dargoth-plugins))
- mechaniki „życia” zegara (kotwice, rekalibracja na wschodzie/zachodzie, model precyzji) — wg rozwiązania z repo [Delwing/arkadia-web-client-extension](https://github.com/Delwing/arkadia-web-client-extension) (`src/client/scripts/clock.ts`)
- pozycję i kolory paska ustawisz komendami (`/pasek pozycja`, `/pasek tlo` itd. — patrz wyżej); zapisują się na dysku razem z kotwicami czasu

