all:
	pdflatex -shell-escape slides_animated.tex && biber slides_animated && pdflatex -shell-escape slides_animated && pdflatex -shell-escape slides_animated && evince slides_animated.pdf&

simple:
	pdflatex  -shell-escape slides_animated.tex && evince slides_animated.pdf&

clean:
	rm -f  *.sov *.vrb *.aux *.toc *.log *.nav *.out *.snm *.blg *.bbl *.bcf *.run.xml *.brf *~ renum.tex

renum:
	cp slides_animated.tex slides_animated.tex.sov
	python3 renumber-slides.py && mv renum.tex slides_animated.tex
