
def localSum(array):
    sum = [[] for i in range(6)]
    #print sum
    for i in range(6):
        sum[i] = [0 for x in range(6)]

    for i in range(1, 6):
        for j in range(1, 6):
            sum[i][j] = sum[i][j - 1] + sum[i - 1][j] - sum[i - 1][j - 1] + array[i - 1][j - 1]
        
    return sum

def getMax1(sum):
    for i in range(1, 6):
        print sum[i][1 : 6]
    max = 0
    res_i_min = 0
    res_i_max = 0
    res_j_min = 0
    res_j_max = 0
    for i_min in range(1, 6):
        for i_max in range(i_min, 6):
            for j_min in range(1, 6):
                for j_max in range(j_min, 6):
                    tempSum = sum[i_max][j_max] - sum[i_min - 1][j_max] - sum[i_max ][j_min - 1] + sum[i_min - 1][j_min - 1]
                    if tempSum > max:
                        max = tempSum
                        res_i_min = i_min
                        res_i_max = i_max
                        res_j_min = j_min
                        res_j_max = j_max
    print max
    print res_i_min, res_i_max
    print res_j_min, res_j_max
    
def columnSum(array):
    sum = [[] for i in range(6)]
    for i in range(6):
        sum[i] = [0 for x in range(6)]
    for i in range(1, 6):
        for j in range(1, 6):
            sum[i][j] = sum[i - 1][j] + array[i - 1][j - 1]
    return sum

def getMax2(columnSum):
    max = 0
    sum = 0
    for i_min in range(1, 6):
       for i_max in range(i_min, 6):
           sum = 0
           for j in range(1, 6):
               sum += columnSum[i_max][j] - columnSum[i_min - 1][j]
               if sum < 0:
                   sum = 0
               else:
                   if sum > max:
                        max = sum
    print max
def main():
    array = [[1, 2, 3, -5, 4],
            [2,-4,-4,3,4],
            [1,3,2,4,5],
            [-4, -5, -12, 5, 6],
            [-1, 3, 4, 5, 2]
         ]
    sum = localSum(array)
    getMax1(sum)
    
    sum2 = columnSum(array)
    getMax2(sum2)

        
if __name__ =='__main__':
    main()

