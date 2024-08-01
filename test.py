from pkgs.color.zyjared_color import Color, ColorStatic as Colors,red,  bold, blue, italic, underline, through,yellow


text = Color('Hello World!').red().bold()
print(text)


text = Colors.red('Hello World!').bold()
print(text)

text = red('Hello World!').bold()
print(text)

text = italic(text)
print(text)

text = red('Hello World!').bold().italic().underline().through()
print(text)

text = text = through(underline(italic(bold(red('Hello World!')))))
print(text)

text = text + ' !!! ' + blue('Hello World!')
print(text)

text.yellow()
print(text)