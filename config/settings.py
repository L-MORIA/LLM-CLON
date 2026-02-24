# Configuration settings for the Numerology RAG System

import os

class Config:
    """Configuration for the Numerology RAG system."""

    # Device configuration
    @staticmethod
    def get_device():
        # Detecting if GPU is available
        if os.environ.get('USE_GPU', 'false').lower() == 'true':
            return 'GPU'
        return 'CPU'

    # Database settings
    DB_URI = os.environ.get('DB_URI', 'sqlite:///numerology.db')  # Default to SQLite
    DB_TRACK_MODIFICATIONS = False

    # Model parameters
    MODEL_NAME = os.environ.get('MODEL_NAME', 'default_model')
    MODEL_VERSION = os.environ.get('MODEL_VERSION', '1.0')
    MAX_INPUT_LEN = int(os.environ.get('MAX_INPUT_LEN', 512))  # Default max input length
    BATCH_SIZE = int(os.environ.get('BATCH_SIZE', 16))  # Default batch size

    # API settings
    API_URL = os.environ.get('API_URL', 'http://localhost:5000')  # Default API URL
    API_TIMEOUT = int(os.environ.get('API_TIMEOUT', 30))  # Default timeout in seconds

    @staticmethod
    def init_app(app):
        """Initialize the application with the given configuration settings."""
        pass
