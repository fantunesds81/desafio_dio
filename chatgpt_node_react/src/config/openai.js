import OpenAI from "openai";

const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

const response = await openai.chat.completions.create({
  model: "gpt-4o-mini-2024-07-18",
  messages: [
    {
      "role": "system",
      "content": [
        {
          "type": "text",
          "text": "diga um nome legal para uma aula de node com chatgpt\n"
        }
      ]
    },
    {
      "role": "assistant",
      "content": [
        {
          "type": "text",
          "text": "\n"
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "diga um nome legal para uma aula de node com chatgpt"
        }
      ]
    }
  ],
  temperature: 1,
  max_tokens: 256,
  top_p: 1,
  frequency_penalty: 0,
  presence_penalty: 0,
  response_format: {
    "type": "text"
  },
});