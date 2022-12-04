import { Shape } from './Shape';

export class Square extends Shape {
  public side: number;

  public constructor(color: string, side: number) {
    super();

    this.color = color;
    this.side = side;
  }

  public calculateArea(): number {
    return this.side ** 2;
  }

  public calculatePerimeter(): number {
    return this.side * 4;
  }
}
