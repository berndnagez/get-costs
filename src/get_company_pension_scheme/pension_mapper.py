from .pension_models import Pension


class PensionMapper:

    @staticmethod
    def to_dict(pension: Pension) -> dict:
        """
        Converts a Pension object into a custom dictionary.

        Only selected fields are included, and some fields can be combined
        or transformed.

        Args:
            pension (Pension): The Pension object to convert.

        Returns:
            dict: A dictionary representation of the Pension with custom keys.
        """
        return {
            "staff_id": pension.staff_id,
            "name": pension.name,
            "month": pension.month,
            "pension_amount": pension.pension_amount
        }

    @staticmethod
    def list_to_dict(pensions: list[Pension]) -> list[dict]:
        return [PensionMapper.to_dict(p) for p in pensions]
