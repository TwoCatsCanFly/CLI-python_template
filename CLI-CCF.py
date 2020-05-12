""" Простой шаблон для консольных программ. Автор CatsCanFly"""
import os,textwrap,shutil
from distutils.util import strtobool

app_constants = {'cli_ver':('1.26 beta 10'),
                 'designed_by':('CatsCanFly')}

app_menu = {'RU':{'main':{'C':['Очистить экран','Очищает текущий экран'],
                          'S':['Настройки','Настройки программы'],
                          'H':['Справка','Информация о программе'],
                          'Q':['Выход','Выход из программы']},'back_to_main':{'B':['Вернуться в предыдущее меню','']}},
            'EN': {'main': {'C': ['Clear screen','Clears the screen obviously'],
                            'S': ['Settings','App settings'],
                            'H': ['Help','Info about'],
                            'Q': ['Exit','Quit the program']},'back_to_main': {'B':['Back to previous menu','']}}}

app_text = {'RU':{'inp':'Ввод: ',
                   'err_inp': 'Некоректный ввод',
                   'q': 'Выход из программы',
                   'wip': 'Функция в разработке',
                   'settings':'Доступные параметры:',
                   'param_name':'Введите номер параметра для изменения:',
                   'param_value':'Изменить параметр на:',
                   'err_param':'Недопустимый параметр',
                   'available_param':'Возможные параметры',
                   'language':'Язык программы',
                   'show_description':'Отображать описание',
                   'desc_language':'Изменение языка программы',
                   'desc_show_description':'Отображает описание пунктов меню и опций',
                   'cli_version':'Версия интерфейса:',
                   'app_version':'Версия программы:',
                   'app_author':'Автор:',
                   'err_func':'Ошибка функции',
                   '404':'Информация отсутствует',
                   'desc_example':'Образец описания пункта меню',
                   'Example option one':'Образец пункта опций',
                   'Example option two':'Образец пункта опций'},
            'EN': {'inp':'Input: ',
                   'err_inp': 'Unknown Input',
                   'q': 'Quit the program',
                   'wip': 'Feature is in development',
                   'settings':'Available settings:',
                   'param_name':'Enter setting number:',
                   'param_value':'Change setting to:',
                   'err_param':'Incorrect Input',
                   'available_param':'Possible variants',
                   'language':'App language',
                   'desc_language':'Set app language',
                   'cli_version':'Interface version:',
                   'app_version':'App version:',
                   'app_author':'Author:',
                   'err_func':'Function Error',
                   '404':'Info unavailable',
                   'desc_example': 'Example description',
                   'Example option one': 'Setting example',
                   'Example option two': 'Setting example'}}

app_settings = {'language':{'value':'RU','setting_type':'choose_from_list','available_settings':['RU','EN'],'localization':True,'description':'desc_language'},
                'show_description':{'value':False,'setting_type':'bool','description':'desc_show_description','localization':True}}

# file_adr - адрес файла с допустимыми типами файла
# file_adr_ex - адрес файла исключая недопустимые типы файла
# directory_adr - адрес файла
# choose_from_list - выбор из списка
# int - целое число min-max
# float - дробное число min-max
# bool - True\False
# text - обычный текст с ограничением по количеству символов
# any - что угодно
# hidden - не отображается в меню

language = app_settings['language']['value']
def t_size():
    rows, columns = shutil.get_terminal_size(fallback=(80, 24))
    return rows
def app_input(inp,inp_type,param_settings=0):
    #функция проверяет на соответствие пользовательский ввод
    #возвращает True если тип ввод соответствует указанному в inp_type
    #Иначе возвращает False
    if inp_type=='file_adr':
        # в param_settings предается допустимые типы файлов. Например ['txt','png','ogg']
        try:
            file_extension = inp.split('.')[-1].lower()
            a = True if file_extension in param_settings else False
            if a: return os.path.isfile(inp)
        except: return False
    elif inp_type=='file_adr_ex':
        # в param_settings предается НЕДОПУСТИМЫЕ типы файлов. Например ['wtf','omg']
        try:
            file_extension = inp.split('.')[-1].lower()
            a = True if file_extension not in param_settings else False
            if a: return os.path.isfile(inp)
        except: return False
    elif inp_type=='directory_adr':
        # в параметрах param_settings передается должна ли папка существовать или нет [True or False]
        if param_settings[0]==False: return True #TODO добавить регулярку
        elif os.path.isdir(inp):return True
        else:return False
    elif inp_type=='choose_from_list':
        #в этом случае в param_settings передаются допустимые параметры
        a = []
        for id,i in enumerate(param_settings,1): a.append(str(id))
        if inp in a: return True
        else:return False
    elif inp_type=='int':
        # в param_settings передается [минимальное значение,максимальное значение]
        try:
            if param_settings == 0:
                a = int(inp)
                return True
            else:
                if param_settings[0] <= int(inp) <= param_settings[1]: return True
        except ValueError: return False
    elif inp_type=='bool':
        try:
            a = strtobool(inp)
            return True
        except ValueError: return False
    elif inp_type=='float':
        # в param_settings передается [минимальное значение,максимальное значение]
        # если param_settings нет то значение любое
        try:
            if param_settings == 0:
                a = float(inp.replace(',','.'))
                return True
            else:
                if param_settings[0]<=float(inp.replace(',','.'))<=param_settings[1]: return True
        except ValueError: return False
    elif inp_type=='text':
        # в param_settings передается [минимальная длинна,максимальная длинна]
        # если param_settings нет то значение любое
        if type(inp)=='str' and param_settings[0]<=len(inp)<=param_settings[1]: return True
        else: return False
    elif inp_type=='hidden': return False
    elif inp_type=='any': return True
    else: return False
def tw_print(txt,len=119):
    print(textwrap.fill(txt, len))
def line_p(sym,len=119):
    print(sym*len)
def line_block(txt,upper='_',lower='‾'):
    line_p(upper)
    print('{:#^119}'.format(txt))
    line_p(lower)
def about():
    line_block(' {app_name} v{app_ver} by {app_author} '.format(**user_constants))
    tw_print(user_text[app_settings['language']['value']]['about'])
    line_p('_')
def main_menu():
    menu(user_menu[app_settings['language']['value']]['main'])
    menu(app_menu[app_settings['language']['value']]['main'])
    line_p('‾')
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def menu(menu_lines):
    for line in menu_lines:
        print('{}. {}'.format(line,menu_lines[line][0]))
def wip():
    print('\n{}'.format(app_text[app_settings['language']['value']]['wip']))
def wrong_input():
    print(app_text[app_settings['language']['value']]['err_inp'])
def error_function(err):
    print('{}: {}'.format(app_text[app_settings['language']['value']]['err_func'],err))
def app_info():
    print('\n{} v{}\n{} {} \n\nCLI v{} by {}'.format(user_constants['app_name'],
                                                     user_constants['app_ver'],
                                                     app_text[app_settings['language']['value']]['app_author'],
                                                     user_constants['app_author'],
                                                     app_constants['cli_ver'],
                                                     app_constants['designed_by']))
def clear_screen():
    clear()
    about()
    main_menu()
def settings():
    clear()
    while True:
        about()
        print(app_text[app_settings['language']['value']]['settings'])
        avl_params = {}
        settings_total = {}
        settings_total.update(user_settings)
        settings_total.update(app_settings)
        for id,param in enumerate(settings_total,1):
            avl_params.update({str(id):param})
            val = settings_total[param]['value']
            if settings_total[param].setdefault('setting_type',False)!='hidden':
                if settings_total[param].setdefault('localization',False):
                    if app_text[app_settings['language']['value']].setdefault(param,False):
                        print('{}. {}: {}'.format(id, app_text[app_settings['language']['value']].setdefault(param,app_text[app_settings['language']['value']]['404']), val))
                    else: print('{}. {}: {}'.format(id, user_text[app_settings['language']['value']].setdefault(param,app_text[app_settings['language']['value']]['404']), val))
                else: print('{}. {}: {}'.format(id, param, val))
        print('\n')
        menu(app_menu[app_settings['language']['value']]['back_to_main'])
        line_p('_')
        i = input('{} '.format(app_text[app_settings['language']['value']]['param_name']))
        if i in ['b','B','И','и']:
            clear()
            about()
            main_menu()
            break
        if avl_params.get(i)!=None:
            while True:
                av_p = {}
                j = settings_total[avl_params[i]]
                if j.setdefault('description',False):
                    if app_text[app_settings['language']['value']].setdefault(j['description'],False):
                        print(app_text[app_settings['language']['value']].setdefault(j['description'],app_text[app_settings['language']['value']]['404']))
                    else: print(user_text[app_settings['language']['value']].setdefault(j['description'],app_text[app_settings['language']['value']]['404']))
                if j.setdefault('setting_type','any')=='choose_from_list':
                    for id,p in enumerate(j.setdefault('available_settings',['']),1): av_p.update({str(id):p})
                    print('{} '.format(app_text[app_settings['language']['value']]['settings']))
                    for h in av_p: print('{}. {}'.format(h,av_p[h]))
                line_p('_')
                user_input = input('{} '.format(app_text[app_settings['language']['value']]['param_value']))
                if user_input in ['b','B','И','и']: break
                check = app_input(user_input,j.setdefault('setting_type','any'),
                          j.setdefault('available_settings',['']))
                if check:
                    if j.setdefault('setting_type','any')=='file_adr':
                        j['value'] = user_input
                        break
                    if j.setdefault('setting_type','any')=='file_adr_ex':
                        j['value'] = user_input
                        break
                    if j.setdefault('setting_type','any')=='directory_adr':
                        j['value'] = user_input
                        break
                    if j.setdefault('setting_type','any')=='choose_from_list':
                        j['value'] = av_p[user_input]
                        break
                    if j.setdefault('setting_type','any')=='int':
                        j['value'] = int(user_input)
                        break
                    if j.setdefault('setting_type','any')=='bool':
                        j['value'] = strtobool(user_input)
                        break
                    if j.setdefault('setting_type','any')=='float':
                        j['value'] = float(user_input.replace(',','.'))
                        break
                    if j.setdefault('setting_type','any')=='text':
                        j['value'] = user_input
                        break
                    if j.setdefault('setting_type','any')=='any':
                        j['value'] = user_input
                        break
                else:
                    print(app_text[app_settings['language']['value']]['err_param'])
                    continue
        clear()
        continue
def help_info():
    line_p('_')
    tw_print(user_text[app_settings['language']['value']]['help'])
    #app_info()
    line_block(' CLI v{cli_ver} by {designed_by} '.format(**app_constants))
def quit_program():
    print('\n{}'.format(app_text[app_settings['language']['value']]['q']))
    quit()

user_text = {'RU':{'about': 'Это шаблон для программ на python с консольным интерфейсом)))',
                   'help': 'Здесь хранится справка о программе. Информация о функциях, пунктах меню и порочее.'},
             'EN':{'about': 'This is CLI python template',
                   'help': 'This is info about app, functions, properties etc.'}}

user_constants = {'app_ver':(0.00),
                  'app_name':'Cli template',
                  'app_author':'Somebody'}

user_settings = {'Example option one':{'value':'RU', 'setting_type':'choose_from_list', 'available_settings':['RU'],'localization':True,'description':'desc_example'},
                 'Example option two':{'value':1, 'setting_type':'int','localization':True,'description':'desc_example'}}

user_menu = {'RU':{'main':{1:['Образец пункта меню','Это образец пункта меню'],
                           2:['Образец пункта меню','Это образец пункта меню']}},
             'EN':{'main':{1:['Example option','This is example option description'],
                           2:['Example option','This is example option description']}}}

def functionality_adder(function,function_reaction,menu_line):




    pass


def settings_adder(function,function_reaction,menu_line):




    pass


def app_start(functions_and_values={}):
    #{function:[on what input it react],function2:[on what input it react]}
    about()
    main_menu()
    while True:
        try:
            i = input(app_text[app_settings['language']['value']]['inp'])
            success = False
            for f in functions_and_values:
                if i in functions_and_values[f]:
                    success = True
                    f()
            if i in ['C', 'c', 'С', 'с']:
                success = True
                clear_screen()
            if i in ['S', 's', 'ы', 'Ы']:
                success = True
                settings()
            if i in ['H', 'h', 'р', 'Р']:
                success = True
                help_info()
            if i in ['Q','q','й','Й']:
                success = True
                quit_program()
            if not success:
                wrong_input()
                continue
        except Exception as err:
            error_function(err)
            continue
def example_function():# эта функция обрабатывает функции меню
    line_block(' {} '.format('Образец функции'))


if __name__=='__main__':app_start({example_function:['E','e','у','У']})
