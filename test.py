import pyautogui

# نمایش موقعیت مکانی موس
print("لطفاً موس را حرکت دهید...")
try:
    while True:
        x, y = pyautogui.position()
        position_str = f'موقعیت مکانی موس: x={x}, y={y}'
        print(position_str, end='\r')
except KeyboardInterrupt:
    print("\nبرنامه پایان یافت.")
