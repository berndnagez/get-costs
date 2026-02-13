
from src.get_refunds.refunds_reader import RefundsReader
from src.get_refunds.refunds_mapper import RefundsMapper


class RefundsService:

    def __init__(self):
        self.reader = RefundsReader()
        self.mapper = RefundsMapper()

    def get_refunds_as_dict(self, file_path: str) -> list[dict]:
        """
        Main entry point to read refunds from a file and return as a list of dicts.

        Args:
            file_path (str): Path to the refunds txt file.

        Returns:
            List[dict]: List of refunds in dictionary format.
        """
        refunds = self.reader.read(file_path)

        return self.mapper.list_to_dict(refunds)
