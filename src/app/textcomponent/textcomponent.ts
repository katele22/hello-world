import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Records } from '../records';
@Component({
  selector: 'app-textcomponent',
  imports: [CommonModule],
  templateUrl: './textcomponent.html',
  styleUrls: ['./textcomponent.css']
})
export class Textcomponent implements OnInit {
  infoRecord1: string[] = [];
  infoRecord2: string[] = [];
getInfo1FromServiceClass(): void {
    this.infoRecord1 = this.rservice.getInfo1();
  }
  getInfo2FromServiceClass(): void {
    this.infoRecord2 = this.rservice.getInfo2();
  }

  constructor(private rservice: Records) { 
  }

  ngOnInit(): void {
    // Initialization logic here
  }
}
