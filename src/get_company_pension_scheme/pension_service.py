from src.get_company_pension_scheme.pension_reader import PensionReader
from src.get_company_pension_scheme.pension_mapper import PensionMapper


class PensionService:

    def __init__(self):
        self.reader = PensionReader()
        self.mapper = PensionMapper()

    def get_pension_as_dict(self, file_path: str) -> dict:
        """
        Main entry point to read pension scheme from a file and return as a dict.

        Args:
            file_path (str): Path to the pension scheme excel file.
        Returns:
            List[dict]: List of company pension schemes in dictionary format.
        """
        pension_scheme = self.reader.read(file_path)

        return self.mapper.list_to_dict(pension_scheme)
