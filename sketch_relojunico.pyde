y = 0

def setup() :
    size(300, 600)

def draw() :
    global y
    background(175)



    ellipse(width/ 2, y, 50, 50)
    fill(81, 301, 237)
    if y > height :
        y = 0
    else:
        y = map(second(), 0, 59, 0, height)



    ellipse(width/ 2, y, 50, 50)
    fill(59, 42, 103)
    if y > height :
        y = 0
    else:
        y = map(minute(), 0, 59, 0, height)



    ellipse(width/ 2, y, 50, 50)
    fill(412, 56, 541)
    if y > height :
        y = 0
    else:
        y = map(hour(), 0, 24, 0, height)
