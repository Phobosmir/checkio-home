

def draw_triangle(height):
    for i in range(height):
        print(' '*(height-i-1) + '*'*(2*i+1))


draw_triangle(5)
