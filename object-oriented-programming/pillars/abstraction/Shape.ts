export abstract class Shape {
  public color: string = 'white';

  public abstract calculateArea(): number;

  public abstract calculatePerimeter(): number;
}
