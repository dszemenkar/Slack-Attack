import backend

rows = backend.view("messages")

for row in rows:
	print(row)