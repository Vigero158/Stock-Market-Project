def zigzag(data, deviation):
    """
    Calculates zigzag highs and lows given a dataframe of prices and a deviation threshold
    """
    zigzag_highs = pd.Series(dtype=np.float64)
    zigzag_lows = pd.Series(dtype=np.float64)
    last_zigzag_high = np.NaN
    last_zigzag_low = np.NaN
    direction = 0
    for i in range(len(data)):
        price = data.iloc[i]
        if pd.isna(last_zigzag_high):
            last_zigzag_high = price
            zigzag_highs[i] = price
        elif pd.isna(last_zigzag_low):
            last_zigzag_low = price
            zigzag_lows[i] = price
        else:
            if direction <= 0 and price - last_zigzag_low >= deviation:
                last_zigzag_high = price
                zigzag_highs[i] = price
                direction = 1
            elif direction >= 0 and last_zigzag_high - price >= deviation:
                last_zigzag_low = price
                zigzag_lows[i] = price
                direction = -1
            else:
                zigzag_highs[i] = np.NaN
                zigzag_lows[i] = np.NaN
    return zigzag_highs, zigzag_lows