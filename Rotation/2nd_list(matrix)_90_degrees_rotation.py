# 2차원 리스트(행렬)를 90도 회전하는 메서드
def rotate_a_matrix_by_90_degrees(a):
    row_length = len(a)
    columns_lenth = len(a[0])

    res = [[0] * row_length for _ in range(columns_lenth)]
    for r in range(row_length):
        for c in range(columns_lenth):
            res[c][row_length - 1 - r] = a[r][c]
    return res


a = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

print(rotate_a_matrix_by_90_degrees(a))
