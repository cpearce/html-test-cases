import os


print("""
<!DOCTYPE html>
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
</head>
<body>
<ul>
""")

paths = list(filter(lambda p: p != "index.html" and p.endswith(".html"), os.listdir(".")))
for p in paths:
  print('<li><a href="{}">{}</a></li>'.format(p, p))

print("""
</ul>
</body>
</html>
""")

