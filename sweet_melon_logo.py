import cs1graphics as cg

paper = cg.Canvas()
paper.setBackgroundColor('black')
paper.setWidth(600)
paper.setHeight(600)
paper.setTitle('Melon Logo')

uber_melon = cg.Ellipse(400, 750, cg.Point(300, 200))

uber_melon.setBorderWidth(100)

uber_melon.setBorderColor("green")

uber_melon.setFillColor('red')

paper.add(uber_melon)
