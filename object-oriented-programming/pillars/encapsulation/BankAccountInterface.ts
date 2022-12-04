import { BankAccount } from './BankAccount';

export interface BankAccountInterface {
  ownerName: string;
  ownerId: number;
  balance: number;
  deposit: (value: number) => void;
  withdraw: (value: number) => void;
  transfer: (accountDestination: BankAccount, value: number) => void;
}
