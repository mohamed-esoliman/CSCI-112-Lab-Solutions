public class Square extends Shape {
    private double side;

    public Square(double x, double y, double side) {
        super(x, y);
        this.side = side;
    }

    public double area() {
        return side * side;
    }

    public String toString() {
        return "Square (center at (%.2f, %.2f) and side length %.2f)".formatted(x, y, side);
    }

}