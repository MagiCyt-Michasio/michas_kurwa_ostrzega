# Michaś Kurwa Ostrzega — kontekst projektu

## Cel
Krótkie rolki TikTok/Reels o psychologii, relacjach i życiu.
Styl: format 9:16, czarne tło, neonowe linie, minimalizm, emocjonalny punchline.

## Pipeline
koncepcja → scenariusz → kod Manim → GitHub → Debian → render MP4 → montaż → publikacja

## Źródło prawdy
1. GitHub: https://github.com/MagiCyt-Michasio/michas_kurwa_ostrzega
2. PROJECT_CONTEXT.md
3. Historia commitów
4. Rzeczywisty stan i wyniki poleceń na Debianie

Pamięć czatów AI nie jest źródłem stanu projektu.

## Role
- Użytkownik: właściciel i decyzje końcowe.
- Perplexity: PM/DevOps, repo, Debian, Manim, testy, debugowanie, kontrola zmian.
- GPT/Grażynka: koncepcje, storytelling, scenariusze, wykresy i sceny Manim.
- Gemini/Gremlin: druga opinia i alternatywne rozwiązania.

## Zasady zmian
Przed zmianą: sprawdź repo, PROJECT_CONTEXT.md i zakres zadania.
Po zmianie: sprawdź kod, test/render, opisz wynik.
Gdy danych brakuje: „Nie wiem”, bez zgadywania.

## Środowisko
- Debian 13.5
- Python w .venv
- Manim Community Edition
- Render lokalny do MP4
- Brak założenia o GPU

## Aktualna faza
Bootstrap repozytorium.
Najbliższy cel: zainstalować Manim w .venv i wyrenderować HelloWorld.
