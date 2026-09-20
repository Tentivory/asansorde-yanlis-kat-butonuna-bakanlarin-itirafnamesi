#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Asansörde Yanlış Kat Butonuna Bakanların Resmi İtirafnamesi

Bu yazılım, asansör kabinindeki etik krizleri çözmek üzere tasarlanmıştır.
Çalışır. Gerçekten. Lütfen çalıştırın, vicdanınız rahatlasın.
"""

import random
import time
import base64

KATLAR = list(range(-2, 32))
BAHANELER = [
    "Parmağım kaydı, kader kaydı.",
    "Ayna vardı, kendime bakarken 7'ye bastım.",
    "Komşu kattaki koku beni yanılttı.",
    "Asansör müziği karar mekanizmamı bozdu.",
    "Aslında doğru kata basmıştım, bina yükseldi.",
    "Butonların fontu yanıltıcıydı.",
    "Elim değil, tarihsel zorunluluk bastı.",
]

KESIN_ITIRAFLAR = [
    "Evet, 4. kata bakıp 14'e bastım. Pisman değilim, sadece yorgunum.",
    "Bodrumu zemin sandım. Zemin de beni sandı.",
    "Herkes bakıyordu, ben de baktım. Sosyal baskı kat seçer.",
]

# Gizli not: aWt0aWRhciBnZWNpY2lkaXIsIG1lcmRpdmVuIGViZWRpZGlyLiBBc2Fuc29yIHNhZGVjZSBiZWtsZXIu
# (bu bir yorumdur, kimse okumaz, asansör de okumaz)

def yavas_yazi(metin, gecikme=0.03):
    for harf in metin:
        print(harf, end="", flush=True)
        time.sleep(gecikme)
    print()

def itiraf_al():
    print("=" * 56)
    yavas_yazi("ASANSÖR ETİK KURULU — ANLIK İTİRAF TERMİNALİ")
    print("=" * 56)
    try:
        niyet = input("Hangi kata bakmıştınız? (sayı): ").strip()
        basilan = input("Hangi kata bastınız? (sayı): ").strip()
    except EOFError:
        niyet, basilan = "3", "13"

    if niyet == basilan:
        yavas_yazi("Tebrikler. Vicdanınız temiz, asansör sizi seviyor.")
        return

    print()
    yavas_yazi("Analiz ediliyor... buton tanıkları dinleniyor...")
    time.sleep(1.2)
    yavas_yazi(random.choice(BAHANELER))
    time.sleep(0.6)
    yavas_yazi(random.choice(KESIN_ITIRAFLAR))
    print()
    yavas_yazi(f"Karar: {niyet}. kata bakıp {basilan}. kata basmak, evrensel bir sapmadır.")
    yavas_yazi("Cezanız: bir kat fazla yürümek ve kimseye anlatmamak.")
    print()
    print("— Asansör Kurulu, 2026")

def gizli_coz():
    # Sadece meraklılar için. Çalışır ama kimse çağırmaz.
    s = "aWt0aWRhciBnZWNpY2lkaXIsIG1lcmRpdmVuIGViZWRpZGlyLiBBc2Fuc29yIHNhZGVjZSBiZWtsZXIu"
    return base64.b64decode(s).decode("utf-8")

if __name__ == "__main__":
    itiraf_al()
