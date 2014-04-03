from membership import large_negative_ang, negative_ang,\
                       zero_ang, positive_ang, large_positive_ang

dispatcher = {
    'large_negative_ang' : large_negative_ang,
    'negative_ang' : negative_ang,
    'zero_ang' : zero_ang,
    'positive_ang' : positive_ang,
    'large_positive_ang' : large_positive_ang
}

output = {
    'smile',
    'neutral',
    'frown'
}

class FuzzySetRule:
    def __init__(self):
        self._upperAngleRules = []
        self._lowerAngleRules = []

    def addUpperAngleRule(self, func):
        self._upperAngleRules.append(func)
        
    def addLowerAngleRule(self, func):
        self._lowerAngleRules.append(func)

    def activate(self, upper_ang, lower_ang):
        results = []
        for func1, func2 in zip(self._upperAngleRules, self._lowerAngleRules):
            results.append(min(func1(upper_ang), func2(lower_ang)))

        return max(results)

def readFuzzySetFile(input_file):
    fuzzy_set_rules = {}
    with open(input_file, 'r') as f:
        for line in f:
            tokens = line.strip().split(' ')
            n = len(tokens)
            output = tokens[n-1]

            if output not in fuzzy_set_rules:
                fuzzy_set_rules[output] = FuzzySetRule()

            rule1 = dispatcher[tokens[3]]
            rule2 = dispatcher[tokens[7]]

            fuzzy_set_rules[output].addUpperAngleRule(rule1)
            fuzzy_set_rules[output].addLowerAngleRule(rule2)

    return fuzzy_set_rules

fuzzy_rules = readFuzzySetFile('smile_data_set.tsv')