from .refunds_models import Refund


class RefundsMapper:

    @staticmethod
    def to_dict(refund: Refund) -> dict:
        """
        Converts a Refund object into a custom dictionary.

        Only selected fields are included, and some fields can be combined
        or transformed.

        Args:
            refund (Refund): The Refund object to convert.

        Returns:
            dict: A dictionary representation of the Refund with custom keys.
        """
        return {
            "title": f"{refund.levy_type} {refund.name} {RefundsMapper.format_period(refund.refunds_start_day, refund.refunds_end_day)}",
            "staff_id": refund.staff_id,
            "month": refund.month,
            "refund_amount": refund.refund_amount,
            "status": refund.status
        }

    @staticmethod
    def list_to_dict(refunds: list[Refund]) -> list[dict]:
        return [RefundsMapper.to_dict(r) for r in refunds]

    @staticmethod
    def format_period(start: str, end: str) -> str:
        """
        Formats the period from start and end dates.
        """
        if not start or not end:
            return ""

        start_day, start_month, start_year = start.split(".")
        end_day, end_month, end_year = end.split(".")
        start_year_short = start_year[2:]
        end_year_short = end_year[2:]

        if start_day == end_day and start_month == end_month and start_year == end_year:
            return f"{start_day}.{start_month}.{start_year_short}"
        if start_month == end_month and start_year == end_year:
            return f"{start_day}. - {end_day}.{end_month}.{end_year_short}"
        else:
            return f"{start_day}.{start_month}.{start_year_short} - {end_day}.{end_month}.{end_year_short}"
