# LangChain Prompt Learning

This repository contains my hands-on practice while learning LangChain with Python and the Groq API.

I created this project to understand how different prompting techniques work and how LangChain can be used to work with large language models.

## What I Learned

In this project, I practiced:

- Basic LLM interaction with LangChain
- Zero-shot prompting
- Few-shot prompting
- Chain of Thought prompting
- Self-consistency prompting
- Prompt Templates
- Using variables in prompts
- Connecting LangChain with the Groq API
- Using `.env` files to manage API keys

## Project Files

**`test_groq.py`**  
Tests the LangChain and Groq setup and sends a basic prompt to the model.

**`basic_prompt.py`**  
Contains basic examples of sending prompts to an LLM.

**`zeroshot_prompt.py`**  
Demonstrates zero-shot prompting, where the model is given a task without examples.

**`fewshot_prompt.py`**  
Demonstrates few-shot prompting by providing examples before asking the model to perform a task.

**`CoT_prompt.py`**  
Practices Chain of Thought prompting for problems that require step-by-step reasoning.

**`selfconsistency_prompt.py`**  
Practices self-consistency by generating multiple responses and comparing the results.

**`prompt_templates.py`**  
Practices LangChain Prompt Templates and using variables such as `{topic}` to create reusable prompts.

**`requirements.txt`**  
Contains the Python libraries required for the project.

## Technologies

- Python
- LangChain
- LangChain Groq
- Groq API
- python-dotenv

## Purpose

This is a learning project where I am building small examples to understand LangChain concepts step by step.

The focus is on understanding how prompts are created, structured, passed to language models, and reused rather than building a complete application.

## Current Status

This project is still in progress.

I will continue adding examples as I learn more LangChain concepts, including LangChain Expression Language (LCEL) and other LangChain components.
