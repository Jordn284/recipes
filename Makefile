all: init compile package

init: kit-init kit-package

kit-init:
	git clone https://github.com/creativetimofficial/material-kit.git kit
	cd kit ; npm install

kit-package:
	cd kit;./node_modules/gulp/bin/gulp.js compile-scss
	cp -r kit/assets out/assets

compile:
	python compile.py

package:
	zip -r package.zip out

clean:
	rm -rf ./out
