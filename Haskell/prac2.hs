-- print = putStrLn + show(anytype to string)
-- lists in haskell cant store multi datatype
{-
main :: IO ()
main = do
    putStrLn "Enter a number: "
    input <- getLine
    let n1 = read input :: Double   -- converting input from string(default) to Double
    putStrLn ("Your number: " ++ show n1)
-- ----------------

-- check odd or even
oddEven :: Int -> String
oddEven x = 
    if x `mod` 2 == 0
    then "Even"
    else "Odd"
main = do
    putStrLn (oddEven 34)  -- Output: "Odd"
-- -----------------

-- calculator
add :: (Int, Int) -> Int
add (x, y) = x + y

sub :: (Int, Int) -> Int
sub (x, y) = x - y

main = do
    putStrLn "Enter the first number:"
    input1 <- getLine
    let n1 = read input1 :: Int
    
    putStrLn "Enter the second number:"
    input2 <- getLine
    let n2 = read input2 :: Int
    
    putStrLn "Enter your choice (1 for addition, 2 for subtraction):"
    input3 <- getLine
    let choice = input3

    let ans = 
            if choice == "1" 
                then add (n1, n2)
            else if choice == "2"
                then sub (n1, n2)
            else error "Invalid"
    putStrLn ("The result is: " ++ show ans)
--------------------

-- Without let (Global scope)
doubling x = x*2
incrementing x = x+1
doingBoth x = incrementing(doubling x)
main = do
  putStrLn (show (doingBoth 10))
-- with let (local scope)
main = do
  let doubling x = x * 2
  let incrementing x = x + 1
  let doingBoth x = incrementing (doubling x)
  putStrLn (show (doingBoth 10))
  -------------------------

import Data.List
main = do
    let numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    let sortedNumbers = reverse (sort numbers)
    print sortedNumbers

-}