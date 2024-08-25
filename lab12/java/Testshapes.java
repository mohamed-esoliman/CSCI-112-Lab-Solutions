
/**
  * A simple class for sorting shapes by area
  *
  * Copyright (c) 2021 Simon D. Levy
  */

import java.util.Arrays;

class Testshapes {

    public static void main(String[] args) {

        Square s1 = new Square(10, 10, 5);
        Square s2 = new Square(30, 40, 7);
        Triangle t1 = new Triangle(10, 15, 10, 3);
        Triangle t2 = new Triangle(0, 5, 5, 4);

        Shape[] array = { t1, t2, s1, s2 };

        Arrays.sort(array);

        System.out.println("Sorted by area:");
        for (Shape s : array) {
            System.out.println(s);
        }

        System.out.println("\nMoving a square:");
        System.out.print("Before move: " + s1 + "\n");
        s1.move(20, 30);
        System.out.print("After move:  " + s1 + "\n");
    }
}
