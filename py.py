from telegram.ext import CommandHandler, Updater
import pyautogui
import time


# تابعی برای باز کردن MetaTrader 5
def open_mt5(update, context):
    def open_meta ():
        pyautogui.press('win')
        time.sleep(1)
        pyautogui.write('metatrader5')
        time.sleep(1)
        pyautogui.press('enter')  # فشردن کلید اینتر برای باز کردن ماشین حساب
        time.sleep(2)

    def open_account():
        pyautogui.click(x=100, y=100)  # مثال: موقعیت (100, 100) را کلیک می‌کند
        pyautogui.click(x=114, y=243)  # مثال: موقعیت (100, 100) را کلیک می‌کند

    open_meta()
    open_account()


# تنظیمات ربات
def main():
    updater = Updater(token='6781593273:AAHIlR4MqkGr42O_rd3JXnYnUS7-4QDwh_I2+3'
                            '', use_context=True)
    dispatcher = updater.dispatcher

    # ایجاد دستور برای باز کردن MetaTrader 5
    open_mt5_handler = CommandHandler('open_mt5', open_mt5)
    dispatcher.add_handler(open_mt5_handler)

    # شروع polling
    updater.start_polling()
    updater.idle()
    


if __name__ == "__main__":
    main()
