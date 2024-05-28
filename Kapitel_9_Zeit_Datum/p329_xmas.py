from datetime import date

xmas = date(2023,11,4)

silvester = xmas.replace(year=2024,month=4,day=21)

print(xmas.strftime("Xmas %Y:"),xmas)
print(silvester.strftime("Silvester %Y: "),silvester)
print("Dt zwischen "+silvester.strftime("Silvester %Y ") +"und " +xmas.strftime("Xmas %Y ="), silvester-xmas)