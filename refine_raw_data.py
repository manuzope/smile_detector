import math

def euclidian_distance((x1, y1), (x2, y2)):
    return math.sqrt(((math.fabs(y1 - y2))**2)+((math.fabs(x1 - x2))**2))

def get_angle(p_A, p_B, p_C):
    a = euclidian_distance(p_B, p_C)
    b = euclidian_distance(p_A, p_C)
    c = euclidian_distance(p_B, p_A)

    cosB = ((b**2) - (a**2) - (c**2))/(-2*a*c)
    return math.degrees(math.acos(cosB))

def refine_raw_data(points):
    angles = {}
    [A, B, C, D, E, F] = points
    angles['CAB'] = get_angle(C, A, B)
    angles['ACB'] = get_angle(A, C, B)
    angles['DAC'] = get_angle(D, A, C)
    angles['CAD'] = get_angle(C, A, D)
    return angles

if __name__ == '__main__':
    from config import get_data
    data = get_data()
    print refine_raw_data(data['manu']['manu_no_smile'])
