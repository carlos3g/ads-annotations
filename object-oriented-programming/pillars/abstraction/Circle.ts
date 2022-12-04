import { Shape } from './Shape';

export class Circle extends Shape {
  public radius: number;

  public constructor(color: string, radius: number) {
    super();

    this.color = color;
    this.radius = radius;
  }

  public calculateArea(): number {
    return Math.PI * this.radius ** 2;
  }

  public calculatePerimeter(): number {
    return 2 * Math.PI * this.radius;
  }
}
