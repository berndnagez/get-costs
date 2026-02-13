import re
from .refunds_models import Refund


class RefundsReader:
    pattern = re.compile(
        r"(?P<staff_id>\d{5})\s+"
        r"(?P<name>[\wÖÜÄöüäß ,'-.]+)\s+"
        r"(?:(?P<month>\d{2}/\d{4})\s+)?"
        r"(?P<levy_type>[A-Z]\d(?:-[A-Z]+)?)\s+"
        r"(?:(?P<last_day>\d{2}\.\d{2}\.\d{4})\s+)?"
        r"(?P<refunds_start_day>\d{2}\.\d{2}\.\d{4})\s+"
        r"(?P<refunds_end_day>\d{2}\.\d{2}\.\d{4})\s+"
        r"(?:(?P<data_id>[a-z0-9]+)\s+)?"
        r"(?P<data_transfer_day>\d{2}\.\d{2}\.\d{4})\s+"
        r"(?P<refund_amount>\d{1,3}(?:\.\d{3})*,\d{2})\s*"
        r"(?P<status>[A-Z])?"
    )

    def read(self, file_path: str):
        refunds = []
        all_lines = self.get_all_lines(file_path)
        refunds = self.extract_refunds(all_lines)
        return refunds

    def get_all_lines(self, file_path: str):
        all_lines = []
        f = open(file_path, "r", encoding="windows-1252")
        for line in f:
            all_lines.append(line)
        f.close()
        return all_lines

    def extract_refunds(self, lines):
        refunds = []
        for line in lines:
            match = self.pattern.match(line)
            if match:
                data = match.groupdict()
                for key, value in data.items():
                    if isinstance(value, str):
                        data[key] = value.strip()
                refunds.append(Refund(**data))
        return refunds
