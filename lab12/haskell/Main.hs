{--
  Test code for Haskell shapes library

  Copyright (c) 2021 Simon D. Levy
--}

module Main where

import Shapes
import Text.Printf (printf)

main :: IO ()
main = do
  let s1 = Square 30 20 5

  printf "%s has area %f\n" (str s1) (area s1)

  let dx = 10
  let dy = 15

  let s1' = move s1 dx dy

  printf "if we move it by (%f, %f) it is now at (%f, %f)\n" dx dy (x s1') (y s1')

  let t1 = Triangle 100 450 100 200

  printf "\n%s has area %f\n" (str t1) (area t1)

  let t1' = move t1 dx dy

  printf "if we move it by (%f, %f) it is now at (%f, %f)\n" dx dy (x t1') (y t1')

  let s2 = Square 30 20 10
  printf "\ncomparing %s to %s,\n" (str s1) (str s2)
  printf "we see that the %s one is bigger\n" (if s1 > s2 then "first" else "second")
