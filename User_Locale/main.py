from datetime import datetime
import locale

def get_data() -> str:

    # user_locale: tuple[str |None, str | None] = ('en_GB', 'UTF-8')
    user_locale: tuple[str |None, str | None] = locale.getlocale()

    try: 
        locale.setlocale(locale.LC_TIME, user_locale)
    except locale.Error:
        print(f'Locale "{user_locale}" is not supported on your system. Falling back to "C" locale.')
        locale.setlocale(locale.LC_TIME, 'C') # default for C programm, culture neutral locale for handling data

    today: datetime = datetime.now()

    return f'{today:%x}'

print(get_data())
                        