def merge(s1, s2, s):
   i, j = 0, 0
   while i + j < len(s):
      if j == len(s2) or (i < len(s1) and s1[i] < s2[j]):
         s[i + j] = s1[i]
         i += 1
      else:
         s[i + j] = s2[j]
         j += 1

def mergesort(s):
   n = len(s)
   if n < 2:
      return
   mid = n // 2
   s1 = s[:mid]
   s2 = s[mid:]
   mergesort(s1)
   mergesort(s2)
   merge(s1, s2, s)

li = [2, 56, 121, 5, 1]
mergesort(li)
print(li)  # Output: [1, 2, 5, 56, 121]