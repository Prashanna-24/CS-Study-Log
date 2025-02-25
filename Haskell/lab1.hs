import Data.List
import Data.Char
import System.IO

-- Ques 1
longest_from_current :: [Int] -> [Int]
longest_from_current [] = []
longest_from_current [x] = [x]
longest_from_current (x:y:xs) 
    | y == x+1 = x : longest_from_current (y:xs)
    | otherwise = [x]


startPoint :: [Int] -> [Int]
startPoint [] = []
startPoint (x:xs)
    | length(longest_from_current (x:xs))  > length(startPoint xs) = longest_from_current (x:xs)
    | otherwise = startPoint xs

instant x = startPoint(remove_duplicates (quicksort x))

remove_duplicates :: [Int] -> [Int]
remove_duplicates x_list = [x | x <- nub x_list]


quicksort :: [Int] -> [Int]
quicksort [] = []
quicksort (x:xs) = quicksort [y | y <- xs, y < x] ++ [x] ++ quicksort[y | y <- xs , y >= x]


-- Ques 2

mid_ele ::[Int] -> Int -> Int
mid_ele [] _ = -1
mid_ele (x:xs) 0 = x
mid_ele (x:xs) y = mid_ele xs (y-1)


triplet :: [Int] -> (Int,Int,Int)
triplet [] = (0,0,0)
triplet x = (head x , mid_ele x ((length x) `div` 2), last x)

mi_values :: [Int] -> Int
mi_values x = ((length x) `div` 2)


-- Ques 3

generate :: Int -> Int -> [Int]
generate x y 
    | x > y = []
    | mod x 2 == 0 = x : generate (x*x) y 
    | otherwise = x : generate (x*x*x) y


-- Ques 4

generate2 :: Int -> Int -> [Int]
generate2 x y
    | x > y = []
    | x <= 1 = []
    | mod x 3 == 0 = x : generate2 (floor(sqrt(fromIntegral x))) y
    | otherwise = x : generate2 (x*x) y


-- Ques 5

init_segment :: [Int] -> [Int] -> [[Int]]
init_segment [] xs = [xs]
init_segment (x:xs) y = [y] ++ init_segment xs (y ++ [x])


-- Ques 6

class_avg :: [Int] -> Int -> Int
class_avg xs n = div (sum xs) n

main = do
    putStr "Enter Number of students: "
    ll<- getLine
    let l = map read (words ll) :: [Int]
    print(class_avg l (length l))
    

-- Ques 7

count_occur :: [Int] -> Int -> Int
count_occur [] _ = 0
count_occur (x:xs) y
    | x == y = 1 + count_occur xs y
    | otherwise = count_occur xs y

odd_occur_recursive :: [Int] -> [Int] -> [Int]
odd_occur_recursive [] _ = []
odd_occur_recursive (x:xs) y
    | odd (count_occur y x) = x : odd_occur_recursive (filter (/= x) y) y
    | otherwise = odd_occur_recursive xs y

-- Ques 8
-- nub is a function from the Data.List module that removes duplicate elements from a list

find_duplicates :: [Int] -> [Int]
find_duplicates x_list = [x | x <- nub x_list , length(filter(==x) x_list) > 1]

-- Ques 9
-- sum of even numbers in a list

sum_even :: [Int] -> Int
sum_even x_list = sum[x | x <- x_list , even x]

-- Ques 10
-- sum of odd index numbers in a list

sum_odd_index :: [Int] -> Int
sum_odd_index [] = 0
sum_odd_index (x:xs:xss) = x + sum_odd_index(xss)

-- Ques 11
-- find number in the list and display an appropriate message

find_number :: [Int] -> Int -> IO ()

find_number num target = do
    let element_found = length (filter(==target) num)
    if element_found /= 0 
        then putStrLn ("Element " ++ show target ++ " found in the list")
        else putStrLn "Element not found in the list"

-- Ques 12
-- sort list of strings based on length
-- remember the ++ [x] ++ part

sort_by_length :: [String] -> [String]
sort_by_length [] = []
sort_by_length (x:xs) = [y | y <- xs , (length y) < (length x)] ++ [x] ++ [y | y <- xs , (length y) >= (length x)]


-- Ques 13


classifyNumbers :: [Int] ->[String]
classifyNumbers [] = []
classifyNumbers (x:xs)
    | mod x 15 == 0 = ["FizzBuzz"] ++ classifyNumbers xs
    | mod x 3 == 0 = ["Fizz"] ++ classifyNumbers xs
    | mod x 5 == 0 = ["Buzz"] ++ classifyNumbers xs
    | otherwise = ["Other"] ++ classifyNumbers xs

-- Ques 14

-- Function to encode a single character using Caesar cipher
caesarShift :: Char -> Char
caesarShift c
    | c >= 'a' && c <= 'z' = chr ((ord c - ord 'a' + 3) `mod` 26 + ord 'a')  -- For lowercase letters
    | c >= 'A' && c <= 'Z' = chr ((ord c - ord 'A' + 3) `mod` 26 + ord 'A')  -- For uppercase letters
    | otherwise = c 

-- Function to encode a string
caesarCipher :: String -> String
caesarCipher x = map caesarShift x


-- Ques 15

check_perfect :: Int -> Bool
check_perfect x = sum [y | y <- [1..x-1] , ((mod x y) == 0)] == x


perfects :: Int -> [Int]
perfects x = [y | y <- [1..x] , (check_perfect y)]

-- Ques 16

scalar_product :: [Int] -> [Int] -> Int
scalar_product [] [] = 0
scalar_product (x:xs) (y:ys) = x*y + scalar_product xs ys


-- Ques 17
-- pangram is a string that contain all alphabets in english language

convert_to_lower :: String -> String
convert_to_lower x = map toLower x

check_pangram :: String -> Bool
check_pangram x = all (`elem` convert_to_lower x) ['a'..'z']

-- Ques 18

apply_list_of_functions :: [Int -> Int] -> Int -> [Int]
apply_list_of_functions [] _ = []
apply_list_of_functions (f:fs) x = f x : apply_list_of_functions fs x

-- Ques 19

list_access :: [Int] -> Int -> Int
list_access [] n = error "incorrect index"
list_access (x:_) 0 = x
list_access (x:xs) n = list_access xs (n-1)

-- Ques 20

triangular_sequence :: Int -> [Int]
triangular_sequence 0 = []
triangular_sequence n = triangular_sequence (n-1) ++ [sum[1..n]]

-- Ques 21

find_max :: [Int] -> Int
find_max [] = -1
find_max [x] = x
find_max (x:xs) = max x (find_max xs)

cummulative_maximum :: [Int] -> [Int]
cummulative_maximum [] = []
cummulative_maximum (x:xs) = helper x (x:xs)
    where
        helper _ [] = []
        helper current_max (x:xs) = (max current_max x) : helper (max current_max x) xs


