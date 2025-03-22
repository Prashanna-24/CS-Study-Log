def karatsuba(x, y):
   # Base case for recursion
   if x < 10 or y < 10:
      return x * y
   else:
      # Calculate the number of digits in the largest number
      n = max(len(str(x)), len(str(y)))
      half = n // 2

      # Split x and y into two halves
      a = x // (10 ** half)   # Left part of x
      b = x % (10 ** half)    # Right part of x
      c = y // (10 ** half)   # Left part of y
      d = y % (10 ** half)    # Right part of y

      # Recursive calls
      ac = karatsuba(a, c)   # Multiply left halves
      bd = karatsuba(b, d)   # Multiply right halves
      ad_plus_bc = karatsuba(a + b, c + d) - ac - bd

      # Return the final result
      return ac * (10 ** (2 * half)) + (ad_plus_bc * (10 ** half)) + bd

print(karatsuba(146123, 352120))