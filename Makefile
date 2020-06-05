gen_stubs:
	rm -rf scrapli
	stubgen -p scrapli -o . --include-private
