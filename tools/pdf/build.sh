#!/usr/bin/env bash
# Build the PDF edition of the book from the Markdown sources.
#
#   tools/pdf/build.sh [EDITION] [VERSION]
#
# EDITION is "en" (default: the original edition, chapters/ and appendices/),
# "fr" (the French edition, fr/chapters/ and fr/appendices/) or "ar" (the
# Arabic edition, ar/chapters/ and ar/appendices/, typeset by LuaLaTeX).
# VERSION is printed on the copyright page (for example "v1.1"). When it is
# omitted, the build is labelled as a development build with the commit hash.
# For compatibility, a first argument that is not an edition is taken as the
# version of the English edition: "build.sh v1.1" is "build.sh en v1.1".
#
# Output: build/openstack-the-day-after-tomorrow.pdf for the English edition,
# build/openstack-the-day-after-tomorrow-fr.pdf for the French one,
# build/openstack-the-day-after-tomorrow-ar.pdf for the Arabic one (plus the
# LaTeX sources and logs, in build/, which is ignored by Git).
#
# An edition still being translated (PARTIAL_OK=1 below) is built from the
# chapters that exist; the missing sources are listed in build/<name>.missing
# so that verify_pdf.py relaxes the checks that depend on completeness.
#
# Requirements: pandoc (>= 3.1), XeLaTeX and LuaLaTeX (TeX Live with
# tcolorbox, titlesec, fancyhdr, microtype, enumitem, caption, babel with the
# Arabic locale), the TeX Gyre and DejaVu fonts, Amiri and Noto Kufi Arabic
# for the Arabic edition, rsvg-convert (librsvg) for the SVG figures.

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT"

EDITION="en"
if [[ "${1:-}" == "en" || "${1:-}" == "fr" || "${1:-}" == "ar" ]]; then
  EDITION="$1"; shift
fi
VERSION="${1:-${BOOK_VERSION:-}}"
if [[ -z "$VERSION" ]]; then
  VERSION="development build ($(git rev-parse --short HEAD 2>/dev/null || echo unversioned))"
fi
DATE="$(date -u +%Y-%m-%d)"
REPO_URL="https://github.com/soufian-zaouam/openstack-the-day-after-tomorrow"

BUILD=build
NAME=openstack-the-day-after-tomorrow
mkdir -p "$BUILD"

# ---- 0. Edition: sources, metadata, title page, figures ----------------------
# All editions share the template, the layout (header.tex) and the Lua filter,
# which recognises the structural markers of each language (see fr/STYLE.md,
# ar/STYLE.md). ENGINE is the LaTeX engine; PARTIAL_OK=1 allows a translation
# in progress to be built from the chapters that exist.
ENGINE=xelatex
PARTIAL_OK=0
case "$EDITION" in
  en)
    SRC=.
    METADATA=tools/pdf/metadata.yaml
    HEADER_EXTRA=()
    FRONT_MATTER=chapters/00-front-matter.md
    FIGURES=assets/figures
    SOURCES=(
      chapters/00-how-to-read-this-book.md
      chapters/00-introduction.md
      chapters/0[1-9]-*.md
      chapters/1[0-9]-*.md
      chapters/20-*.md
      chapters/21-*.md
      appendices/appendix-[a-f]-*.md
      appendices/references-and-further-reading.md
    )
    TITLE="OpenStack,\\\\ the Day After Tomorrow"
    SUBTITLE="Operating Mission-Critical OpenStack Platforms"
    ABOUT="\\textbf{About this edition.} Version \\bookversion, generated on \\bookdate\\ from the
Markdown sources published at \\url{$REPO_URL}. Corrections and suggestions are
welcome through the issues of that repository."
    ;;
  fr)
    SRC=fr
    NAME="$NAME-fr"
    METADATA=tools/pdf/metadata-fr.yaml
    HEADER_EXTRA=(--include-in-header tools/pdf/header-fr.tex)
    FRONT_MATTER=fr/chapters/00-pages-liminaires.md
    FIGURES=assets/figures/fr
    SOURCES=(
      fr/chapters/00-comment-lire-ce-livre.md
      fr/chapters/00-introduction.md
      fr/chapters/0[1-9]-*.md
      fr/chapters/1[0-9]-*.md
      fr/chapters/20-*.md
      fr/chapters/21-*.md
      fr/appendices/annexe-[a-f]-*.md
      fr/appendices/references-et-lectures-complementaires.md
    )
    TITLE="OpenStack,\\\\ après-demain"
    SUBTITLE="Exploiter des plateformes OpenStack critiques"
    ABOUT="\\textbf{À propos de cette édition.} Version \\bookversion, générée le \\bookdate\\ à partir des
sources Markdown publiées à l’adresse \\url{$REPO_URL}. Les corrections et suggestions
sont les bienvenues dans les issues de ce dépôt."
    ;;
  ar)
    SRC=ar
    NAME="$NAME-ar"
    ENGINE=lualatex
    PARTIAL_OK=1      # the Arabic edition is being translated by the community (see TRANSLATIONS.md)
    METADATA=tools/pdf/metadata-ar.yaml
    HEADER_EXTRA=(--include-in-header tools/pdf/header-ar.tex)
    FRONT_MATTER=ar/chapters/00-front-matter.md
    FIGURES=assets/figures/ar
    SOURCES=(
      ar/chapters/00-how-to-read-this-book.md
      ar/chapters/00-introduction.md
      ar/chapters/0[1-9]-*.md
      ar/chapters/1[0-9]-*.md
      ar/chapters/20-*.md
      ar/chapters/21-*.md
      ar/appendices/appendix-[a-f]-*.md
      ar/appendices/references-and-further-reading.md
    )
    TITLE="OpenStack،\\\\ بعد غد"
    SUBTITLE="تشغيل منصّات OpenStack الحرجة"
    ABOUT="\\textbf{عن هذه الطبعة.} الإصدار \\foreignlanguage{english}{\\bookversion}، أُنشئ بتاريخ \\foreignlanguage{english}{\\bookdate} من مصادر
Markdown المنشورة في \\url{$REPO_URL}. التصويبات والاقتراحات
مرحّب بها في issues ذلك المستودع."
    ;;
esac
echo "Edition: $EDITION"

# ---- 1. Ordered list of sources ---------------------------------------------
# A glob that matches nothing stays literal; an edition in progress may skip it.
rm -f "$BUILD/$NAME.missing"
PRESENT=()
for f in "${SOURCES[@]}"; do
  if [[ -f "$f" ]]; then
    PRESENT+=("$f")
  elif [[ "$PARTIAL_OK" == 1 ]]; then
    echo "$f" >> "$BUILD/$NAME.missing"
  else
    echo "missing source: $f" >&2; exit 1
  fi
done
[[ -f "$FRONT_MATTER" ]] || { echo "missing front matter: $FRONT_MATTER" >&2; exit 1; }
SOURCES=("${PRESENT[@]}")
if [[ -s "$BUILD/$NAME.missing" ]]; then
  echo "Sources: ${#SOURCES[@]} files (edition in progress: $(wc -l < "$BUILD/$NAME.missing") source(s) not yet translated, listed in $BUILD/$NAME.missing)"
else
  echo "Sources: ${#SOURCES[@]} files"
fi

# ---- 2. Version stamp, title page and colophon (copyright page) --------------
cat > "$BUILD/version.tex" <<EOF
\\newcommand{\\bookversion}{$VERSION}
\\newcommand{\\bookdate}{$DATE}
\\newcommand{\\booktitle}{$TITLE}
\\newcommand{\\booksubtitle}{$SUBTITLE}
EOF

# The copyright page is the text of the front-matter file between the first
# horizontal rule (after the title block) and the navigation footer.
awk 'BEGIN{n=0} /^---$/{n++; next} n==1{print}' "$FRONT_MATTER" \
  | pandoc -f markdown -t latex -o "$BUILD/colophon-body.tex"
{
  cat "$BUILD/colophon-body.tex"
  printf '\n\\vspace{1em}\n%s\n' "$ABOUT"
} > "$BUILD/colophon.tex"

# ---- 3. Figures: SVG -> PDF (vector) ------------------------------------------
rm -rf "$BUILD/figures"; mkdir -p "$BUILD/figures"
for svg in "$FIGURES"/*.svg; do
  rsvg-convert -f pdf -o "$BUILD/figures/$(basename "${svg%.svg}").pdf" "$svg"
done
echo "Figures: $(ls "$BUILD"/figures/*.pdf | wc -l) converted from $FIGURES"

# ---- 4. Markdown -> LaTeX -----------------------------------------------------
pandoc "${SOURCES[@]}" \
  --from markdown+smart+autolink_bare_uris \
  --to latex \
  --template tools/pdf/template.tex \
  --metadata-file "$METADATA" \
  --include-in-header tools/pdf/header.tex \
  ${HEADER_EXTRA[@]+"${HEADER_EXTRA[@]}"} \
  --lua-filter tools/pdf/filters/book.lua \
  --resource-path=.:"$SRC"/chapters:"$SRC"/appendices \
  --top-level-division=chapter \
  --pdf-engine="$ENGINE" \
  --standalone \
  --output "$BUILD/$NAME.tex"

# ---- 5. LaTeX -> PDF (three passes for the table of contents and marks) -------
for pass in 1 2 3; do
  echo "$ENGINE pass $pass"
  "$ENGINE" -interaction=nonstopmode -halt-on-error -file-line-error \
          -output-directory="$BUILD" "$BUILD/$NAME.tex" > "$BUILD/$ENGINE-pass$pass.out" 2>&1 \
    || { echo "$ENGINE failed on pass $pass — last lines of the log:" >&2; tail -n 40 "$BUILD/$NAME.log" >&2; exit 1; }
done

test -s "$BUILD/$NAME.pdf" || { echo "PDF was not produced" >&2; exit 1; }
echo "Built $BUILD/$NAME.pdf ($(du -h "$BUILD/$NAME.pdf" | cut -f1), $(pdfinfo "$BUILD/$NAME.pdf" | awk '/^Pages/{print $2}') pages, $VERSION)"
