from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    train_file_path: str
    test_file_path: str

@dataclass
class DataValidationArtifact:
    validation_status: bool
    valid_train_file_path: str
    valid_test_file_path: str
    invalid_train_file_path: str
    invalid_test_file_path: str
    drift_report_file_path: str


@dataclass
class DataTransfomationArtifact:
    transformed_object_file_path: str
    transformed_train_file_path:str
    transformed_test_file_path: str

@dataclass
class ClassficationMetricArtifact:
    f1_score: float
    precision_score: float
    recall_score: float


@dataclass
class ModleTrainerArtifact:
    trainer_model_file_path: str
    train_metric_artifact: ClassficationMetricArtifact
    test_metric_artifact: ClassficationMetricArtifact