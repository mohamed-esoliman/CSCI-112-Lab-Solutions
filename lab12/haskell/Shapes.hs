module Shapes where

import Text.Printf (printf)

data Shape
  = Square {x :: Double, y :: Double, l :: Double}
  | Triangle {x :: Double, y :: Double, w :: Double, h :: Double}
  deriving (Show)

area :: Shape -> Double
area (Square _ _ l) = l * l
area (Triangle _ _ w h) = (w * h) / 2

move :: Shape -> Double -> Double -> Shape
move (Square x y l) dx dy = Square (x + dx) (y + dy) l
move (Triangle x y w h) dx dy = Triangle (x + dx) (y + dy) w h

str :: Shape -> String
str (Square x y l) = printf "Square (center at (%f, %f) and side length %f)" x y l
str (Triangle x y w h) = printf "Triangle (center at (%f, %f) and width %f & height %f." x y w h

instance Eq Shape where
  (==) :: Shape -> Shape -> Bool
  s1 == s2 = area s1 == area s2

instance Ord Shape where
  compare :: Shape -> Shape -> Ordering
  compare s1 s2
    | area s1 < area s2 = LT
    | area s1 > area s2 = GT
    | otherwise = EQ
