# Pasek kalendarza Arkadii — Mudlet

Pakiet do Mudleta: pasek u góry okna z żywym kalendarzem i zegarem gry dla Arkadii MUD (domeny Ishtar i Imperium).

---

## Jak zainstalować

1. Pobierz `.mpackage` albo `.xml` z [najnowszego wydania](https://github.com/Isithunzi000/arkadia-mudlet-pasek_czas/releases/latest) (oba działają tak samo, wybierz który wolisz)
2. W Mudlecie: **Ustawienia → Menedżer pakietów → Zainstaluj** i wskaż pobrany plik
3. Gotowe — pasek pojawi się u góry okna; po zalogowaniu wpisz `czas` (albo kliknij pasek), żeby go zsynchronizować

Plik [`pasek_kalendarz_arkadia.xml`](pasek_kalendarz_arkadia.xml) w korzeniu repo to źródło pakietu — możesz podejrzeć cały kod bez pobierania.

---

## Co pokazuje pasek

- godzinę gry — zegar chodzi na żywo między synchronizacjami
- dzień / noc z ikoną (☀ / ☾)
- datę: pora roku (Ishtar) albo miesiąc (Imperium) plus numer dnia roku
- wskaźnik **CIEMNO** — osobna „pigułka” dokładnie pod środkiem paska, zapala się tylko gdy postać nic nie widzi w ciemnym pomieszczeniu

## Jak to działa

- synchronizacja wyłącznie na świadome żądanie gracza: wpisz `czas`, kliknij pasek albo użyj komendy `pasek` — plugin parsuje odpowiedź; **plugin nigdy nie wysyła komend samodzielnie** (wymóg pkt 2 Zasad Arkadii)
- zegar dokręca się przy każdym wschodzie i zachodzie słońca (z GMCP) — bez dodatkowych zapytań do serwera
- domena (Ishtar / Imperium) rozpoznawana automatycznie z GMCP
- kotwice czasu i ustawienia wyglądu zapisywane na dysku — po restarcie klienta wszystko chodzi dalej
- gdy odpowiedź `czas` jest niejednoznaczna (np. noc Geheimnisnacht), zegar nie zgaduje — zostaje ekstrapolacja z ostatniej pewnej kotwicy

## Komendy

**Czas:**

- `pasek` — wymusza synchronizację (wysyła `czas`)
- `pasek ustaw imperium 8 273` — ręczne ustawienie: domena, godzina 0–23, opcjonalnie dzień roku
- `pasek reset` — czyści zapisane kotwice czasu

**Wygląd i pozycja** (od v1.4 — wszystko zapisuje się na dysku i działa po restarcie):

- `pasek pozycja X Y` — przesuwa pasek (pigułka CIEMNO sama podąża za paskiem)
- `pasek tlo R G B [A]` — kolor tła paska (opcjonalnie przezroczystość 0–255)
- `pasek tekst R G B` — kolor tekstu paska
- `pasek ciemno R G B [A]` — kolor pigułki CIEMNO
- `pasek domyslne` — powrót do ustawień fabrycznych (pozycja + kolory)
- `pasek pomoc` — ściągawka komend w oknie gry

Kolory podaje się jako trzy liczby 0–255 (RGB), np. `pasek tlo 40 0 60 180`. Kliknięcie paska też wysyła `czas`.

---

## Uwagi

- przelicznik czasu: 2 sekundy RL = 1 minuta IG (doba gry = 48 minut RL)
- kalendarz Ishtar: 360 dni (8 pór roku po 45 dni); Kalendarz Imperialny: 400 dni (17 pozycji ze świętami interkalarnymi)
- od v1.5.0 plugin nie wysyła już sam komendy `czas` po zalogowaniu — synchronizacja wyłącznie świadoma (komenda `czas`, klik w pasek, alias `pasek`), zgodnie z pkt 2 Zasad Arkadii
- od v1.4.1 poprawka parsera godziny: „poludnie”/„poludniem” po słowie godziny nie dodają już 12 (np. „poludnie poludniem” = 12:00, wcześniej błędnie 0:00)
- silnik kalendarza przeniesiony 1:1 z pluginów Dargoth ([ishtar_cal / imperium_cal](https://github.com/Isithunzi000/arkadia-dargoth-plugins))
- mechaniki „życia” zegara (kotwice, rekalibracja na wschodzie/zachodzie, model precyzji) — wg rozwiązania z repo [Delwing/arkadia-web-client-extension](https://github.com/Delwing/arkadia-web-client-extension) (`src/client/scripts/clock.ts`)
- pozycję i kolory paska ustawisz komendami (`pasek pozycja`, `pasek tlo` itd. — patrz wyżej); zapisują się na dysku razem z kotwicami czasu

