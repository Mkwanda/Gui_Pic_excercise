
picture = [ 
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]

]
# pic_numbers = list(picture)
# items = 0
# val = 1

for rows  in  picture  :
    for pixels in rows:

       if  (pixels  == 1):
          print('*', end='')
       else :
          print (' ', end='')
    print('')
    # if i == 0:
    #     print(f'{i} ')s
    # elif items == 1:
        # print('*')