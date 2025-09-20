bet_dict = {
    0: 'combo',
    1: 'color',
    2: 'even_odd',
    3: 'low_high',
    4: 'dozen',
    5: 'column',
    6: 'combo',
    7: 'combo',
    8: 'combo',
    9: 'combo',
}

from games.models import RouletteSpin

fields = {  "0": "green",
        "32": "red", "15": "black","19": "red",
        "4": "black", "21": "red", "2": "black",
        "25": "red", "17": "black", "34": "red",
        "6": "black", "27": "red", "13": "black",
        "36": "red", "11": "black", "30": "red",
        "8": "black", "23": "red", "10": "black",
        "5": "red", "24": "black", "16": "red",
        "33": "black", "1": "red", "20": "black",
        "14": "red", "31": "black","9": "red",
        "22": "black", "18": "red", "29": "black",
        "7": "red","28": "black", "12": "red",
        "35": "black", "3": "red", "26": "black",
    }

fields_in_order = { '0': 'green', '1': 'red', '2': 'black', '3': 'red', '4': 'black', '5': 'red',
                    '6': 'black', '7': 'red', '8': 'black', '9': 'red', '10': 'black', '11': 'black',
                    '12': 'red', '13': 'black', '14': 'red', '15': 'black', '16': 'red', '17': 'black',
                    '18': 'red', '19': 'red', '20': 'black', '21': 'red', '22': 'black', '23': 'red',
                    '24': 'black', '25': 'red', '26': 'black', '27': 'red', '28': 'black', '29': 'black',
                    '30': 'red', '31': 'black', '32': 'red', '33': 'black', '34': 'red', '35': 'black', '36': 'red'}

coordinates = {0: (0.0, 9.72972972972973),
               32: (9.72972972972973, 19.45945945945946), 15: (19.45945945945946, 29.18918918918919), 19: (29.18918918918919, 38.91891891891892),
               4: (38.91891891891892, 48.648648648648646), 21: (48.648648648648646, 58.37837837837838), 2: (58.37837837837838, 68.10810810810811),
               25: (68.10810810810811, 77.83783783783784), 17: (77.83783783783784, 87.56756756756756), 34: (87.56756756756756, 97.29729729729729),
               6: (97.29729729729729, 107.02702702702703), 27: (107.02702702702703, 116.75675675675676), 13: (116.75675675675676, 126.48648648648648),
               36: (126.48648648648648, 136.21621621621622), 11: (136.21621621621622, 145.94594594594594), 30: (145.94594594594594, 155.67567567567568),
               8: (155.67567567567568, 165.40540540540542), 23: (165.40540540540542, 175.13513513513513), 10: (175.13513513513513, 184.86486486486487),
               5: (184.86486486486487, 194.59459459459458), 24: (194.59459459459458, 204.32432432432432), 16: (204.32432432432432, 214.05405405405406),
               33: (214.05405405405406, 223.78378378378378), 1: (223.78378378378378, 233.51351351351352), 20: (233.51351351351352, 243.24324324324326),
               14: (243.24324324324326, 252.97297297297297), 31: (252.97297297297297, 262.7027027027027), 9: (262.7027027027027, 272.43243243243245),
               22: (272.43243243243245, 282.1621621621622), 18: (282.1621621621622, 291.8918918918919), 29: (291.8918918918919, 301.6216216216216),
               7: (301.6216216216216, 311.35135135135135), 28: (311.35135135135135, 321.0810810810811), 12: (321.0810810810811, 330.81081081081084),
               35: (330.81081081081084, 340.5405405405405), 3: (340.5405405405405, 350.27027027027026), 26: (350.27027027027026, 360.0)}


colors = {
    0: 'black',
    1: 'red'
}


even_odd = {
    0: 'even',
    1: 'odd'
}


low_high = {
    0: 'low',
    1: 'high'
}


dozens = {
    0: '1st 12',
    1: '2nd 12',
    2: '3rd 12'
}


columns = {
    0: '1st column',
    1: '2nd column',
    2: '3rd column'
}

bets_variants = {
    0: [str(i) for i in range(37)],
    1: colors,
    2: even_odd,
    3: low_high,
    4: dozens,
    5: columns,
}

splits = {
    # horizontal
    (1, 2): 0, (2, 3): 1,
    (4, 5): 2, (5, 6): 3,
    (7, 8): 4, (8, 9): 5,
    (10, 11): 6, (11, 12): 7,
    (13, 14): 8, (14, 15): 9,
    (16, 17): 10, (17, 18): 11,
    (19, 20): 12, (20, 21): 13,
    (22, 23): 14, (23, 24): 15,
    (25, 26): 16, (26, 27): 17,
    (28, 29): 18, (29, 30): 19,
    (31, 32): 20, (32, 33): 21,
    (34, 35): 22, (35, 36): 23,

    #vertical
    (1, 4): 24, (2, 5): 25, (3, 6): 26,
    (4, 7): 27, (5, 8): 28, (6, 9): 29,
    (7, 10): 30, (8, 11): 31, (9, 12): 32,
    (10, 13): 33, (11, 14): 34, (12, 15): 35,
    (13, 16): 36, (14, 17): 37, (15, 18): 38,
    (16, 19): 39, (17, 20): 40, (18, 21): 41,
    (19, 22): 42, (20, 23): 43, (21, 24): 44,
    (22, 25): 45, (23, 26): 46, (24, 27): 47,
    (25, 28): 48, (26, 29): 49, (27, 30): 50,
    (28, 31): 51, (29, 32): 52, (30, 33): 53,
    (31, 34): 54, (32, 35): 55, (33, 36): 56}

streets = {
    (1, 2, 3): 0,
    (4, 5, 6): 1,
    (7, 8, 9): 2,
    (10, 11, 12): 3,
    (13, 14, 15): 4,
    (16, 17, 18): 5,
    (19, 20, 21): 6,
    (22, 23, 24): 7,
    (25, 26, 27): 8,
    (28, 29, 30): 9,
    (31, 32, 33): 10,
    (34, 35, 36): 11
}

corners = {
    (1, 2, 4, 5): 0, (2, 3, 5, 6): 1,
    (4, 5, 7, 8): 2, (5, 6, 8, 9): 3,
    (7, 8, 10, 11): 4, (8, 9, 11, 12): 5,
    (10, 11, 13, 14): 6, (11, 12, 14, 15): 7,
    (13, 14, 16, 17): 8, (14, 15, 17, 18): 9,
    (16, 17, 19, 20): 10, (17, 18, 20, 21): 11,
    (19, 20, 22, 23): 12, (20, 21, 23, 24): 13,
    (22, 23, 25, 26): 14, (23, 24, 26, 27): 15,
    (25, 26, 28, 29): 16, (26, 27, 29, 30): 17,
    (28, 29, 31, 32): 18, (29, 30, 32, 33): 19,
    (31, 32, 34, 35): 20, (32, 33, 35, 36): 21
}

lines = {
    (1, 2, 3, 4, 5, 6): 0,
    (4, 5, 6, 7, 8, 9): 1,
    (7, 8, 9, 10, 11, 12): 2,
    (10, 11, 12, 13, 14, 15): 3,
    (13, 14, 15, 16, 17, 18): 4,
    (16, 17, 18, 19, 20, 21): 5,
    (19, 20, 21, 22, 23, 24): 6,
    (22, 23, 24, 25, 26, 27): 7,
    (25, 26, 27, 28, 29, 30): 8,
    (28, 29, 30, 31, 32, 33): 9,
    (31, 32, 33, 34, 35, 36): 10
}

win_values = {
    0: 36,
    6: 18,
    7: 12,
    8: 9,
    9: 6,
}

combo_variants = {

    6: splits,
    7: streets,
    8: corners,
    9: lines,
}





def is_win(spin: RouletteSpin) -> bool:
    types = {
        0: single_win,
        1: color_win,
        2: even_odd_win,
        3: low_high_win,
        4: dozen_win,
        5: column_win,
        6: combos_win,
        7: combos_win,
        8: combos_win,
        9: combos_win,
    }
    return types[int(spin.bet_type)](spin)

def combos_win(spin: RouletteSpin) -> bool:
    target_nums = [key for key in combo_variants[spin.bet_type] if combo_variants[spin.bet_type][key] == spin.bet_value][0]
    win_ranges = [coordinates[num] for num in target_nums]
    win = any([start < spin.result_value < end for start, end in win_ranges])
    if win:
        spin.win_value = spin.bet_amount * win_values[spin.bet_type]
        spin.user.profile.balance += spin.win_value
    return win

def single_win(spin: RouletteSpin) -> bool:
        win_range = coordinates[spin.bet_value]
        win = win_range[0] < spin.result_value < win_range[1]
        if win:
                spin.win_value = spin.bet_amount * 35 + spin.bet_amount
                spin.user.profile.balance += spin.win_value
        return win

def color_win(spin: RouletteSpin) -> bool:
    color_dict = { 0: 'black', 1: 'red' }

    target_color = color_dict[spin.bet_value]
    target_nums = [num for num in fields if fields[num] == target_color]

    win_ranges = [coordinates[int(num)] for num in target_nums]

    win = any([start < spin.result_value < end for start, end in win_ranges])

    if win:
        spin.win_value = spin.bet_amount * 2
        spin.user.profile.balance += spin.win_value
    return win

def even_odd_win(spin: RouletteSpin) -> bool:
    target_nums = [num for num in map(int, fields_in_order.keys()) if num % 2 == int(spin.bet_value)][1::]

    win_ranges = [coordinates[int(num)] for num in target_nums]
    win = any([start < spin.result_value < end for start, end in win_ranges])

    if win:
        spin.win_value = spin.win_value = spin.bet_amount * 2
        spin.user.profile.balance += spin.win_value
    return win

def low_high_win(spin: RouletteSpin) -> bool:
    target_nums = [range(1, 19), range(19, 37)][int(spin.bet_value)]

    win_ranges = [coordinates[num] for num in target_nums]

    win = any([start < spin.result_value < end for start, end in win_ranges])

    if win:
        spin.win_value = spin.win_value = spin.bet_amount * 2
        spin.user.profile.balance += spin.win_value
    return win

def dozen_win(spin: RouletteSpin) -> bool:
    target_nums = [range(1, 13), range(13, 25), range(26, 27)][int(spin.bet_value)]

    win_ranges = [coordinates[num] for num in target_nums]
    win = any([start < spin.result_value < end for start, end in win_ranges])

    if win:
        spin.win_value = spin.win_value = spin.bet_amount * 2 + spin.bet_amount
        spin.user.profile.balance += spin.win_value
    return win

def column_win(spin: RouletteSpin) -> bool:
    target_nums = [range(1, 37, 3), range(2, 37, 3), range(3, 37, 3)][int(spin.bet_value)]

    win_ranges = [coordinates[num] for num in target_nums]
    win = any([start < spin.result_value < end for start, end in win_ranges])

    if win:
        spin.win_value = spin.win_value = spin.bet_amount * 2
        spin.user.profile.balance += spin.win_value
    return win





