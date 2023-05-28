hh = 0
mm = 0
ss = 0

while hh < 24:
    ss = ss + 1
    if ss == 60:
        ss = 0
        mm = mm + 1
    if mm == 60:
        mm = 0
        hh = hh + 1
    if hh == 24:
        hh = 0
        break
    print(f"{hh}:{mm}:{ss}")