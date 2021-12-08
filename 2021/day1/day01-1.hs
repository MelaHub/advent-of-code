import qualified Data.Text    as Text
import qualified Data.Text.IO as Text
import System.IO

main = do
  handle <- openFile "input.txt" ReadMode
  strContents <- hGetContents handle
  let intContents = makeIntegers (getNumbers strContents)
  let pair = zip intContents (tail intContents)
  let s = sum (map doesItIncrease pair)
  print s
  hClose handle
 
getNumbers :: String -> [String]
getNumbers str =  words str
makeIntegers :: [String] -> [Int]
makeIntegers = map read
doesItIncrease :: (Int, Int) -> Int
doesItIncrease (a, b) = if a < b then 1 else 0
