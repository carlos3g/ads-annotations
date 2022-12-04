export interface MammalInterface {
  height: number;
  weight: number;

  walk: () => void;
  eat: () => void;
  drink: () => void;
}
