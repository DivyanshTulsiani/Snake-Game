# tim = Turtle()
# # timmy = Turtle()
# # tommy = Turtle()
# # tim.color("white")
# # timmy.color("white")
# # tommy.color("white")
# # tim.shape("square")
# # timmy.shape("square")
# # tommy.shape("square")
# # timmy.goto(-20,0)
# # tommy.goto(-40,0)
#
#

k = 0
segments = []
for i in range(0,3):
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(x=k,y=0)
    k -= 20
    segments.append(new_segment)
screen.update()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for seg_num in range(len(segments)-1,0,-1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x,new_y)
    segments[0].forward(20)
    segments[0].left(90)