import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class Records {
  info1: string[] = ["apple", "banana", "cherry"];
  info2: string[] = ["dog", "elephant", "frog"]
  getInfo1(): string[] {
    return this.info1;
  }
  getInfo2(): string[] {
    return this.info2;
  }   

  constructor() { }
}
