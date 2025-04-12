import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class OpenAiChatService {

  private apiUrl = 'http://localhost:8080/api/chat';

  constructor(private http: HttpClient) {}

  askQuestion(prompt: string) {
    return this.http.post(this.apiUrl, { prompt }, { responseType: 'text' });
  }
}