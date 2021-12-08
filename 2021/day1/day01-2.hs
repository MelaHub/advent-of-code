import System.IO

main = do
  handle <- openFile "input.txt" ReadMode
  strContents <- hGetContents handle
  let intContents = makeIntegers (getNumbers strContents)
  let triplet = zip (zip intContents (tail intContents)) (tail (tail intContents))
  let windows = map sumTriplet triplet
  let s = sum (map doesItIncrease (zip windows (tail windows)))
  print s
  hClose handle
 
getNumbers :: String -> [String]
getNumbers str =  words str
makeIntegers :: [String] -> [Int]
makeIntegers = map read
doesItIncrease :: (Int, Int) -> Int
doesItIncrease (a, b) = if a < b then 1 else 0
sumTriplet :: ((Int, Int), Int) -> Int
sumTriplet ((a, b), c) = a + b + c

