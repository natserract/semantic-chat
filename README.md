# Semantic Search Supabase PG Vector + LangChain

The purpose of this guide is to demonstrate how to store OpenAI embeddings in Supabase Vector (Postgres + pgvector) with LangChain for the purposes of semantic search.

## Running

```bash
# Set environment
poetry shell

# Install packages
poetry install

# Running
poetry run python cli/run.py
```

## Issues

### Error code 429

```sh
Error code: 429 - {'error': {'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, read the docs: https://platform.openai.com/docs/guides/error-codes/api-errors.', 'type': 'insufficient_quota', 'param': None, 'code': 'insufficient_quota'}}
```

_Payment required?_: https://community.openai.com/t/probable-openai-bug-insufficient-quota-error-on-paid-account-with-available-balance/331067/14
