/*input format:

First line : An integer N
Next N lines: Each line contains a point (xi,yi)

output format:
Print the N points in the same order illustrated in the question. The format of the 
output must be , "Xi Yi " without quotes. Each point must be printed in a new line

sample input:
5
2 5
3 6
1 2
3 5
5 1

sample output:
1 2
2 5
3 6
3 5
5 1
*/

# code:
def sort_data(a):
  a.sort(key = lambda x: (x[0],-x[1]) )
  return a
a = list()
for _ in range(int(input())):
  a.append(list(map(int,input().split())))

sort_list = sort_data(a)
print(sort_list)
