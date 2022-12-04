import { MammalInterface } from './MammalInteface';

export class Person implements MammalInterface {
  public name: string;
  public height: number;
  public weight: number;

  public constructor(name: string, height: number, weight: number) {
    this.name = name;
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

  public speak(): void {
    // Speaking...
  }
}
