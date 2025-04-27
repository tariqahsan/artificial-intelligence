import { Component } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { FormControl } from '@angular/forms';

@Component({
  selector: 'app-ollama-ai-chat',
  standalone: false,
  templateUrl: './ollama-ai-chat.component.html',
  styleUrl: './ollama-ai-chat.component.css'
})
// Ollama running locally

// export class OllamaAiChatComponent {
//   prompt = new FormControl('');
//   responseText = '';
//   loading = false;
//   apiname = "Ollama"

//   constructor(private http: HttpClient) {}

//   sendPrompt() {
//     this.loading = true;
//     const body = {
//       model: 'mistral',
//       prompt: this.prompt.value,
//       stream: false
//     };

//     this.http.post<any>('http://localhost:11434/api/generate', body).subscribe({
//       next: (res) => {
//         this.responseText = res.response;
//         this.loading = false;
//       },
//       error: (err) => {
//         this.responseText = 'Error: ' + err.message;
//         this.loading = false;
//       }
//     });
//   }
// }
  

// Existing imports - add HttpHeaders if missing
//import { HttpClient, HttpHeaders } from '@angular/common/http';

// Ollama running on Docker Desktop
export class OllamaAiChatComponent {
  prompt = new FormControl('');
  responseText = '';
  loading = false;
  apiname = "Ollama"

  constructor(private http: HttpClient) {}
// Modify sendPrompt() method
sendPrompt() {
  this.loading = true;
  const body = {
    model: 'llama3', // Changed from 'mistral'
    stream: false,
    messages: [ // Replaces 'prompt' field
      { 
        role: 'user', 
        content: this.prompt.value || '' 
      }
    ]
  };

  // Update endpoint and headers
  this.http.post<any>(
    'http://localhost:11434/api/chat', // Changed from /api/generate
    body,
    {
      headers: new HttpHeaders({
        'Content-Type': 'application/json' // Explicit header
      })
    }
  ).subscribe({
    next: (res) => {
      this.responseText = res.message?.content || ''; // New response path
      this.loading = false;
    },
    error: (err) => {
      this.responseText = 'Error: ' + (err.message || 'Unknown error');
      this.loading = false;
    }
  });
}
}
