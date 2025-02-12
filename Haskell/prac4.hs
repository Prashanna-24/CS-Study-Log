
-- Write a program in Haskell using “Guards, Pattern matching” and taking natural number from the user and generates a sequence where: If the current term is divisible by 3, the next term is the square root of the current term (integer part only). If the current term is not divisible by 3, the next term is the current term multiplied by 2. The sequence stops when the term becomes less than or equal to 1.(transformationSequence 18) returns Output: [18, 4, 8, 16, 32] (stops when the term is ≤ 1).

{-
createSequence :: Int -> [Int]
createSequence n
  | n<=1 = []
  | n`mod`3==0 = n : createSequence (floor(sqrt(fromIntegral n)))
  | otherwise = n : createSequence (n*2)

main = do
  let result_list = createSequence 18
  print(result_list)






longestPalindromicSubstring :: String -> Int
longestPalindromicSubstring [] = 0
longestPalindromicSubstring [_] = 1
longestPalindromicSubstring str = longestHelper str 0
  where
    longestHelper [] longest = longest
    longestHelper (x:xs) longest =
      if null xs
        then longestHelper [] longest  
        else let lastChar = last xs
                 t = longestPalindromicSubstring (init xs)
             in if x == lastChar
                then longestHelper xs (max longest (t + 2))
                else longestHelper xs longest
-}

longestPalindromicSubstring :: String -> Int
longestPalindromicSubstring [] = 0
longestPalindromicSubstring [x] = 1
longestPalindromicSubstring str
  | str == reverse str = length str
  | otherwise = max (longestPalindromicSubstring (init str)) (longestPalindromicSubstring (tail str))

main = do
    print(longestPalindromicSubstring "abacdadc")