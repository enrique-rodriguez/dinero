def to_dollars(amount):
    sign = '' if amount >= 0 else '-'
    amount = abs(amount)
    dollars = amount // 100
    cents = f"{amount % 100}".rjust(2, '0')

    return "{}${:,}.{}".format(sign, dollars, cents)