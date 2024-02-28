from aiogram.types import KeyboardButton


LIST_KEYBOARD_BUTTONS_FOR_START_HANDLER = [
    [
        KeyboardButton(text="1️⃣ Я предлагаю работу"),
        KeyboardButton(text="2️⃣ Я ищу работу"),
    ]
]

LIST_KEYBOARD_BUTTONS_FOR_COMMON_HANDLER_FIRST_OPTION = [
    [
        KeyboardButton(text="3️⃣ Смотреть резюме"),
        KeyboardButton(text="4️⃣ Создать вакансию"),
        KeyboardButton(text="🔙 НАЗАД")
    ]
]


LIST_KEYBOARD_BUTTONS_FOR_COMMON_HANDLER_SECOND_OPTION = [
    [
        KeyboardButton(text="3️⃣ Смотреть вакансии"),
        KeyboardButton(text="4️⃣ Создать резюме"),
        KeyboardButton(text="🔙 НАЗАД")
    ]
]


LIST_KEYBOARD_BUTTONS_FOR_DISPLAY_RESUME_HANDLER = [
    [
        KeyboardButton(text="3️⃣ Смотреть вакансии"),
        KeyboardButton(text="4️⃣ Создать резюме"),
        KeyboardButton(text="🔙 НАЗАД"),
        KeyboardButton(text="Next")
    ]
]

LIST_KEYBOARD_BUTTONS_FOR_DISPLAY_VACANCY_HANDLER = [
    [
        KeyboardButton(text="3️⃣ Смотреть вакансии"),
        KeyboardButton(text="4️⃣ Создать резюме"),
        KeyboardButton(text="🔙 НАЗАД"),
        KeyboardButton(text="NEXT")
    ]
]