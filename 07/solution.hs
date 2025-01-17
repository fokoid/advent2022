import System.IO

data Node = File { name :: String, size :: Int } | Dir { name :: String, contents :: [Node]} deriving (Show)

-- size :: Node -> Int
-- size (File f) = f.size
-- size (Dir xs) = sum (map size xs)

parse :: [String] -> Node
parse ("$ cd /":xs) = Dir { name = "/", contents = [] }



main = do
  inh <- openFile "input.txt" ReadMode
  inpStr <- hGetContents inh
  let dt = lines inpStr
  let root = parse dt
  return root
