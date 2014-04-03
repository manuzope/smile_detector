from SimpleCV import *

def get_points(img):
    disp = Display()
    points = []
    while(disp.isNotDone()):
        if (disp.mouseLeft and disp.leftButtonDownPosition() != None):
            x = disp.mouseX
            y = disp.mouseY
            point = (x, y)
            print point
            points.append(point)
            if len(points) == 6:
                disp.done = True

        img.save(disp)

    print points
    return points

def get_filename(fn):
    f = fn.split("/")
    f = f[len(f) - 1]
    f = f.split(".")[0]
    return f

iset = ImageSet("images/anshika")
image_dict = {}

for img in iset:
    fn = get_filename(img.filename)
    points = get_points(img)
    image_dict[fn] = points

print image_dict
 
