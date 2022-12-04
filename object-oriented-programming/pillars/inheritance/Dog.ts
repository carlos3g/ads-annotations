import { Animal } from './Animal';

export class Dog extends Animal {
  public ownerName: string;
  public name: string;

  public constructor(ownerName: string, name: string) {
    super('Canis familiaris');

    this.ownerName = ownerName;
    this.name = name;
  }

  public walk(): void {
    // Walking...
  }

  public bark(): void {
    // Barking...
  }
}
