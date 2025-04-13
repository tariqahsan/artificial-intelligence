package org.mma.SpringAIDemo;

//import org.springframework.ai.openai.OpenAiChatModel;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.Map;

import org.springframework.ai.openai.OpenAiChatClient;
import org.springframework.beans.factory.annotation.Autowired;

@RestController
@RequestMapping("/api/chat")
@CrossOrigin(origins = "*") // Optional: allow all for testing
public class OpenAIController {

    @Autowired
    private OpenAiChatClient chatClient;

    @PostMapping
    public ResponseEntity<Map<String, String>> askQuestion(@RequestBody ChatRequest request) {
        String result = chatClient.call(request.getPrompt());
        Map<String, String> response = Map.of("response", result);
        return ResponseEntity.ok(response); // 200 OK with JSON body
}

    // DTO class
    public static class ChatRequest {
        private String prompt;

        public String getPrompt() {
            return prompt;
        }

        public void setPrompt(String prompt) {
            this.prompt = prompt;
        }
    }
}
