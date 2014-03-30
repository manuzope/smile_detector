def get_data():
    h = {}
    h["no_smile"] = [(300, 288), (327, 304), (356, 290), (330, 279), (279, 208), (381, 210)]
    h["smile"] = [(290, 280), (329, 318), (356, 285), (328, 283), (278, 212), (383, 216)]
    h["awkward_smile"] = [(252, 312), (283, 323), (314, 313), (282, 307), (240, 259), (326, 260)]
    h["ff_smile"] = [(257, 318), (291, 337), (324, 319), (292, 319), (246, 264), (335, 265)]
    h["frown"] = [(269, 333), (294, 342), (317, 335), (294, 320), (252, 255), (343, 257)]
    h["duckface"] = [(266, 305), (282, 325), (302, 308), (283, 290), (239, 253), (326, 251)]
    h["teeth_no_smile"] = [(237, 345), (263, 365), (296, 346), (264, 331), (223, 278), (312, 276)]
    return h

data = get_data()
for a in data:
    val = data[a]
    assert len(val) == 6
