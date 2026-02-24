import os
from pathlib import Path
from typing import Literal

# Базовые пути
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
PDF_DIR = DATA_DIR / "pdfs"
PROCESSED_DIR = DATA_DIR / "processed"
MODELS_DIR = DATA_DIR / "models"
LOGS_DIR = BASE_DIR / "logs"

# Создание папок если их нет
for directory in [DATA_DIR, PDF_DIR, PROCESSED_DIR, MODELS_DIR, LOGS_DIR]:
    directory.mkdir(parents=True, exist_ok=True)

# ============ ОСНОВНЫЕ ПАРАМЕТРЫ ============
PROJECT_NAME = "Numerology RAG System"
PROJECT_VERSION = "1.0.0"
LANGUAGE = "ru"  # Русский язык

# ============ PDF ОБРАБОТКА ============
PDF_CONFIG = {
    "ocr_lang": "rus+eng",  # Tesseract языки
    "ocr_timeout": 60,  # Таймаут OCR в секундах
    "min_text_length": 10,  # Минимальная длина текста для считки
    "dpi_for_ocr": 300,  # DPI для OCR сканов
    "binary_threshold": 200,  # Порог бинаризации для улучшения OCR
}

# ============ EMBEDDINGS ============
EMBEDDINGS_CONFIG = {
    "model_name": "intfloat/multilingual-e5-large",  # multilingual-e5
    "model_dimension": 1024,  # Размер вектора E5-large
    "batch_size_cpu": 4,  # Батч для CPU
    "batch_size_gpu": 32,  # Батч для GPU
    "cache_embeddings": True,
}

# ============ CHUNKING ============
CHUNKING_CONFIG = {
    "chunk_size": 512,  # Размер чанка в токенах
    "chunk_overlap": 50,  # Перекрытие между чанками
    "min_chunk_size": 100,  # Минимальный размер чанка
}

# ============ RETRIEVAL ============
RETRIEVAL_CONFIG = {
    "top_k": 5,  # Количество результатов
    "rerank_top_k": 10,  # Переранжирование топ N
    "bm25_weight": 0.4,  # Вес BM25 в гибридном поиске
    "faiss_weight": 0.6,  # Вес FAISS в гибридном поиске
    "cosine_threshold": 0.3,  # Минимальный порог косинуса для результата
}

# ============ LLM ============
LLM_CONFIG = {
    "model_name": "qwen2:8b",  # Модель Qwen2 8B
    "temperature": 0.7,
    "top_p": 0.9,
    "max_tokens": 512,  # Максимум токенов в ответе
    "timeout": 10,  # Таймаут ответа в секундах
    "context_size": 2048,  # Размер контекста
}

# ============ БАЗА ДАННЫХ ============
DATABASE_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "port": int(os.getenv("DB_PORT", "5432")),
    "user": os.getenv("DB_USER", "numerology"),
    "password": os.getenv("DB_PASSWORD", "numerology_pass"),
    "database": os.getenv("DB_NAME", "numerology_db"),
    "pool_size": 20,
    "max_overflow": 40,
}

# ============ API ============
API_CONFIG = {
    "host": "0.0.0.0",
    "port": 8000,
    "reload": True,
    "workers": 4,
}

# ============ TELEGRAM ============
TELEGRAM_CONFIG = {
    "token": os.getenv("TELEGRAM_BOT_TOKEN", "YOUR_TOKEN_HERE"),
    "max_message_length": 4096,  # Максимум символов в Telegram
    "timeout": 30,
}

# ============ FRONTEND ============
FRONTEND_CONFIG = {
    "host": "0.0.0.0",
    "port": 3000,
    "api_base_url": "http://localhost:8000",
}

# ============ ЛОГИРОВАНИЕ ============
LOGGING_CONFIG = {
    "level": "INFO",
    "log_file": LOGS_DIR / "app.log",
    "format": "%\(asctime\)s - %\(name\)s - %\(levelname\)s - %\(message\)s",
}