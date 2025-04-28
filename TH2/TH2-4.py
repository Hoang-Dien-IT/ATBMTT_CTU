#Nguyễn Hoàng Điển
#B2113329
#20
# Initial Permutation (IP) table
IP = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]

# Final Permutation (FP) table
FP = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
]

def permute(block, table):
    return ''.join([block[table[i] - 1] for i in range(len(table))])

def Encrypt_IP(block):
    return permute(block, IP)

def Decrypt_IP(block):
    return permute(block, FP)

# Permuted Choice 1 (PC1) table
PC1 = [
    57, 49, 41, 33, 25, 17, 9,
    1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27,
    19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29,
    21, 13, 5, 28, 20, 12, 4
]

# Permuted Choice 2 (PC2) table
PC2 = [
    14, 17, 11, 24, 1, 5,
    3, 28, 15, 6, 21, 10,
    23, 19, 12, 4, 26, 8,
    16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32
]

# Number of left shifts per round
SHIFT_SCHEDULE = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

def left_shift(key, shifts):
    return key[shifts:] + key[:shifts]

def Generation_Key(key):
    # Apply PC1
    key = permute(key, PC1)
    # Split key into two halves
    left = key[:28]
    right = key[28:]
    round_keys = []
    for shift in SHIFT_SCHEDULE:
        # Shift both halves
        left = left_shift(left, shift)
        right = left_shift(right, shift)
        # Combine and apply PC2
        combined = left + right
        round_key = permute(combined, PC2)
        round_keys.append(round_key)
    return round_keys

# Expansion table
E = [
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
]

# S-boxes
S_BOX = [
    # S1
    [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
    [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
    [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
    [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
    # S2 to S8 omitted for brevity
]

# Permutation table
P = [
    16, 7, 20, 21,
    29, 12, 28, 17,
    1, 15, 23, 26,
    5, 18, 31, 10,
    2, 8, 24, 14,
    32, 27, 3, 9,
    19, 13, 30, 6,
    22, 11, 4, 25
]

def expand(block):
    return permute(block, E)

def substitute(block):
    # Split block into 8 parts of 6 bits each
    blocks = [block[i*6:(i+1)*6] for i in range(8)]
    result = ""
    for i in range(8):
        block = blocks[i]
        row = int(block[0] + block[5], 2)
        col = int(block[1:5], 2)
        val = S_BOX[i][row][col]
        result += format(val, '04b')
    return result

def permute_p(block):
    return permute(block, P)

def round_function(block, round_key):
    expanded = expand(block)
    xored = ''.join(str(int(expanded[i]) ^ int(round_key[i])) for i in range(48))
    substituted = substitute(xored)
    permuted = permute_p(substituted)
    return permuted