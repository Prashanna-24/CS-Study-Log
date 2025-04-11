{-
--1

import Data.List (nub)
import Data.Char (isAlpha, toLower)

pangram :: String -> Bool
-- pangram s = length cleaned == 26
--   where cleaned = nub [toLower c | c <- s, isAlpha c]

pangram s = all (`elem` lowerS) ['a'..'z']
  where lowerS = map toLower s

main = do
  print(pangram "The quick brown fox jumps over a lazy dog.")

------------------
--2

perfectNo :: Int -> Bool
perfectNo n = sum divisors == n
  where divisors = [x | x <- [1..n-1], n `mod` x == 0] 

main = do
  print(perfectNo 6)

----------------------
-}

--3

applylistfun :: [a -> a] -> a -> [a]
applylistfun fs x = [f x | f <- fs]

main = do
  print(applylistfun [(+10), (*3),  (\x -> x - 5)] 2)
