def judgeCircle(moves: str) -> bool:
    origins = {'x': 0, 'y': 0}
    location = {'x': 0, 'y': 0}
    position = {'x': 1, 'y': 1}

    for move in moves:
        if move == 'U':
            position['y'] = 1
        elif move == 'D':
            position['y'] = -1
        if move == 'R':
            position['x'] = 1
        elif move == 'L':
            position['x'] = -1

        if move in ['L', 'R']:
            location['x'] += position['x']
        else:
            location['y'] += position['y']

    return origins == location


print(judgeCircle(moves = "LL"))
# print((0, 0) == (0, 1))

# class Solution:
#     def judgeCircle(self, moves: str) -> bool:
#         def move(a,i,j):
#             if(a=='L'):
#                 j-=1
#             elif(a=='R'):
#                 j+=1
#             elif(a=='U'):
#                 i-=1
#             else:
#                 i+=1
#             return i,j
#         i=j=0
#         for a in moves:
#             i,j=move(a,i,j)
#         return i==0 and j==0
