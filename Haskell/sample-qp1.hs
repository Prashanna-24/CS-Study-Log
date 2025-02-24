{-
map_list :: (Int -> a) -> Int -> Int -> Int -> [a]
map_list f a b c
  | a<=b = (f a) : map_list f (a+c) b c
  | otherwise = []

square :: Int -> Int
square x = x * x

main = do
  print(map_list square 1 10 2)

------------------
-}
