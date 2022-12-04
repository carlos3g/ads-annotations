import { MammalInterface } from './MammalInteface';

export class Dog implements MammalInterface {
  public height: number;
  public weight: number;

  public constructor(height: number, weight: number) {
    this.height = height;
    this.weight = weight;
  }

  public eat(): void {
    // Eating...
  }

  public drink(): void {
    // Drinking...
  }

  public walk(): void {
    // Walking...
  }

  public bark(): void {
    // Barking...
  }
}
