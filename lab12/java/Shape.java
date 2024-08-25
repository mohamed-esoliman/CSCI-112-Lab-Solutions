public abstract class Shape implements Moveable, Comparable<Shape> {
    // coordinates of the shape
    public double x;
    public double y;

    // constructor
    public Shape(double x, double y) {
        this.x = x;
        this.y = y;
    }

    // move the shape by dx and dy
    public void move(double dx, double dy) {
        this.x += dx;
        this.y += dy;
    }

    public abstract double area();

    public int compareTo(Shape other) {
        if (this.area() < other.area()) {
            return -1;
        } else if (this.area() > other.area()) {
            return 1;
        } else {
            return 0;
        }
    }
}
