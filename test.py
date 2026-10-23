import matrix as mt
import time
import sys
import msvcrt
WIDTH = 80
HEIGHT = 30
vert = [
    (x,y,z)
    for x in (-1,1)
    for y in (-1,1)
    for z in (-1,1)
]
edges = [
    (i,j)
    for i in range(8)
    for j in range(i+1,8)
    if sum(
        abs(vert[i][k] - vert[j][k])
        for k in range(3)
    ) == 2
]
def rotate(x,y,z,ax,ay,az):
    vector = mt.matrixRotateRad([[x],[y],[z]],ax,0,0,"x")
    vector = mt.matrixRotateRad(vector,0,ay,0,"y")
    vector = mt.matrixRotateRad(vector,0,0,az,"z")
    return vector[0][0],vector[1][0],vector[2][0]
def project(x,y,z):
    dist = 4
    persp = 30 / (z+dist)
    screen_x = int(WIDTH/2 + x * persp)
    screen_y = int(HEIGHT/2 - y * persp*0.5)
    return screen_x,screen_y
def draw_line(buffer,x1,y1,x2,y2):
    dx = abs(x2-x1)
    dy = abs(y2-y1)
    sx =1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    error = dx - dy
    while True:
        if 0 <= x1 < WIDTH and 0 <= y1 < HEIGHT:
            buffer[y1][x1] = "#"
        if x1 == x2 and y1 == y2:
            break
        error2 = 2 * error
        if error2 > -dy:
            error -= dy
            x1+=sx
        if error2 < dx:
            error +=dx
            y1 += sy
def main():
    ax = 0.0
    ay = 0.0
    az = 0.0
    step = 0.08
    sys.stdout.write("\033[?251\033[2J")
    sys.stdout.flush()
    try:
        while True:
            if msvcrt.kbhit():
                key = msvcrt.getch().lower()
                if key ==b'w':
                    ax += step
                elif key ==b's':
                    ax -= step
                elif key ==b'a':
                    ay -= step
                elif key ==b'd':
                    ay += step
                elif key ==b'q':
                    az -=step
                elif key ==b'e':
                    az += step
                elif key ==b'r':
                    ax=ay=az=0
                elif key ==b'\x1b':
                    break
            buffer = [
                [" "] * WIDTH
                for _ in range(HEIGHT)
            ]
            points = []
            for x,y,z in vert:
                rx,ry,rz = rotate(x,y,z,ax,ay,az)

                length = (rx**2 + ry**2 + rz**2)**0.5
                if length > 1.74 or length < 1.72:
                    print(f"Error:={length:.8f},"
                          f"coor:={rx,ry,rz}")
                sx,sy = project(rx,ry,rz)
                points.append((sx,sy))
            for i,j in edges:
                x1,y1 = points[i]
                x2,y2 = points[j]
                draw_line(buffer,x1,y1,x2,y2)
            frame = "\n".join("".join(row) for row in buffer)
            sys.stdout.write("\033[H" + frame)
            sys.stdout.flush()


            time.sleep(0.05)
    except KeyboardInterrupt:
        pass
    finally:
        sys.stdout.write("\033[?25h\n")
        sys.stdout.flush()
if __name__ == "__main__":
    main()
