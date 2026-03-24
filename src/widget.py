from masks import get_mask_account, get_mask_card_number


def mask_account_card(account_info):

    info = str(account_info)
    parts = info.split()

    if parts[0].lower() == "счет":
        account_number = parts[-1]
        masked = get_mask_account(account_number)
        return f"Счет {masked}"
    else:
        card_number = parts[-1]
        card_name = " ".join(parts[:-1])
        masked = get_mask_card_number(card_number)
        return f"{card_name} {masked}"


result1 = mask_account_card("Visa Platinum 7000792289606361")
print("Visa Platinum 7000792289606361")
print({result1})

result2 = mask_account_card("Maestro 7000792289606361")
print("\nMaestro 7000792289606361")
print({result2})

result3 = mask_account_card("Счет 73654108430135874305")
print("\nСчет 73654108430135874305")
print({result3})

result4 = mask_account_card("Visa Gold 1234567890123456")
print("\nVisa Gold 1234567890123456")
print({result4})
