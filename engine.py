import re


def evaluate(data, fixture_path):
    currency = data["currency"]
    if not re.fullmatch(r"[A-Z]{3}", currency):
        raise ValueError("currency must be a three-letter uppercase code")
    amounts = [data[name] for name in ("invoice_minor", "allocated_minor", "shared_minor", "unallocated_minor")]
    if any(type(amount) is not int for amount in amounts):
        raise ValueError("amounts must be integers in minor units")
    invoice, *allocations = amounts
    residual = invoice - sum(allocations)
    return [] if not residual else [{"code": "invoice_unbalanced", "currency": currency, "residual_minor": residual}]
