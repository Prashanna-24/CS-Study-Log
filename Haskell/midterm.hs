{-
import Control.Monad (replicateM)

isUpperTriangular :: [[Int]] -> Bool
isUpperTriangular matrix = and [matrix !! i !! j == 0 | i <- [1..n-1], j <- [0..i-1]]
  where n = length matrix

isLowerTriangular :: [[Int]] -> Bool
isLowerTriangular matrix = and [matrix !! i !! j == 0 | i <- [0..n-2], j <- [i+1..n-1]]
  where n = length matrix

main :: IO ()
main = do
    putStrLn "Enter size of matrix:"
    nStr <- getLine
    let n = read nStr :: Int

    putStrLn "Enter the matrix values row by row (space-separated):"
    matrix <- replicateM n $ do
        rowStr <- getLine
        let row = map read (words rowStr)
        if length row /= n
            then fail "Each row must have exactly n elements!"
            else return row

    putStrLn "\nThe entered matrix is:"
    mapM_ print matrix

    let upper = isUpperTriangular matrix
        lower = isLowerTriangular matrix

    case (upper, lower) of
        (True, True)   -> putStrLn "Diagonal"
        (True, False)  -> putStrLn "Upper"
        (False, True)  -> putStrLn "Lower"
        (False, False) -> putStrLn "None"

-------------------------
-}

import Data.List (elemIndex)   -- maybe return

splitAtElem :: Eq a => a -> [a] -> ([a], [a])
splitAtElem _ [] = ([],[])
splitAtElem n xs = case (elemIndex n xs) of
  Nothing -> (xs, [])
  Just idx -> splitAt (idx+1) xs



  cumulativeDiff :: [Double] -> Double
cumulativeDiff temps = sum [ abs (x - y) | (x, y) <- zip temps (tail temps) ]
