from abc import ABC, abstractmethod

class DataProcessor(ABC):
    def process(self) -> None:
        self.load_data()
        self.analyze_data()
        self.save_results()

    @abstractmethod
    def load_data(self) -> None:
        pass

    @abstractmethod
    def analyze_data(self) -> None:
        pass

    @abstractmethod
    def save_results(self) -> None:
        pass

class CSVDataProcessor(DataProcessor):
    def load_data(self) -> None:
        print("Loading data from a CSV file...")

    def analyze_data(self) -> None:
        print("Analyzing data using CSV-specific algorithms...")

    def save_results(self) -> None:
        print("Saving analysis results to a CSV file...")

class JSONDataProcessor(DataProcessor):
    def load_data(self) -> None:
        print("Loading data from a JSON file...")

    def analyze_data(self) -> None:
        print("Analyzing data using JSON-specific algorithms...")

    def save_results(self) -> None:
        print("Saving analysis results to a JSON file...")

csv_processor = CSVDataProcessor()
csv_processor.process()

json_processor = JSONDataProcessor()
json_processor.process()