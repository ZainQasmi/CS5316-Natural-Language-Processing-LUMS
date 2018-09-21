import sys

def min_edit(source, target):

    print (source, target)
    coloumns = len(target)+1
    rows = len(source)+1
    mat = [ [0] * coloumns for _ in range(rows)] #init matrix of zeros

    for i in range(1, coloumns):
        mat[0][i] = i # first row initialized to 1-m which is the length of subtring of source
    for j in range(1, rows):
        mat[j][0] = j # first coloumn initialized to 1-n which is the length of subtring of target

    insertCost = 1
    delCost = 1
    for col in range(1, coloumns):
        for row in range(1, rows):
            if source[row-1] != target[col-1]:
                subCost = 1	# cost of substitution
            else:
                subCost = 0	# cost zero if substituted with same letter i.e. s == s

            mat[row][col] = min(mat[row][col-1] + insertCost,     	#insertion
            					mat[row-1][col] + delCost,			#deletion     
                                mat[row-1][col-1] + subCost)		#substitution
    print(mat) 
    return mat[row][col]	#last row,col is the distance. Terminating condition in case of recursive algorithm



def main():
	# print sys.argv
	print '#### Sample Test ####'
	print min_edit('intention', 'execution')
	print
	print '#### Test on User Input ####'
	print min_edit(sys.argv[1],sys.argv[2])

if __name__ == "__main__":
    main()