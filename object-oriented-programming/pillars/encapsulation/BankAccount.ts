import { BankAccountInterface } from './BankAccountInterface';

export class BankAccount implements BankAccountInterface {
  private _balance: number = 0.0;
  private _ownerName: string;
  private _ownerId: number;

  public constructor(ownerName: string, ownerId: number) {
    this._ownerName = ownerName;
    this._ownerId = ownerId;
  }

  public get ownerName() {
    return this._ownerName;
  }

  public get ownerId() {
    return this._ownerId;
  }

  public get balance() {
    return this._balance;
  }

  public deposit(value: number): void {
    if (!this.isDepositValid(value)) {
      throw new Error('Deposit amount invalid!');
    }

    this._balance += value;
  }

  public withdraw(value: number): void {
    if (!this.isWihdrawValid(value)) {
      throw new Error('Withdraw amount invalid!');
    }

    this._balance -= value;
  }

  // Doing this since I don't have DB implementation. It's just a example
  public transfer(accountDestination: BankAccount, value: number): void {
    if (!this.isDepositValid || !this.isWihdrawValid) {
      throw new Error('Transference amount invalid!');
    }

    accountDestination.deposit(value);
    this.withdraw(value);
  }

  private isDepositValid(value: number): boolean {
    return value > 0;
  }

  private isWihdrawValid(value: number): boolean {
    return value > 0 && value < this._balance;
  }
}
