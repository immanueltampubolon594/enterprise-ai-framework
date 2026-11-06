<div align="center">

# 🌐 Enterprise AI Framework & RAG Toolkit (v2.5.0-Enterprise)
### *A Production-Grade, Highly Modular, and Scalable Python Architecture for Autonomous AI Agents, RAG Pipelines, and LLM Microservices.*

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110.0-teal.svg)](https://fastapi.tiangolo.com/)
[![Architecture](https://img.shields.io/badge/Architecture-Enterprise%20Microservices-orange.svg)]()
[![Code style: black](https://img.shields.io/badge/code%20style-black-00index.svg)](https://github.com/psf/black)
[![Tests Passing](https://img.shields.io/badge/tests-passing-brightgreen.svg)]()

[**Fitur Utama**](#-fitur-utama) • [**Arsitektur Codebase**](#-arsitektur-codebase-109-files) • [**Instalasi & Konfigurasi**](#-instalasi--konfigurasi) • [**Quick Start**](#-quick-start) • [**Testing Suite**](#-testing-suite) • [**Deployment**](#-deployment-infrastructure) • [**Kontribusi**](#-kontribusi)

</div>

---

## 📖 1. Ikhtisar Sistem (System Overview)

**Enterprise AI Framework** adalah ekosistem perangkat lunak tingkat enterprise yang dibangun dari awal (*from scratch*) untuk mengatasi kompleksitas dalam mendeploy aplikasi Large Language Models (LLM) ke lingkungan produksi skala besar. 

Framework ini mengintegrasikan pola desain *Clean Architecture*, *Design Patterns* berorientasi objek, *asyncio concurrency*, serta pemisahan tanggung jawab (*separation of concerns*) yang ketat antara *Core Engine*, *API Layer*, *Database Repositories*, dan *Background Workers*.

### Mengapa Framework Ini Dibangun?
1. **Mengatasi Hallucination**: Menggunakan *Robust JSON Parsers* dan *Pydantic Validators* untuk memastikan output LLM selalu terstruktur.
2. **Skalabilitas Tinggi**: Arsitektur modular memungkinkan penambahan *Custom Tools*, *Vector Stores*, dan *LLM Providers* tanpa merusak kode yang sudah ada.
3. **Observabilitas (Observability)**: Sistem *Logging* dan *Telemetry Callbacks* bawaan untuk memantau latensi dan penggunaan token secara real-time.

---

## 📂 2. Arsitektur Codebase (109+ Files)

Berikut adalah struktur direktori lengkap dari framework ini, dirancang modular untuk memudahkan pemeliharaan (*maintainability*):

```text
enterprise-ai-framework/
│
├── api/                                # API Gateway & Microservices Layer
│   ├── v1/
│   │   ├── endpoints.py                # REST API controllers (POST/GET/PUT/DELETE)
│   │   ├── dependencies.py             # Dependency injection (Auth, DB Session)
│   │   ├── schemas.py                  # Pydantic request/response validation schemas
│   │   ├── middleware.py               # Custom CORS, Rate limiting, & Error middleware
│   │   └── auth.py                     # JWT Token validation & API Key verification
│   ├── v2/
│   │   ├── endpoints.py                # Advanced asynchronous v2 endpoints
│   │   ├── schemas.py                  # Extended v2 validation schemas
│   │   └── websockets.py               # Real-time streaming chat & agent execution
│   └── core/
│       ├── server.py                   # FastAPI Application Factory & Lifespan events
│       ├── router.py                   # Central API router aggregator
│       └── rate_limiter.py             # Redis-backed distributed rate limiter
│
├── core/                               # Core AI & LLM Engine
│   ├── agents/
│   │   ├── base_agent.py               # Abstract base class untuk semua agen AI
│   │   ├── react_agent.py              # ReAct (Reasoning & Acting) execution loop
│   │   ├── planning_agent.py           # Multi-step task planner & breakdown engine
│   │   ├── executor.py                 # Tool execution engine with exception safety
│   │   └── router.py                   # Intent classification & dynamic agent router
│   ├── chains/
│   │   ├── base_chain.py               # Abstract Chain execution interface
│   │   ├── llm_chain.py                # Standard Prompt -> LLM execution chain
│   │   ├── sequential_chain.py         # Multi-stage pipeline execution chain
│   │   ├── transform_chain.py          # Data transformation & pre-processing chain
│   │   └── router_chain.py             # Conditional execution branching chain
│   ├── prompts/
│   │   ├── base_prompt.py              # Prompt template abstract interface
│   │   ├── chat_prompt.py              # System/User/Assistant role message builder
│   │   ├── few_shot_prompt.py          # Dynamic few-shot example selector & injector
│   │   ├── templates.py                # Pre-built enterprise prompt templates repository
│   │   └── serializer.py               # Prompt versioning and state serialization
│   ├── memory/
│   │   ├── base_memory.py              # Abstract memory backend interface
│   │   ├── buffer_memory.py            # Sliding window conversation buffer memory
│   │   ├── summary_memory.py           # LLM-compressed conversational summary memory
│   │   ├── redis_memory.py             # Distributed Redis session memory store
│   │   └── vector_memory.py            # Long-term semantic episodic vector memory
│   ├── tools/
│   │   ├── base_tool.py                # Abstract Base Tool with JSON Schema generation
│   │   ├── calculator.py               # Safe sandboxed math evaluation tool
│   │   ├── web_search.py               # Mock/Live enterprise web search tool connector
│   │   ├── sql_query.py                # Safe read-only natural language to SQL tool
│   │   ├── python_repl.py              # Sandboxed python execution environment tool
│   │   └── file_io.py                  # Secure file read/write workspace management tool
│   ├── embeddings/
│   │   ├── base_embedding.py           # Abstract embedding vector provider
│   │   ├── openai_embedding.py         # OpenAI text-embedding-3-small/large wrapper
│   │   ├── huggingface_embedding.py    # Local open-source sentence-transformers wrapper
│   │   ├── chunker.py                  # Advanced semantic & recursive text chunker
│   │   └── cache.py                    # Redis-backed embedding response cache layer
│   ├── vectorstores/
│   │   ├── base_vectorstore.py         # Abstract vector store interface (CRUD)
│   │   ├── chroma_store.py             # ChromaDB local persistence vector store
│   │   ├── pinecone_store.py           # Pinecone cloud distributed vector database
│   │   ├── faiss_store.py              # Facebook FAISS high-performance local index
│   │   └── memory_store.py             # In-memory numpy vector store for testing
│   ├── parsers/
│   │   ├── base_parser.py              # Abstract output parser interface
│   │   ├── json_parser.py              # Robust LLM markdown/regex JSON parser
│   │   ├── pydantic_parser.py          # Automatic Pydantic schema validation parser
│   │   ├── regex_parser.py             # Custom regular expression pattern extractor
│   │   └── csv_parser.py               # Tabular data and CSV output structured parser
│   ├── callbacks/
│   │   ├── base_callback.py            # Event-driven callback handler interface
│   │   ├── stdout_callback.py          # Console printing and streaming handler
│   │   ├── logging_callback.py         # Enterprise file & structured JSON logger
│   │   ├── telemetry_callback.py       # OpenTelemetry APM tracing integration
│   │   └── metrics_callback.py         # Prometheus token usage & latency metrics
│   ├── retrievers/
│   │   ├── base_retriever.py           # Abstract document retriever interface
│   │   ├── vector_retriever.py         # Semantic similarity vector space retriever
│   │   ├── bm25_retriever.py           # Keyword-based sparse BM25 text retriever
│   │   ├── ensemble_retriever.py       # Hybrid retrieval (Dense + Sparse fusion)
│   │   └── reranker.py                 # Cross-encoder neural document reranking layer
│   ├── exceptions/
│   │   ├── base_exception.py           # Root framework custom exception class
│   │   ├── model_exception.py          # LLM API connection & timeout exceptions
│   │   ├── parsing_exception.py        # Malformed output & JSON extraction failures
│   │   ├── token_exception.py          # Context window overflow & token limits
│   │   └── rate_limit_exception.py     # Provider throttling & exponential backoff
│   └── utils/
│       ├── logger.py                   # Centralized colorized logging setup
│       ├── config.py                   # Pydantic-settings env configuration loader
│       ├── helpers.py                  # General-purpose utility functions
│       ├── validators.py               # Data integrity and type check validators
│       ├── retry.py                    # Decorator-based exponential backoff retry handler
│       └── async_helper.py             # Asynchronous concurrency management utilities
│
├── database/                           # Persistence & Data Access Layer
│   ├── migrations/
│   │   ├── env.py                      # Alembic environment migration runner
│   │   ├── script.py.mjs               # Migration template generator script
│   │   └── versions/                   # Timestamped database schema migration files
│   ├── repositories/
│   │   ├── user_repo.py                # User profile & organization data access
│   │   ├── chat_repo.py                # Conversational thread & message persistence
│   │   ├── vector_repo.py              # Metadata index and chunk reference tracking
│   │   └── log_repo.py                 # Audit logs & agent execution telemetry storage
│   └── schemas/
│       ├── sql_models.py               # SQLAlchemy ORM relational database models
│       └── nosql_models.py             # Document store & cache schema definitions
│
├── workers/                            # Distributed Background Processing
│   ├── celery_app.py                   # Celery application broker initialization
│   ├── tasks.py                        # Long-running async AI tasks (Batch RAG, Training)
│   ├── queue_manager.py                # Priority queue orchestration & routing
│   └── scheduler.py                    # Periodic cron job task runner (Data syncing)
│
├── cli/                                # Command Line Interface Utility
│   ├── main.py                         # Click/Typer CLI entrypoint router
│   ├── commands.py                     # CLI command implementations (init, migrate, run)
│   ├── installer.py                    # Automated dependency & environment setup
│   └── formatter.py                    # CLI colored output formatting utility
│
├── tests/                              # Comprehensive Testing Suite
│   ├── unit/                           # Isolated component unit tests (Pytest)
│   ├── integration/                    # Multi-component integration tests (API & DB)
│   └── e2e/                            # End-to-end agent workflow & RAG pipeline tests
│
├── docs/                               # Technical Documentation
│   ├── architecture.md                 # Deep dive into system design patterns
│   ├── api_reference.md                # Complete Swagger/OpenAPI endpoint documentation
│   ├── contributing.md                 # Developer guidelines and code standard rules
│   └── changelog.md                    # Version history and breaking changes log
│
└── deploy/                             # Infrastructure & DevOps Configuration
    ├── helm_chart.yaml                 # Kubernetes Helm chart configuration templates
    ├── k8s_deployment.yaml             # Production Kubernetes pod & service manifests
    ├── terraform.tf                    # Cloud infrastructure as code (AWS/GCP resources)
    └── ansible_playbook.yml            # Server provisioning & automated setup playbooks
