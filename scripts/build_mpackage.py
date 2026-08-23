#!/usr/bin/env python3
"""Deterministyczny build pakietu Mudleta (.mpackage) dla paska kalendarza.

- Wersja: PLUGIN_VERSION z pasek_kalendarz_arkadia.xml (jedyne zrodlo prawdy).
- config.lua: author Isithunzi000, bez pola created (determinizm).
- W mpackage XML nosi nazwe pakietu: "pasek kalendarz arkadia.xml".
- Wpisy sortowane, timestampy sztywne (1980-01-01), stale uprawnienia.
- Dwukrotny build daje identyczny SHA-256 (bramka publikacji w CI).
Wypisuje: sciezki artefaktow (dist/) i ich SHA-256.
"""
import hashlib
import os
import re
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
XML_NAME = "pasek_kalendarz_arkadia.xml"
XML_IN_PACKAGE = "pasek kalendarz arkadia.xml"
ASSET_BASE = "pasek_kalendarz"
PACKAGE = "pasek kalendarz arkadia"
TITLE = "Pasek kalendarza Arkadii (Ishtar / Imperium)"
DESCRIPTION = ("Zyjacy pasek kalendarza: zegar gry, data Ishtar/Imperium, "
               "dzien/noc, wskaznik CIEMNO pod paskiem. Synchronizacja wylacznie "
               "na swiadome zadanie gracza (komenda czas, klik w pasek, alias "
               "pasek) oraz pasywnie z GMCP; rekalibracja na wschodzie/zachodzie "
               "slonca. Plugin nigdy nie wysyla komend samodzielnie (pkt 2 Zasad "
               "Arkadii). Komendy: pasek pomoc (pozycja, kolory, tlo, domyslne).")
OUT_DIR = os.path.join(ROOT, "dist")
FIXED_DATE = (1980, 1, 1, 0, 0, 0)
FILE_ATTR = 0o100644 << 16


def plugin_version():
    with open(os.path.join(ROOT, XML_NAME), encoding="utf-8") as f:
        m = re.search(r'local PLUGIN_VERSION = "([^"]+)"', f.read())
    if not m:
        raise SystemExit("BLAD: brak PLUGIN_VERSION w " + XML_NAME)
    return m.group(1)


def config_lua(version):
    return (
        'mpackage = "' + PACKAGE + '"\n'
        + 'author = "Isithunzi000"\n'
        + 'title = "' + TITLE + '"\n'
        + 'description = "' + DESCRIPTION + '"\n'
        + 'version = "' + version + '"\n'
    )


def write_entry(zf, arcname, data):
    zi = zipfile.ZipInfo(arcname, date_time=FIXED_DATE)
    zi.external_attr = FILE_ATTR
    zi.compress_type = zipfile.ZIP_DEFLATED
    zf.writestr(zi, data)


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    version = plugin_version()
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(os.path.join(ROOT, XML_NAME), "rb") as f:
        xml_bytes = f.read()

    base = ASSET_BASE + "_" + version.replace(".", "_")
    mpackage_path = os.path.join(OUT_DIR, base + ".mpackage")
    with zipfile.ZipFile(mpackage_path, "w") as zf:
        write_entry(zf, "config.lua", config_lua(version).encode("utf-8"))
        write_entry(zf, XML_IN_PACKAGE, xml_bytes)

    xml_asset = os.path.join(OUT_DIR, base + ".xml")
    with open(xml_asset, "wb") as f:
        f.write(xml_bytes)

    for p in (mpackage_path, xml_asset):
        print(sha256(p) + "  " + p)


if __name__ == "__main__":
    main()
