# Semantic Search Supabase PG Vector + LangChain

The purpose of this guide is to demonstrate how to store embeddings in Supabase Vector (Postgres + pgvector) with LangChain for the purposes of semantic search.

## Tools

- LLM Framework: [LangChain](https://python.langchain.com/)
- ChatModel: [FireWorks](https://fireworks.ai/)
- Embeddings: [Spacy](https://spacy.io/usage/embeddings-transformers)

## Running

```bash
# Set environment
poetry shell

# Install spacy model
python -m spacy download en_core_web_sm

# Install packages
poetry install

# Running
poetry run python cli/run.py
```

## Example Questions

```sh
> Question: Do you know famous indonesian athletes?
> Answer: """
Famous Indonesian Athletes
--------------------------

### 1. **Lily Sri Martha**

*   **Sport**: Weightlifting
*   **Achievements**: Gold medalist in the 1988 Seoul Olympics, setting a world record in the 44 kg weight class.

### 2. **Rudy Hartono**

*   **Sport**: Badminton
*   **Achievements**: Eight-time All England Open champion (1968-1974, 1976) and gold medalist in the 1972 Munich Olympics.

### 3. **Susi Susanti**

*   **Sport**: Badminton
*   **Achievements**: Gold medalist in the 1992 Barcelona Olympics and a four-time SEA Games gold medalist.
...
"""
```

## Issues

### Error code 429

```sh
Error code: 429 - {'error': {'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, read the docs: https://platform.openai.com/docs/guides/error-codes/api-errors.', 'type': 'insufficient_quota', 'param': None, 'code': 'insufficient_quota'}}
```

So, I decided to not using OpenAI, and migrate to FireWorksAI (or any similar goals) instead.

_Payment required?_: https://community.openai.com/t/probable-openai-bug-insufficient-quota-error-on-paid-account-with-available-balance/331067/14
