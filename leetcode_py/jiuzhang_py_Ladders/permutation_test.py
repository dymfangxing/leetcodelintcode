#python for loop still need to learn more abt how to write it simply
#array + array = array

def permute(list, s):
    print("list is: %i" % list)
    print("s is: %s" % s)
    if list == 1:
        return s
    else:
    	'''
        return [ y + x
                 for y in permute(1, s)
                 for x in permute(list - 1, s)
                 ]
        '''
        temp = []
        for y in permute(1, s):
        	for x in permute(list - 1, s):
        		#z = y+x
        		#temp.append(z)
        		temp += [y+x]

        return temp

#print(permute(1, ["a","b","c"]))
print(permute(2, ["a","b","c"]))
