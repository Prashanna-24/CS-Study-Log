-- Stack type as a synonym for a list
type Stack a = [a]

push :: a -> Stack a -> Stack a
push x stack = x : stack

-- returns the new stack and the popped element
pop :: Stack a -> (Maybe a, Stack a)
pop []     = (Nothing, [])  -- Handle empty stack
pop (x:xs) = (Just x, xs)

-- Peek at the top element of the stack without removing it
peek :: Stack a -> Maybe a
peek []    = Nothing  -- Handle empty stack
peek (x:_) = Just x   -- also peek (x:xs) = Just x

-- Check if the stack is empty
isEmpty :: Stack a -> Bool
isEmpty [] = True
isEmpty _  = False


main :: IO ()
main = do
  let stack = [] :: Stack Int  -- Start with an empty stack
  let stack1 = push 10 stack   -- Push 10
  -- let stack2 = push 20 stack1  -- Push 20
  let (top, stack3) = pop stack1 -- Pop the top element
  let (top, stack3) = pop stack1 -- Pop the top element
  print stack3                -- Print the remaining stack
  print top                   -- Print the popped element
  print (peek stack3)         -- Peek at the top of the stack
  print (isEmpty stack3)      -- Check if the stack is empty
