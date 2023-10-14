state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]


def add_round_key(s, k):
    cols , rows = 4,4 
    temp =[[0 for i in range(cols)] for j in range(rows)]
    for i in range(0,4):
         for j in range(0,4):
              temp[i][j] = s[i][j] ^ k[i][j]
    return temp     
    

def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    nam =''
    for i in range(0,4):
        for j in range(0,4):
            nam = nam + chr(matrix[i][j])
    return nam        
# print(state^round_key)

# print(add_round_key(state, round_key))
print(matrix2bytes(add_round_key(state, round_key)))
