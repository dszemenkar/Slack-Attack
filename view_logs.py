import backend

rows = backend.view("logs")

for row in rows:
	print(row)