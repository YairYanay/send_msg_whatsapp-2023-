import webbrowser as web
from urllib.parse import quote
import pyautogui as pg
from pywhatkit.core import log
import time
from tqdm import tqdm

#older before yoni whatsapp that give me excel
def read_check_data():
    with open('../n.txt', encoding="utf8") as t:
        data = t.readlines()

    clear_phones = []
    for i in data:
        # print(i)
        if '+972' in i:
            clear_phones.append(i[len(i) - len('+972 58-689-2888') - 1:-1])

    clear_phones_isl = []
    for i in clear_phones:
        if("+972" in i):
            clear_phones_isl.append(i)

    clear_phones = clear_phones_isl
    print(clear_phones)
    print(len(clear_phones))

    msg = """
    מה קורה, אני מדבר איתך מקשרי תעופה
    סגרת חופשה לקיץ?
    רוצה לשמוע טיסות, מסיבות אטקרציות לזקינטוס, מאליה סאניביץ וכו…
    """

msg = """
היי מה קורה?
נעים מאד אני יאיר יחצן מדבר איתך מקשרי תעופה✈️
פה בשביל להציע לך ולחברים שלך חופשת קיץ שלא תשכחו 💙
טיסות, מסיבות אטרקציות…
היעדים שלנו:

יורט דה מאר🇪🇸
פלמה דה מאיורקה🇪🇸
זקינטוס ומאליה 🇬🇷
זרצ׳ה ביץ 🇭🇷
סאני ביץ🇧🇬
קפריסין🇨🇾
וכו…

מה דעתך רוצה פרטים נוספים?

להסרה - הגב "הסר"
"""
def send_whatsapp_msg(phone_no, msg):
    web.open(f"https://web.whatsapp.com/send?phone=+{phone_no}&text={quote(msg)}")
    time.sleep(15)
    pg.press("enter")
    #log.log_message(_time=time.localtime(), receiver=phone_no, message=msg)
    time.sleep(3)
    pg.hotkey('ctrl', 'w')


with open('phones', 'r') as fp:
    clear_phones = fp.read().split('\n')

# print(clear_phones)
count = 0
have_sent = 0
for i in tqdm(clear_phones):
    # print(i, end="")
    with open('my_sent_phone_h.txt', 'r') as fp:
        data_sent_phones = fp.read().split('\n')
    if(i not in data_sent_phones):
        send_whatsapp_msg(i, msg)
        # print("correct")
        open('my_sent_phone_h.txt', 'a+').write('\n' + i)
    else:
        # print("cant")
        have_sent += 1
    count += 1

print()
print("send msg for "+ str(count))
print("have sent befor for "+ str(have_sent))