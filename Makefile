all: functions

manual.html:
	curl -qL http://nl3.php.net/get/php_manual_en.html.gz/from/this/mirror | gunzip > manual.html

functions: manual.html
	python phpparse.py manual.html > functions || rm -f functions

clean:
	rm -f manual.html functions

.PHONY: all clean
