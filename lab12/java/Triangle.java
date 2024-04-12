public class Triangle extends Shape {
    private double width;
    private double height;

    public Triangle(double x, double y, double width, double height) {
        super(x, y);
        this.width = width;
        this.height = height;
    }

    public double area() {
        return this.width * this.height * 0.5;
    }

    public String toString() {
        return "Triangle (center at (%.2f, %.2f) and width %.2f & height %.2f)".formatted(x, y, width, height);
    }

}