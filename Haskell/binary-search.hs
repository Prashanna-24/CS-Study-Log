-- binarySearch ([], target, low, high) -> result
binarySearch :: (Ord a) => [a] -> a -> Int -> Int -> Int
binarySearch arr target low high
  | low<=high =
    let mid = (low+high)`div`2
        midval = arr!!mid

    in if midval==target
         then mid
       else if midval<target
         then binarySearch arr target (mid+1) high
       else binarySearch arr target low (mid-1)

  | otherwise = -1
    

main = do
  print(binarySearch [1,2,3,4,5] 3 0 4)
