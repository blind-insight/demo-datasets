from faker import Faker
from faker_datasets import Provider, add_dataset

fake = Faker()


# Setup our fake datasets for record generation.
@add_dataset(
    name="descriptions",
    filename="fixtures/medical.json",
    picker="description",
    root=".descriptions",
)
class ProcedureDescriptions(Provider):
    """Provider for Procedure Descriptions."""


fake.add_provider(ProcedureDescriptions)


@add_dataset(
    name="codes",
    filename="fixtures/medical.json",
    picker="code",
    root=".codes",
)
class ProcedureCodes(Provider):
    """Provider for Procedure Codes."""


fake.add_provider(ProcedureCodes)


@add_dataset(
    name="reason_codes",
    filename="fixtures/medical.json",
    picker="reason_code",
    root=".reason_codes",
)
class ReasonCodes(Provider):
    """Provider for Reason Codes."""


fake.add_provider(ReasonCodes)


@add_dataset(
    name="reason_descriptions",
    filename="fixtures/medical.json",
    picker="reason_description",
    root=".reason_descriptions",
)
class ReasonDescriptions(Provider):
    """Provider for Reason Descriptions."""


fake.add_provider(ReasonDescriptions)
