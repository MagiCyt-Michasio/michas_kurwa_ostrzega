#!/usr/bin/env bash
set -euo pipefail

mkdir -p scenes presets assets/fonts assets/audio tests renders

cat > README.md <<'README'
# Michaś Kurwa Ostrzega

Krótkie rolki tworzone w Manimie:
neonowe wykresy na czarnym tle, psychologia, relacje i życie.
README

cat > PROJECT_CONTEXT.md <<'CONTEXT'
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
CONTEXT

cat > .gitignore <<'IGNORE'
.venv/
__pycache__/
*.py[cod]
.env
.env.*
*.pem
*.key
media/
renders/
*.mp4
*.mov
*.webm
*.gif
*.png
.vscode/
.idea/
IGNORE

printf 'manim\n' > requirements.txt

cat > render.sh <<'RENDER'
#!/usr/bin/env bash
set -euo pipefail
source .venv/bin/activate
manim -pqh "$1" "$2"
RENDER

cat > scenes/hello_world.py <<'PY'
from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16
config.background_color = "#050505"

class HelloWorld(Scene):
    def construct(self):
        title = Text("MICHAŚ KURWA OSTRZEGA", font_size=48, color=WHITE)
        subtitle = Text("Manim render test", font_size=30, color=TEAL_A)
        subtitle.next_to(title, DOWN, buff=0.35)
        self.play(Write(title), run_time=1.4)
        self.play(FadeIn(subtitle), run_time=0.7)
        self.wait(1)
PY

touch assets/fonts/.gitkeep assets/audio/.gitkeep presets/.gitkeep renders/.gitkeep
chmod +x render.sh

echo "BOOTSTRAP_OK"
find . -maxdepth 3 -type f | sort
