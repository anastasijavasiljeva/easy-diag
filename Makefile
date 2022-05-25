target: start-client start-server

start-client: 
	npx webpack --mode production

start-server:
	python .\app.py