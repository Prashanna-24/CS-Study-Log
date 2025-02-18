{-
quickSort :: Ord a => [a] -> [a]
quickSort [] = []  -- Base case: an empty list is already sorted
quickSort (x:xs) = quickSort smaller ++ [x] ++ quickSort larger
  where
    smaller = filter (< x) xs  -- Elements smaller than the pivot (x)
    larger  = filter (>= x) xs  -- Elements greater than or equal to the pivot (x)

-------------------------

-- SORT LIST OF SUBLISTS W.R.T TO THE LENGTH OF SUBLLISTS
sortList :: Ord a => [[a]] -> [[a]]
sortList [] = []
sortList (x:xs) =
  let smaller = [a | a<-xs, length a < length x]
      larger = [a | a<-xs, length a >= length x]
  in sortList smaller ++ [x] ++ sortList larger

main = do
  print(sortList [ [1,2,3], [1,3], [55,33,42,13,4], [4,5] ])

-------------------------
-}

mergeSort :: (Ord a) => [a] -> [a]
mergeSort []  = []
mergeSort [x] = [x]
mergeSort xs  = merge (mergeSort left) (mergeSort right)
  where
    (left, right) = splitAt (length xs `div` 2) xs

merge :: (Ord a) => [a] -> [a] -> [a]
merge [] ys = ys
merge xs [] = xs
merge (x:xs) (y:ys)
    | x <= y    = x : merge xs (y:ys)
    | otherwise = y : merge (x:xs) ys

main :: IO ()
main = print (mergeSort [3,1,4,1,5,9,2,6,5,3,5])
