{-
increment, decrement
maximum, minimum
toUpper, toLower
head, tail
init, last
take, drop
elem
null
compare 2 3 == LT
replicate 3 [5]
splitAt 3 "apple"
intersperse '|' "abcd"  --> "a|b|c|d"
intercalate " " ["ajithey", "kadavuley"]   --> "ajithey kaduvuley"
words  "ajithey kadavuley"   --> ["ajithey", "kadavuley"]   |||||  lines  "ajithey\nkadavuley"   --> ["ajithey", "kadavuley"]
-}




main = do
   putStr "Enter a number:"
   x <- getLine
   let num = read x :: Int
   
   putStr "Enter a choice:"
   x <- getLine
   let n = read x :: Int

   if n == 1
      then print (num * num)  