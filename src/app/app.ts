import { Component, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { Textcomponent } from './textcomponent/textcomponent';
import {Imagecomponent} from './imagecomponent/imagecomponent';
@Component({
  selector: 'app-root',

  imports: [RouterOutlet, Textcomponent , Imagecomponent],
  

  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  protected readonly title = signal('hello-world');
}
