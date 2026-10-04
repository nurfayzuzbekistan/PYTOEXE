# PYTOEXE

Bu loyiha HTML + CSS + JSdan tayyorlangan oddiy dasturni Python orqali `.exe` formatiga o'girish uchun yaratilgan.

## Loyihadagi fayllar

- `index.html` - bitta HTML fayl, ichida CSS va JS mavjud.
- `app.py` - HTML faylni ochish uchun Python skripti.
- `build_exe.py` - PyInstaller yordamida `.exe` yaratish uchun skript.
- `requirements.txt` - kerakli paketlar ro'yxati.

## Qadamlar

```bash
python -m venv .venv
source .venv/bin/activate   # Windows uchun: .venv\Scripts\activate
pip install -r requirements.txt
python build_exe.py
```

Yakunida `dist/HTMLApp.exe` fayli hosil bo'ladi.

## HTML fayl haqida

`index.html` fayli ichida quyidagilar bor:
- CSS uslubi
- JavaScript funksionalligi
- localStorage orqali saqlangan vazifalar
- oddiy to-do app

## Eslatma

Bu yondashuv HTML/CSS/JS loyihasini kompilyatsiya qilish emas, balki uni `PyInstaller` orqali `.exe` sifatida paketlashdir.

Agar xohlasangiz, men keyinchalik sizga:
- kalkulyator
- quiz app
- portfolio website
- login form
- todo app
- shaxsiy dastur

shaklida yanada murakkab HTML loyihalarni ham yaratib bera olaman.
