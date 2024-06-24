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
# Related Question
> Question: Demographics condition in Indonesia?

> Answer: """
I don't have real-time data, but as of the last available statistics, Indonesia is the fourth-most populous country in the world with a population of over 260 million people. The largest ethnic group is Javanese, but there is a significant diversity of cultures, languages, and religions across the archipelago. The official religion is Islam, followed by Protestantism, Catholicism, Hinduism, and Buddhism. The population is relatively young, with a median age of around 30 years old.
"""

# Unrelated Question
> Question: Who is Nelson Mandela?

> Answer: """
I'm sorry for any confusion, but the context provided does not include any information about Nelson Mandela. He is a significant historical figure from South Africa, known for his fight against apartheid and his role as the first black president of South Africa.
"""
```

## Issues

### Error code 429

```sh
Error code: 429 - {'error': {'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, read the docs: https://platform.openai.com/docs/guides/error-codes/api-errors.', 'type': 'insufficient_quota', 'param': None, 'code': 'insufficient_quota'}}
```

So, I decided to not using OpenAI, and migrate to FireWorksAI (or any similar goals) instead.

> _Payment required?_: https://community.openai.com/t/probable-openai-bug-insufficient-quota-error-on-paid-account-with-available-balance/331067/14 :)
