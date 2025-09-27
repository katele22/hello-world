import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Textcomponent } from './textcomponent';

describe('Textcomponent', () => {
  let component: Textcomponent;
  let fixture: ComponentFixture<Textcomponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [Textcomponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(Textcomponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
