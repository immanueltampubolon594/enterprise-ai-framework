<div align="center">

# 🌐 Enterprise AI Framework & RAG Toolkit (v2.5.0-Enterprise)
### *A Production-Grade, Highly Modular, and Scalable Python Architecture for Autonomous AI Agents, RAG Pipelines, and LLM Microservices.*

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110.0-teal.svg)](https://fastapi.tiangolo.com/)
[![Architecture](https://img.shields.io/badge/Architecture-Enterprise%20Microservices-orange.svg)]()

[**Arsitektur Visual**](#-arsitektur-visual-system-architecture) • [**Struktur Codebase**](#-arsitektur-codebase-109-files) • [**Fitur Utama**](#-fitur-utama) • [**Quick Start**](#-quick-start)

</div>

---

## 🏗️ Arsitektur Visual (System Architecture)

Berikut adalah diagram visual arsitektur end-to-end dari *Enterprise AI Framework* ini, menggambarkan bagaimana request pengguna diproses dari API Gateway, melewati Core Engine (Agents & RAG), hingga penyimpanan data (Database & Vector Store):

```mermaid
graph TD
    %% Client Layer
    Client([Client / Frontend / CLI]) -->|HTTP / WebSockets| APIGateway[API Gateway <br/> FastAPI v1 & v2]

    %% API Layer
    subgraph API Layer [API & Microservices Layer]
        APIGateway --> Auth[Auth & Rate Limiter]
        Auth --> Endpoints[REST Endpoints & WebSockets]
    end

    %% Core AI Engine Layer
    Endpoints --> CoreEngine[Core AI Engine Orchestrator]
    
    subgraph Core Engine [Core AI & LLM Engine]
        CoreEngine --> Agents[Autonomous Agents <br/> ReAct / Planning]
        CoreEngine --> Chains[LLM Execution Chains]
        CoreEngine --> Retrievers[Hybrid Retrievers <br/> Vector + BM25 + Reranker]
        
        Agents --> Tools[Execution Tools <br/> Calculator, Web Search, SQL]
        Retrievers --> VectorStores[Vector Databases <br/> Chroma, Pinecone, FAISS]
        Agents --> Memory[Conversation Memory <br/> Buffer, Redis, Vector]
    end

    %% Data & Worker Layer
    CoreEngine --> Repositories[Data Repositories & ORM]
    
    subgraph Persistence & Async Workers
        Repositories --> PostgreSQL[(PostgreSQL Database)]
        Repositories --> Redis[(Redis Cache & Broker)]
        Redis --> Celery[Celery Background Workers]
    end

    style APIGateway fill:#009688,stroke:#333,stroke-width:2px,color:#fff
    style CoreEngine fill:#FF9800,stroke:#333,stroke-width:2px,color:#fff
    style PostgreSQL fill:#336791,stroke:#333,stroke-width:2px,color:#fff
    style Redis fill:#DC382D,stroke:#333,stroke-width:2px,color:#fff
