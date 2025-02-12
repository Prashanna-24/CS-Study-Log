{-
-- PATTERN MATCHING
func1 :: Int -> String
func1 1 = "one"
func1 2 = "two"
func1 3 = "three"
func1 x = "others" -- can also use _

main = do
  putStrLn (func1 6)
---------------------

-- WHERE
populationDensity :: (Float, Float) -> Float
populationDensity (population, area)= density where density = population/area

main = do
  print (populationDensity(45, 89.4)) 
------------------
-- FACTORIAL USING RECURSION

factorial :: Int -> Int
factorial 0 = 1
factorial n = n * factorial (n-1)

main = do
  print (factorial 5)
------------------
-- FACTORIAL USING FOLD and GUARDS

factorial :: Int -> Int
factorial n
  | n<0 = error "-ve not possible"
  | otherwise = foldl (*) 1 [1..n]

main = do
  print (factorial 5)
-----------------
-- MAP & FILTER

isEven :: Int -> Bool
isEven x = mod x 2 == 0

main = do
  let originalList = [1, 2, 4]
  let map_result = map isEven originalList -- Applying to each element
  let filter_result = filter isEven originalList
  print map_result
  print filter_result      
------------------
-- OTHER HIGHER FUNCTIONS

isEven :: Int -> Bool
isEven x = mod x 2 == 0

main :: IO ()
main = do
  let list1 = [1, 3, 2, 4, 5, 6]
  let list2 = [10, 20, 30, 40, 50, 60]

  -- Using zipWith to sum corresponding elements of two lists
  let zipWithResult = zipWith (+) list1 list2

  -- Using takeWhile to take elements from the list while they are ...
  let takeWhileResult = takeWhile (<=3) list1

  -- Using dropWhile to drop elements from the list while they are ...
  let dropWhileResult = dropWhile (<2) list1

  -- Using all to check if all elements in the list are even
  let allResult = all isEven list2

  -- Using any to check if any element in the list is even
  let anyResult = any isEven list1

  -- Printing results
  print ("zipWith (+):", zipWithResult)
  print ("takeWhile odd:", takeWhileResult)
  print ("dropWhile odd:", dropWhileResult)
  print ("all isEven (list2):", allResult)
  print ("any isEven (list1):", anyResult)
------------------
-- APPENDING AN ELEMENT TO LIST

main = do
  let list1 = [i | i <- [1..10]]
  print(list1)
  let n1 = 11
  let list1 = list1 ++ [11]
  print(list1)
----------------------
-- FINDING MAX

findMax :: (Ord a) => [a] -> a
findMax [x] = x
findMax (x:xs) = max x (findMax xs)

main = do
  print(findMax [1,25,2,5])
------------------------
-- REMOVING ADJ DUPLICATES

removeAdjacentDuplicates :: Eq a => [a] -> [a]
removeAdjacentDuplicates [] = []  -- Base case: empty list
removeAdjacentDuplicates [x] = [x]  -- Base case: single-element list
removeAdjacentDuplicates (x:y:xs)
  | x == y    = removeAdjacentDuplicates (y:xs)  -- Skip duplicate
  | otherwise = x : removeAdjacentDuplicates (y:xs)  -- Keep the element

main = do
  let list1 = [1, 1, 2, 3, 3, 3, 4, 4, 5]
  print (removeAdjacentDuplicates list1)  -- Output: [1, 2, 3, 4, 5]
  let list2 = "aabbccdd"
  print (removeAdjacentDuplicates list2)  -- Output: "abcd"
--------------------------
-- REMOVE ELEMENT FROM LIST

removeFromList :: Eq a => a -> [a] -> [a]
removeFromList _ [] = []
removeFromList y (x:xs)
  | y == x = removeFromList y xs  -- SKIP THE MATCHING ELEMENT
  | otherwise = x : removeFromList y xs

main = do
  print(removeFromList 2 [1,2,3,4])
--------------------------------
-- PALINDROME

checkPalindrome :: String -> Bool
checkPalindrome x = x == reverse x

main = do
  let result_pal = checkPalindrome "abcb"
  print(result_pal)

--------------------------------

-- FUNCTIONAL COMPOSITION
multByTwo :: Int -> Int
addByOne :: Int -> IO()

multByTwo x = x*2
addByOne x = print(x+1)

main = do
  (addByOne.multByTwo) 3   --(addByOne(multByTwo 3 ))
--------------------------------

safeDivide :: Double -> Double -> Maybe Double
safeDivide _ 0 = Nothing
safeDivide x y = Just (x / y)

main = do
  let a = 10
  let b = 2
  let result = 
             safeDivide a b
  print result  -- Output: Just 5.0         
    
-}
