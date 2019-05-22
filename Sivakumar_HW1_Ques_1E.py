# Namrata Sivakumar
# nxs8168
# North, South, East, West
import turtle

north_x = 0
north_y = 100

south_x = 0
south_y = -100

west_x = -100
west_y = 0

east_x = 100
east_y = 0

origin_x = 0
origin_y = 0

turtle.goto(north_x, north_y )
turtle.goto(north_x-1, north_y+1)

turtle.write("North")


turtle.goto(origin_x, origin_y)
turtle.penup()


turtle.goto(south_x, south_y)
turtle.goto(south_x-1,south_y-5)
turtle.pendown()
turtle.write("South")

turtle.goto(origin_x, origin_y)
turtle.pendown()

turtle.goto(west_x, west_y)
turtle.goto(west_x-3, west_y)
turtle.write("West")

turtle.goto(origin_x, origin_y)
turtle.pendown()

turtle.goto(east_x, east_y)
turtle.goto(east_x+3, east_y)
turtle.write("East")

turtle.goto(origin_x, origin_y)
turtle.pendown()

turtle.goto(origin_x, -20)
turtle.circle(20)


turtle.done()
#turtle.clearscreen()