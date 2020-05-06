""" Простой шаблон для консольных программ. Автор CatsCanFly"""
import os,textwrap

lang_pack = {'text':{'RU':{'inp':'Ввод: ',
                           'q': '\nВыход из программы',
                           'errinp': 'Некоректный ввод',
                           'wip': '\nФункция в разработке',
                           'settings':'Доступные параметры:',
                           'param_name':'Введите номер параметра для изменения: ',
                           'err_func':'Ошибка функции',
                           'param_value':'Изменить параметр на ',
                           'err_param':'Недопустимый параметр',
                           'available_param':'Возможные параметры',
                           'cli_version':'Версия интерфейса: ',
                           'app_author':'Автор: ',
                           'about':'Это шаблон для программ на python с консольным интерфейсом)))',
                           'help':'Здесь хранится справка о программе. Информация о функциях, пунктах меню и порочее.'}},
             'menu':{'RU':{'main':{'C':'Очистить экран',
                                   'S':'Настройки',
                                   'H':'Справка',
                                   'Q':'Выход'},
                           'back_to_main':{'m':'Вернутся в главное меню'},
                           'example':{1:'something',2:'once again something'}}}}
app_settings = {'1':{'language':'RU'}}
app_constants = {'cli_ver':(1.2),
                 'designed_by':('CatsCanFly')}
available_settings = {'language':['RU']}
txt_list = lang_pack['text'][app_settings['1']['language']]
menu_txt = lang_pack['menu'][app_settings['1']['language']]
def tw_print(txt,len=119):
    print(textwrap.fill(txt, len))
def line_p(sym,len=119):
    print(sym*len)
def about():
    line_p('_')
    tw_print(txt_list['about'])
    line_p('_')
def main_menu():
    menu(menu_txt['main'])
    line_p('_')
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def menu(menu_lines):
    for line in menu_lines:
        print('{}. {}'.format(line,menu_lines[line]))
def wip():
    print(txt_list['wip'])
def wrong_input():
    print(txt_list['errinp'])
def error_function(err):
    print('{}: {}'.format(txt_list['err_func'],err))
def cli_info():
    print('{}{}\n{}{}'.format(txt_list['cli_version'],app_constants['cli_ver'],txt_list['app_author'],app_constants['designed_by']))
    line_p('_',119)
def clear_screen(inp):
    if inp not in ['C', 'c', 'С', 'с']: return False
    clear()
    about()
    main_menu()
def settings(inp):
    if inp not in ['S', 's', 'ы', 'Ы']: return False
    clear()
    while True:
        about()
        print(txt_list['settings'])
        for i in app_settings:
            for line in app_settings[i]:
                print('{}. {}: {}'.format(i, line, app_settings[i][line]))
        print('\n')
        menu(menu_txt['back_to_main'])
        line_p('_')
        i = input(txt_list['param_name'])
        if i in ['m','M','ь','Ь']:
            clear()
            about()
            main_menu()
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
                    print(txt_list['err_param'])
                    continue
        clear()
        continue
def help_info(inp):
    if inp not in ['H', 'h', 'р', 'Р']: return False
    line_p('_',119)
    tw_print(txt_list['help'])
    cli_info()
def quit_program(inp):
    if inp not in ['Q','q','й','Й']: return False
    print(txt_list['q'])
    quit()

'''



ОСНОВНАЯ ЧАСТЬ ДЛЯ КОДА



'''

def app_main():
    while True:
        i = input(txt_list['inp'])
        if clear_screen(i)!=False:continue
        if settings(i)!=False:continue
        if help_info(i)!=False:continue
        if quit_program(i)!=False:continue
        try:#здесь вписывать свои функции

            if example_function(i)!=False:continue
            elif example_function(i)!=False:continue
            elif example_function(i)!=False:continue
            elif example_function(i)!=False:continue
            elif example_function(i)!=False:continue

            else:
                wrong_input()
                continue
        except Exception as err:
            error_function(err)
            continue

def example_function(inp):# эта функция обрабатывает функции меню
    if inp not in ['У', 'у', 'E', 'e']: return False #ввод при котором функция выполняется
    # тело
    line_p('@')
    print('Образец функции')
    line_p('@')
    #/тело


about()
main_menu()
app_main()