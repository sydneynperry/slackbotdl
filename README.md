# slackbotdl
Deep learning slack bot. Intern project 1
research-bot/
│
├── config/
│   └── settings.yaml                # Configuration settings (API keys, search params, thresholds)
│   └── prompts/                    # Structured prompts for each LLM task
│       ├── intent_classification.txt
│       ├── search_strategy.txt
│       └── synthesis_prompt.txt
│
├── ingestion/
│   ├── slack_listener.py           # Slack bot entrypoint (listens for user queries)
│   ├── query_handler.py            # Passes query through triage pipeline
│   └── clarifier.py                # Clarification loop logic
│
├── triage/
│   ├── intent_recognizer.py        # Intent classification using LLM
│   ├── entity_extractor.py         # Extracts keywords, projects, people, etc.
│   ├── clarity_checker.py          # Determines if query is clear or ambiguous
│
├── retrieval/
│   ├── strategy_decider.py         # Chooses internal, external, or hybrid strategy
│   ├── internal_search.py          # Embedding and similarity search against internal vector DB
│   ├── external_search.py          # Query generation and search engine API usage
│   └── retriever.py                # Unified interface for retrieval step
│
├── synthesis/
│   ├── context_builder.py          # Combines internal + external docs into a single context block
│   ├── answer_synthesizer.py       # LLM-based answer synthesis
│   └── self_critic.py              # Evaluates whether the synthesized answer is sufficient
│
├── response/
│   ├── slack_formatter.py          # Formats answers using Slack Block Kit
│   ├── followup_generator.py       # Suggests intelligent follow-up questions
│   └── response_dispatcher.py      # Sends message back to Slack
│
├── feedback/
│   ├── feedback_listener.py        # Handles 👍 / 👎 feedback
│   ├── feedback_logger.py          # Logs feedback to database or file
│   └── flag_for_review.py          # Flags bad results for human review
│
├── models/
│   └── embeddings.py               # Custom embedding setup (if applicable)
│   └── llm_interface.py            # Central wrapper for calling different LLMs
│
├── utils/
│   ├── logger.py                   # Centralized logging
│   ├── validators.py               # Input sanitization, etc.
│   └── helpers.py                  # General utilities
│
├── tests/
│   ├── test_ingestion.py
│   ├── test_retrieval.py
│   ├── test_synthesis.py
│   └── ...
│
├── data/
│   ├── internal_documents/         # Local storage of vectorized internal documents
│   ├── feedback_logs/              # Feedback storage (JSON, CSV, etc.)
│   └── ...
│
├── main.py                         # Orchestrates full pipeline: query → response
└── requirements.txt                # Python package dependencies
#  AI-Powered Research Bot

This project implements an intelligent, multi-phase research assistant that operates inside Slack. It dynamically interprets user queries, retrieves information from both internal and external sources, synthesizes coherent answers using LLMs, and formats responses for Slack delivery. The bot continuously improves through feedback collection and self-evaluation loops.

---

##  Features

- **Intent Detection & Clarity Checking**
  - Determines query goals (e.g., summarize, compare, find data).
  - Asks clarifying questions if the query is ambiguous.

- **Strategic Information Retrieval**
  - Searches internal vector database or the web, depending on context.
  - Supports hybrid retrieval (internal + external) when needed.

- **LLM-Powered Synthesis**
  - Merges and reasons over multiple sources to generate concise answers.
  - Self-checks answer quality and loops back if incomplete.

- **Slack Integration**
  - Accepts natural language queries via Slack.
  - Formats answers with interactive Slack Block Kit UI.

- **Feedback Loop**
  - Users can rate answers with 👍 / 👎.
  - Poor responses are flagged for human review.

---

