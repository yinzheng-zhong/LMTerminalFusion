# LMTerminalFusion

## Introduction
LMTerminalFusion is a tool that allows the local LLM or GPT to control the terminal. This project is inspired by TermGPT
(https://github.com/Sentdex/TermGPT). It doesn't do much for now but it's a fun tool to play with.

Currently tested with LMStudio.

## Usage
### Preset
The setting below is the best I can find so far. Other settings may still work but please make sure the text generation
is stopped at a proper time.

```json
{
  "name": "LMTerminalFusion",
  "inference_params": {
    "pre_prompt": "Below is an instruction that describes a task. Write a response that appropriately completes the request.",
    "pre_prompt_prefix": "\n### System Prompt\n",
    "pre_prompt_suffix": "\n",
    "input_prefix": "### Instruction\n",
    "input_suffix": "\n### Response\n",
    "antiprompt": [
      "### Instruction"
    ]
  },
  "load_params": {
    "rope_freq_scale": 0,
    "rope_freq_base": 0
  }
}
```

Set the `context over flow policy` to `Keep the system prompt and the first user message, truncate middle`.