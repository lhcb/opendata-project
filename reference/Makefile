DOCUMENT_MARKDOWN = lhcb-opendata-reference.md

DOCUMENT_LATEX = lhcb-opendata-reference.tex
DOCUMENT_PDF = ../Background-Information-Notebooks/FunctionReferences.pdf

LATEX_SETTINGS = \
    -V documentclass:article \
    -V papersize:a4paper \
    -V fontsize:10pt \
    -V geometry:margin=1in

PANDOC_ARGS = \
    --standalone \
    $(LATEX_SETTINGS)


all: latex pdf

latex: $(DOCUMENT_LATEX)

pdf: $(DOCUMENT_PDF)

non-stop:
	- make
	- while inotifywait -e close_write *; do make; done


$(DOCUMENT_LATEX): $(DOCUMENT_MARKDOWN)
	- pandoc $(PANDOC_ARGS) $(DOCUMENT_MARKDOWN) -o $(DOCUMENT_LATEX)

$(DOCUMENT_PDF): $(DOCUMENT_LATEX)
	- rm -rf tmp
	- mkdir tmp
	- cp $(DOCUMENT_LATEX) tmp/document.tex
	# Make tables narrower
	- sed -i "s#\\\begin{minipage}\[b\]{0.47\\\columnwidth}\\\raggedright\\\strut#\\\begin{minipage}\[b\]{0.4\\\columnwidth}\\\raggedright\\\strut#g" tmp/document.tex
	- sed -i "s#\\\begin{minipage}\[t\]{0.47\\\columnwidth}\\\raggedright\\\strut#\\\begin{minipage}\[t\]{0.4\\\columnwidth}\\\raggedright\\\strut#g" tmp/document.tex
	# Add vertical lines
	# - sed -i "s#\\\begin{longtable}\[\]{@{}ll@{}}#\\\begin{longtable}[]{|l|l|}#g" tmp/document.tex
	# Remove "Table X: " from captions
	- sed -i "s#\\\caption{#\\\caption*{#g" tmp/document.tex
	# Replace \textasciitilde{} with ~
	- sed -i "s#\\\textasciitilde{}#~#g" tmp/document.tex
	- latexmk -xelatex -halt-on-error -output-directory=tmp/ tmp/document.tex
	- mv tmp/document.pdf $(DOCUMENT_PDF)
