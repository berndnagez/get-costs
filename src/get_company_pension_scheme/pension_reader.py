from .pension_models import Pension
from data_reader import reader
from src.get_costs.config import INDEX


class PensionReader:
    def get_dataframe(self, file):
        sheet_name = "first_sheet"
        df = reader.get_sheet_data(file, sheet_name, INDEX)
        return df.to_dict('dict')

    def parse_pensions(self, dataframe_dict):
        pensions = []
        names = dataframe_dict.get("Name,Vorname (MA)", {})
        for staff_id, name in names.items():
            pension_amount = dataframe_dict.get(
                "bAV AG-Anteil", {}).get(staff_id, "0.00")
            month = dataframe_dict.get(
                "Abrechnungsmonat", {}).get(staff_id, "Unknown")
            pensions.append(Pension(int(staff_id), name,
                            month, float(pension_amount)))
        return pensions

    def read(self, file) -> list:
        dataframe_dict = self.get_dataframe(file)
        return self.parse_pensions(dataframe_dict)
