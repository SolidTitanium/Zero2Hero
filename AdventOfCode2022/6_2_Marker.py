with open(r".\Inputs\6_1_Input.txt") as f:
    text = f.read().strip()

window_size = 14
for i in range(len(text) - (window_size - 1)):
    window = text[i:i + window_size]
    if len(set(window)) == window_size:
        marker_position = i + window_size
        print(marker_position)
        break
