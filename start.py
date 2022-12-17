from pyrogram import Client, enums
import random
import time

start_print = '''
-----------------------------------

User Tag Telegram
(Тегает всех в чате)

-----------------------------------
'''
print(start_print)
print("Канал создателя to https://t.me/holey_moon")

api_id = 25983686
api_hash = "d49ffa3e2b617c66250b7f4c169d1cb9"
chat_name = input("Установи название чата (если не надо, просто [enter] жми):\n")

def get_list(f_name):
    return [row for row in open(f_name, encoding="utf-8").read().split("\n") if row]

app = Client(
    "alice",
    api_id=api_id, api_hash=api_hash
)


app.start()
dialogs = [dialog for dialog in app.get_dialogs(limit=20)]
x = 0
for dialog in dialogs:
    print(f"{x}. Айди чата: {dialog.chat.id}\n Название чата: {dialog.chat.title}\n Количество участников: {dialog.chat.members_count}")
    print("============================")
    x += 1
chat_id = dialogs[int(input())].chat.id
print(chat_id)
bad_list = []
members = [member for member in app.get_chat_members(chat_id, limit=20)]
x = 1
while True:
    for member in members:
        u_info = member.user
        first_name = u_info.first_name
        last_name = u_info.last_name
        if not last_name:
            last_name = ""
        print(f"{x}. Айди участника: {u_info.id}\n Имя: {first_name} {last_name}")
        print("============================")
        x += 1
    x = 1
    user_ch = int(input("\n0. Запустить!\n"))
    if user_ch == 0:
        break
    else:
        bad_id = members[user_ch-1].user.id
        bad_list.append(bad_id)
    print(f"Список выбранных айдишников {bad_list}")

words = get_list("sentences.txt")
push_text = get_list("push_text.txt")
chat_check = list(range(10))

while True:
    try:
        word = random.choice(words)
        push = random.choice(push_text)
        bad_id = random.choice(bad_list)
        msg = f"<a href='tg://user?id={bad_id}'>{push}</a> {word}"
        ch = random.choice(chat_check)
        if ch == 5:
            chat = app.get_chat(chat_id)
            title = chat.title
            if title != chat_name:
                app.set_chat_title(chat_id, chat_name)
                app.delete_chat_photo(chat_id)
        app.send_chat_action(chat_id, enums.ChatAction.TYPING)
        time.sleep(random.randint(5, 10))
        app.send_message(chat_id, msg, parse_mode=enums.ParseMode.HTML)
    except KeyboardInterrupt:
        break
    except:
        pass
    
    
app.stop()
