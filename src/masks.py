def get_mask_card_number(card_number):

    card = str(card_number)

    first_part = card[:4]
    second_part = card[4:6]
    third_part = card[-4:]

    return f"{first_part} {second_part}** **** {third_part}"


def get_mask_account(account_number):

    card = str(account_number)

    last_part = card[-4:]

    return f"**{last_part}"
