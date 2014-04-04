import math
from operator import itemgetter
from fuzzy_set_rules import readFuzzySetFile

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
    angles['lra'] = get_angle(B, A, C)
    angles['lla'] = get_angle(B, C, A)
    angles['ura'] = get_angle(D, A, C)
    angles['ula'] = get_angle(D, C, A)
    return angles

if __name__ == '__main__':
    from config import get_data
    fuzzy_rules = readFuzzySetFile('smile_data_set.data')
    data = get_data()


    correct = 0
    total_smiles = 0

    for subject, states in data.iteritems():
        for face, points in states.iteritems():
            print subject, ': ', face
            angles = refine_raw_data(points)
            print 'angles: ', angles
            upper_max = max(angles['ura'], angles['ula'])
            lower_max = max(angles['lra'], angles['lla'])

            result = []
            for state, fuzzy_rule in fuzzy_rules.iteritems():
                fuzzy_value = fuzzy_rule.activate(upper_max, lower_max)
                print '\t', state, ": ", fuzzy_value
                result.append((state, fuzzy_value))                

            output = max(result, key=itemgetter(1))

            if 'smile' in output[0]:
                    correct += 1

            if 'smile' in face:
                total_smiles += 1

    if total_smiles != 0:
        print '---------------------------------'
        print 'total samples: ', total_smiles
        print 'correct samples: ', correct
        print float(correct)/float(total_smiles)