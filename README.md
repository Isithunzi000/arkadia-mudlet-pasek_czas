# Pasek kalendarza Arkadii — Mudlet

Pakiet do Mudleta: pasek u góry okna z żywym kalendarzem i zegarem gry dla Arkadii MUD (domeny Ishtar i Imperium).

---

## Jak zainstalować

1. Pobierz `.mpackage` albo `.xml` z [najnowszego wydania](https://github.com/Isithunzi000/arkadia-mudlet-pasek_czas/releases/latest) (oba działają tak samo, wybierz który wolisz)
2. W Mudlecie: **Ustawienia → Menedżer pakietów → Zainstaluj** i wskaż pobrany plik
3. Gotowe — pasek pojawi się u góry okna i sam się zsynchronizuje po zalogowaniu

Plik [`pasek_kalendarz_arkadia.xml`](pasek_kalendarz_arkadia.xml) w korzeniu repo to źródło pakietu — możesz podejrzeć cały kod bez pobierania.

---

## Co pokazuje pasek

- godzinę gry — zegar chodzi na żywo między synchronizacjami
- dzień / noc z ikoną (☀ / ☾)
- datę: pora roku (Ishtar) albo miesiąc (Imperium) plus numer dnia roku
- wskaźnik **CIEMNO** — osobna „pigułka” dokładnie pod środkiem paska, zapala się tylko gdy postać nic nie widzi w ciemnym pomieszczeniu

## Jak to działa

- pierwsza synchronizacja: pakiet sam wysyła `czas` po zalogowaniu i parsuje odpowiedź
- zegar dokręca się przy każdym wschodzie i zachodzie słońca (z GMCP) — bez dodatkowych zapytań do serwera
- domena (Ishtar / Imperium) rozpoznawana automatycznie z GMCP
- kotwice czasu zapisywane na dysku — po restarcie klienta zegar chodzi dalej
- gdy odpowiedź `czas` jest niejednoznaczna (np. noc Geheimnisnacht), zegar nie zgaduje — zostaje ekstrapolacja z ostatniej pewnej kotwicy

## Komendy

- `pasek` — wymusza synchronizację (wysyła `czas`)
- `pasek ustaw imperium 8 273` — ręczne ustawienie: domena, godzina 0–23, opcjonalnie dzień roku
- `pasek reset` — czyści zapisane kotwice i synchronizuje od nowa

Kliknięcie paska też wysyła `czas`.

---

## Uwagi

- przelicznik czasu: 2 sekundy RL = 1 minuta IG (doba gry = 48 minut RL)
- kalendarz Ishtar: 360 dni (8 pór roku po 45 dni); Kalendarz Imperialny: 400 dni (17 pozycji ze świętami interkalarnymi)
- silnik kalendarza przeniesiony 1:1 z pluginów Dargoth ([ishtar_cal / imperium_cal](https://github.com/Isithunzi000/arkadia-dargoth-plugins))
- mechaniki „życia” zegara (kotwice, rekalibracja na wschodzie/zachodzie, model precyzji) — wg rozwiązania z repo [Delwing/arkadia-web-client-extension](https://github.com/Delwing/arkadia-web-client-extension) (`src/client/scripts/clock.ts`)
- pozycję i rozmiar paska zmienisz w skrypcie `silnik` → tabela `pk.cfg` (x, y, width, height); pigułka CIEMNO sama podąża za paskiem

