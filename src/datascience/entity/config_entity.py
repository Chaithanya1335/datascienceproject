from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    root_dir:Path
    source_URL:str
    local_data_file:Path
    unzip_dir:Path

@dataclass
class DatavalidationConfig:
    root_dir:Path
    STATUS_FILE:str
    unzip_dir:Path
    all_schema:dict

@dataclass
class DataTransformationconfig:
    root_dir:Path
    data_path:Path