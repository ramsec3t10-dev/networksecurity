from dataclasses import dataclass
#with help of dataclass which acts as decorator which probably creates variable for an empty class

@dataclass
class DataIngestionArtifact:
    trained_file_path:str
    test_file_path:str