""" Простой шаблон для консольных программ"""
import os

lang_pack = {'text':{'RU':{'inp':'\nВвод: ',
                            'q': '\nВыход из программы',
                            'errinp': 'Некоректный ввод',
                            'wip': '\nФункция в разработке',
                            'settings':'Доступные параметры:',
                            'param_name':'Введите номер параметра для изменения: ',
                            'param_value':'Изменить параметр на ',
                            'err_param':'Недопустимый параметр',
                            'available_param':'Возможные параметры',
                            'about':'Это шаблон для программ на python с консольным интерфейсом)))\nАвтор: CCF'}},
             'menu':{'RU':{'main':{'s':'Настройки','q':'Q. Выход',},
                           'back_to_main':{'m':'Вернутся в главное меню'},
                           'example':{1:'something',2:'once again something'}}}}
app_settings = {'1':{'language':'RU'}}
available_settings = {'language':['RU']}
txt_list = lang_pack['text'][app_settings['1']['language']]
menu_txt = lang_pack['menu'][app_settings['1']['language']]


def about():
    print('-'*80)
    print(txt_list['about'])
    print('-'*80+'\n')
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def menu(menu_lines):
    for line in menu_lines:
        print('{}. {}'.format(line,menu_lines[line]))
def wip():
    print(txt_list['wip'])
def wrong_input():
    print(txt_list['errinp'])
def settings(inp):
    if inp not in ['S', 's', 'ы', 'Ы']: return False
    clear()
    while True:
        print(txt_list['settings'])
        for i in app_settings:
            for line in app_settings[i]:
                print('{}. {}: {}'.format(i, line, app_settings[i][line]))
        print('\n')
        menu(menu_txt['back_to_main'])
        i = input(txt_list['param_name'])
        if i in ['m','M','ь','Ь']:
            clear()
            menu(menu_txt['main'])
            break
        if app_settings.get(i)!=None:
            param = []
            for j in app_settings[i]: param.append(j)
            print('{}: {}'.format(txt_list['available_param'],available_settings[param[0]]))
            while True:
                b = input(txt_list['param_value'])
                if b in available_settings[j]:
                    app_settings[i].update({j:b})
                    break
                if b in ['m','M','ь','Ь']: break
                else:
                    print(txt_list['err_param'],)
                    continue

        clear()
        continue

    #else: return False
def quit_program(inp):
    if inp in ['Q','q','й','Й']:
        print(txt_list['q'])
        quit()
    else:return False
def app_main():
    while True:
        i = input(txt_list['inp'])
        if quit_program(i)!=False:continue
        elif settings(i)!=False:continue
        #здесь вписывать свои функции

        elif example_function(i)!=False:continue

        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        else:
            wrong_input()
            continue

def example_function(input):
    if input in ['У', 'у', 'E', 'e']: #ввод при котором функция выполняется
        # тело
        print('\n'+'-' * 170)
        print('Образец функции')
        print('\n'+'-' * 170)
        #/тело
    else: return False

'''
ОСНОВНАЯ ЧАСТЬ ДЛЯ КОДА
'''

about()
menu(menu_txt['main'])
app_main()