import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

// Angular Material
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatButtonModule } from '@angular/material/button';
import { MatCardModule } from '@angular/material/card';
import { MatDividerModule } from '@angular/material/divider';
import { MatToolbarModule } from '@angular/material/toolbar';

import { AppComponent } from './app.component';
import { ChatComponent } from './chat/chat.component';
import { OpenAiChatComponent } from './open-ai-chat/open-ai-chat.component';
import { OllamaAiChatComponent } from './ollama-ai-chat/ollama-ai-chat.component';

@NgModule({
  declarations: [AppComponent, ChatComponent, OpenAiChatComponent, OllamaAiChatComponent],
  imports: [
    BrowserModule,
    ReactiveFormsModule,
    HttpClientModule,
    BrowserAnimationsModule,
    MatFormFieldModule,
    MatInputModule,
    MatButtonModule,
    MatCardModule,
    MatDividerModule,
    MatToolbarModule,
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }


