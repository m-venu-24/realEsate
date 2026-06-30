def get_recommendation(score):

    if score > 1.15:
        return "BUY"

    elif score > 1.0:
        return "HOLD"

    else:
        return "SELL"