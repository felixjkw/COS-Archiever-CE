import os 
from dataclasses import dataclass

@dataclass
class Config:

    #Claudant Database
    claudant_url: str = os.getenv("CLAUDANT_URL", "")
    claudant_api_key: str = os.getenv("CLAUDANT_API_KEY", "")
    claudant_database: str = os.getenv("CLAUDANT_DATABASE", "")

    #COS
    cos_endpoint: str = os.getenv("COS_ENDPOINT", "")
    cos_api_key: str = os.getenv("COS_API_KEY", "")
    source_bucket: str = os.getenv("COS_BUCKET", "")
    destination_bucket: str = os.getenv("COS_DESTINATION_BUCKET", "")
    cos_instance_crn: str = os.getenv("COS_INSTANCE_CRN", "")
    cos_region: str = os.getenv("COS_REGION", "")

    #Code Engine
    ce_project_id: str = os.getenv("CODE_ENGINE_PROJECT_ID", "")
    ce_region: str = os.getenv("CODE_ENGINE_REGION", "")
    
    #WorkerConfig
    default_batch_size: int = int(os.getenv("DEFAULT_BATCH_SIZE", "100"))
    max_workers_default: int = int(os.getenv("MAX_WORKERS_DEFAULT", "50"))
    threads_per_worker_default: int = int(os.getenv("THREADS_WORKER_DEFAULT", "2"))

    #RetryMechanism
    max_retries: int = int(os.getenv("MAX_RETRIES", "3"))
    delay_retry:int = int(os.getenv("RETRY_DELAY", "5"))

    # Logging
    log_level: str = os.getenv('LOG_LEVEL', 'INFO')

