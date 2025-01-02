def ball_collide(ball1,ball2):
    ball1= float (x1,y1,r1)
    ball2= float (x2,y2,r2)
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance<=(r1+r2)
ball1=(0,0,5)
ball2=