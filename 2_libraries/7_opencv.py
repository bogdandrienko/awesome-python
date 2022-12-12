import time
from concurrent.futures.thread import ThreadPoolExecutor

import httplib2
import numpy
import cv2
import smtplib

class ComputerVisionClass:
    class SoloCamSettingsComputerVisionClassExample:
        """
        Настройки одной камеры для модуля: грохота 16 операции, 10 отметка
        """

        def __init__(self, ip: str, correct: float):
            # Ip address
            self.ip = ip
            # Коэффициент корректировки
            self.correct = round(correct, 3)

    class EventLoopClass:
        @staticmethod
        def loop_modules_global(tick_delay=0.5):
            """
            Цикл прохода по всем модулям-циклам
            """
            try:
                def global_tick():
                    # Начальное время
                    start_time = time.time()
                    # Получение словаря с названиями модулей из константы модели: "ComputerVisionModuleModel"
                    dict_modules = {str(x[0]).strip(): str(x[1]).strip() for x in
                                    backend_models.ComputerVisionModuleModel.get_all_modules()}
                    # Менеджер контекста для многопоточное прохода по всем модулям
                    with ThreadPoolExecutor() as executor:
                        # Получение всех активных модулей
                        modules = backend_models.ComputerVisionModuleModel.objects.filter(play_boolean_field=True)
                        # Получение всех активных модулей
                        if modules:
                            delay = tick_delay
                        else:
                            delay = tick_delay * 5
                        # Цикл прохода по всем активным модулям
                        for module in modules:
                            # Проверка, что цикл модуля отработал в последний раз не позже задержки цикла
                            if module.datetime_field and (module.datetime_field + datetime.timedelta(hours=6)) > \
                                    backend_utils.DateTimeUtils.get_difference_datetime(
                                        seconds=-module.delay_float_field):
                                continue
                            # Получение имени модуля из константы в модели ComputerVisionModuleModel
                            name_module = dict_modules[module.path_slug_field]
                            if name_module == 'Грохота, 16 операция, 10 отметка':
                                executor.submit(ComputerVisionClass.EventLoopClass.Grohota16OperationClass.
                                                loop_module_grohota_16_operation, module=module)
                            elif name_module == 'Грохота, 26 операция, 10 отметка':
                                executor.submit(ComputerVisionClass.EventLoopClass.Grohota16OperationClass.
                                                loop_module_grohota_16_operation, module=module)
                            elif name_module == 'Грохота, 36 операция, 10 отметка':
                                executor.submit(ComputerVisionClass.EventLoopClass.Grohota16OperationClass.
                                                loop_module_grohota_16_operation, module=module)
                    time.sleep(delay)
                    print(f'\n#######################################'
                          f'\n##### {round(time.time() - start_time, 2)} seconds for global_tick ####'
                          f'\n#######################################\n')

                while True:
                    global_tick()
            except Exception as error:
                print(f'\nloop_modules_global | error : {error}\n')
                time.sleep(tick_delay * 10)
                ComputerVisionClass.EventLoopClass.loop_modules_global()

        class Grohota16OperationClass:
            @staticmethod
            def loop_module_grohota_16_operation(module):
                """
                Цикл прохода по компонентам-функциям внутри модуля: Грохота, 16 операция, 10 отметка
                """
                try:
                    # Начальное время
                    start_time = time.time()
                    # Данные из базы с настройками по каждому активному компоненту
                    components = backend_models.ComputerVisionComponentModel.objects.filter(play_boolean_field=True)
                    with ThreadPoolExecutor() as executor:
                        # Цикл для прохода по настройкам и запуску компонентов
                        for component in components:
                            executor.submit(ComputerVisionClass.EventLoopClass.Grohota16OperationClass.
                                            component_grohota_16_operation, component=component)
                    module = backend_models.ComputerVisionModuleModel.objects.get(
                        path_slug_field=module.path_slug_field)
                    module.duration_float_field = round(time.time() - start_time, 2)
                    module.datetime_field = timezone.now()
                    module.save()
                except Exception as error:
                    error_text_field = f'loop_module_grohota_16_operation | {timezone.now()} | error : {error}'
                    module = backend_models.ComputerVisionModuleModel.objects.get(
                        path_slug_field=module.path_slug_field)
                    module.error_text_field = error_text_field
                    module.save()
                    print(f'\n{error_text_field}\n')

            @staticmethod
            def component_grohota_16_operation(component):
                """
                Компонент-функция расчёта % схода на грохотах 16 операции, 10 отметка
                """
                try:
                    # Создание папки с кешем для библиотеки
                    temp_path = backend_utils.DirPathFolderPathClass.create_folder_in_this_dir(
                        folder_name='static/media/data/computer_vision/temp'
                    )
                    # Создание экземпляра объекта библиотеки, установка папки с кешем для библиотеки и таймаута
                    h = httplib2.Http(cache=temp_path, timeout=3)
                    # Установка логина от камеры
                    login = 'admin'
                    # Установка пароля от камеры
                    password = 'q1234567'
                    # Добавление логина и пароля к авторизации
                    h.add_credentials(login, password)
                    # Заполнение api-пути для получения изображения по сети от камеры
                    sources = f'http://{str(component.genericipaddress_field)}:80' \
                              f'/ISAPI/Streaming/channels/101/picture?snapShotImageType=JPEG'
                    # Установка заголовка для запроса
                    headers = {
                        'user-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0',
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
                    }
                    # Получение данных с api камеры
                    response, content = h.request(uri=sources, method="GET", headers=headers)
                    # Чтение изображения-маски
                    mask = cv2.imread(component.mask_char_field, 0)
                    # Превращение массива байтов в массив пикселей и чтение массива в объект-изображение cv2
                    image = cv2.imdecode(numpy.frombuffer(content, numpy.uint8), cv2.IMREAD_COLOR)
                    # Наложение на изображение маски с тёмным режимом: закрашивание участков в чёрный
                    bitwise_and = cv2.bitwise_and(image, image, mask=mask)
                    # Перевод изображения BGR(RGB - для не cv2) в формат HSV
                    cvtcolor = cv2.cvtColor(bitwise_and, cv2.COLOR_BGR2HSV)
                    # Заполнение массива изображения по диапазону с выбранной чувствительностью
                    inrange = cv2.inRange(
                        cvtcolor,
                        numpy.array([0, 0, 255 - 120], dtype=numpy.uint8),
                        numpy.array([255, 120, 255], dtype=numpy.uint8)
                    )
                    # Подсчёт белых пикселей после заполнения к белым пикселям на маске и умножение на коррекцию
                    value = numpy.sum(inrange > 0) / numpy.sum(mask > 0) * 100 * float(1)
                    # Запись результата в базу данных
                    backend_models.LoggingModel.objects.create(
                        username_slug_field='computer vision',
                        ip_genericipaddress_field=component.genericipaddress_field,
                        request_path_slug_field='component_grohota_16_operation',
                        request_method_slug_field='POST',
                        error_text_field=f'value: {round(value, 2)} %'
                    )
                    # value = value/100
                    #
                    # device_row = component.alias_char_field
                    # if value > 30:
                    #     alarm_row = 1
                    # else:
                    #     alarm_row = 0
                    # datetime_row = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
                    # rows = ['device_row', 'value_row', 'alarm_row', 'datetime_row']
                    # values = [device_row, round(value, 2), alarm_row, datetime_row]
                    #
                    # connection = SQLClass.pyodbc_connect(
                    #     ip='192.168.15.122',
                    #     server='WINCC',
                    #     port='49279',
                    #     database='KM_Fabrika',
                    #     username='computer_vision',
                    #     password='vision12345678'
                    # )
                    # cursor = connection.cursor()
                    # cursor.fast_executemany = True
                    # __rows = ''
                    # for x in rows:
                    #     __rows = f"{__rows}{str(x)}, "
                    # query = f"UPDATE {'grohot16_now_table'} SET {rows[1]} = '{values[1]}',{rows[2]} = '{values[2]}' ,
                    # {rows[3]} = '{values[3]}' " \
                    #         f"WHERE {rows[0]} = '{values[0]}'"
                    # cursor.execute(query)
                    # connection.commit()

                    # Вывод результата в консоль
                    print(f'{component.genericipaddress_field} | {component.alias_char_field} : {round(value, 2)} %')
                except Exception as error:
                    print(
                        f'\ncomponent_grohota_16_operation| {component.genericipaddress_field} | '
                        f'{component.alias_char_field} | error : {error}\n')


############################################################################################


class OpenCvClass:
    @staticmethod
    def example_computer_vision():
        # UTILITES
        class LoggingClass:
            @staticmethod
            def logging(message, file_name='log.txt', type_write='a'):
                with open(file_name, type_write) as log:
                    log.write(f'{TimeUtils.get_current_time()} : {message}\n')

        class CopyDictionary:
            @staticmethod
            def get_all_sources(source: dict, values: dict):
                value = source.copy()
                for _key, _value in values.items():
                    value[_key] = _value
                return value

        class FileSettings:
            @staticmethod
            def export_settings(data: dict):
                with open(f"{data['import_file']}.json", 'w') as file:
                    json.dump(data, file)

            @staticmethod
            def import_settings(data: dict):
                try:
                    with open(f"{data['import_file']}.json", "r") as read_file:
                        data = json.load(read_file)
                except Exception as ex:
                    LoggingClass.logging(ex)
                    print(f'import_settings error : {ex}')
                return data

        class TimeUtils:
            @staticmethod
            def get_current_time():
                return f"{time.strftime('%X')}"

        class SendMail:
            @staticmethod
            def sender_email(subject='subj', text='text'):
                host = 'smtp.yandex.ru'
                port = '465'
                login = 'eevee.cycle'
                password = '31284bogdan'
                writer = 'eevee.cycle@yandex.ru'
                recipient = 'eevee.cycle@yandex.ru'

                message = f"""From: {recipient}\nTo: {writer}\nSubject: {subject}\n\n{text}"""

                smtpobj = smtplib.SMTP_SSL(host=host, port=port)
                smtpobj.ehlo()
                smtpobj.login(user=login, password=password)
                smtpobj.sendmail(from_addr=writer, to_addrs=recipient, msg=message)
                smtpobj.quit()

        # SQL
        class SQLClass:
            @staticmethod
            def sql_post_data(ip: str, server: str, port: str, database: str, username: str, password: str, table: str,
                              rows: list, values: list):
                try:
                    sql = SQLClass.pyodbc_connect(ip=ip, server=server, port=port, database=database, username=username,
                                                  password=password)
                    SQLClass.execute_data_query(connection=sql, table=table, rows=rows, values=values)
                except Exception as ex:
                    print(ex)
                    with open('log.txt', 'a') as log:
                        log.write(f'\n{ex}\n')

            @staticmethod
            def sql_post_now(ip: str, server: str, port: str, database: str, username: str, password: str, table: str,
                             rows: list, values: list):
                try:
                    sql = SQLClass.pyodbc_connect(ip=ip, server=server, port=port, database=database, username=username,
                                                  password=password)
                    SQLClass.execute_now_query(connection=sql, table=table, rows=rows, values=values)
                except Exception as ex:
                    print(ex)
                    with open('log.txt', 'a') as log:
                        log.write(f'\n{ex}\n')

            @staticmethod
            def pyodbc_connect(ip: str, server: str, port: str, database: str, username: str, password: str):
                conn_str = (
                        r'DRIVER={ODBC Driver 17 for SQL Server};SERVER=tcp:' + ip + '\\' + server + ',' + port +
                        ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password + ';'
                )
                return pyodbc.connect(conn_str)

            @staticmethod
            def pd_read_sql_query(connection, query: str, database: str, table: str):
                return pandas.read_sql_query(f'{query} {database}.dbo.{table} ORDER BY id', connection)

            @staticmethod
            def execute_data_query(connection, table: str, rows: list, values: list):
                cursor = connection.cursor()
                cursor.fast_executemany = True
                _rows = ''
                for x in rows:
                    _rows = f"{_rows}{str(x)}, "
                value = f"INSERT INTO {table} (" + _rows[:-2:] + f") VALUES {tuple(values)}"
                cursor.execute(value)
                connection.commit()

            @staticmethod
            def execute_now_query(connection, table, rows: list, values: list):
                cursor = connection.cursor()
                cursor.fast_executemany = True
                __rows = ''
                for x in rows:
                    __rows = f"{__rows}{str(x)}, "
                value = f"UPDATE {table} SET {rows[1]} = '{values[1]}',{rows[2]} = '{values[2]}' ,{rows[3]} = '{values[3]}' " \
                        f"WHERE {rows[0]} = '{values[0]}'"
                cursor.execute(value)
                connection.commit()

        # OPENCV
        class AnalyzeClass:
            @staticmethod
            def start_analyze(data: dict):
                sources = AnalyzeClass.get_full_sources(source_type=data['source_type'], sources=data['ip_cam'],
                                                        masks=data['mask_cam'], protocol=data['protocol_cam_type'],
                                                        login=data['login_cam'], password=data['password_cam'],
                                                        port=data['port_cam'], sensitivity=data['sensitivity_analysis'],
                                                        correct=data['correct_coefficient'],
                                                        alias_device=data['alias_device'],
                                                        alarm_level=data['alarm_level'])
                data = CopyDictionary.get_all_sources(data, {'sources': sources})
                if data['compute_debug'] == 'sync':
                    AnalyzeClass.sync_method(data)
                elif data['compute_debug'] == 'async':
                    AnalyzeClass.async_method(data)
                elif data['compute_debug'] == 'multithread':
                    AnalyzeClass.multithread_method(data)
                elif data['compute_debug'] == 'multiprocess':
                    AnalyzeClass.multiprocess_method(data)
                elif data['compute_debug'] == 'complex':
                    AnalyzeClass.complex_method(data)

            @staticmethod
            def sync_method(data: dict):
                while True:
                    if not data['pause']():
                        cv2.destroyAllWindows()
                        break
                    else:
                        for source in data['sources']:
                            AnalyzeClass.analyze(source, data)
                    time.sleep(1 / data['speed_analysis'])

            @staticmethod
            def async_method(data: dict):
                def thread_loop(source):
                    while True:
                        if not data['pause']():
                            cv2.destroyAllWindows()
                            break
                        else:
                            asyncio.run(AnalyzeClass.async_analiz(source, data))
                        time.sleep(1 / data['speed_analysis'])

                for src in data['sources']:
                    threading.Thread(target=thread_loop, args=(src,)).start()

            @staticmethod
            async def async_analiz(source, data: dict):
                image = await AnalyzeClass.async_get_source(data['source_type'], source[0], data['login_cam'],
                                                            data['password_cam'])
                mask = source[1]
                name = source[0].split("192.168.")[1].strip().split(":")[0].strip()
                AnalyzeClass.render_final(image=image, mask=mask,
                                          sensitivity_analysis=source[2],
                                          correct_coefficient=source[3],
                                          name=name,
                                          resolution_debug=data['resolution_debug'])
                cv2.waitKey(round(1000 / data['speed_video_stream']))
                values = AnalyzeClass.result_final(image=image, mask=mask,
                                                   sensitivity_analysis=source[2],
                                                   correct_coefficient=source[3])
                AnalyzeClass.write_result(ip_sql=data['ip_sql'],
                                          server_sql=data['server_sql'],
                                          port_sql=data['port_sql'],
                                          database_sql=data['database_sql'],
                                          user_sql=data['user_sql'],
                                          password_sql=data['password_sql'],
                                          sql_now_check=data['sql_now_check'],
                                          table_now_sql=data['table_now_sql'],
                                          rows_now_sql=data['rows_now_sql'],
                                          sql_data_check=data['sql_data_check'],
                                          table_data_sql=data['table_data_sql'],
                                          rows_data_sql=data['rows_data_sql'],
                                          values=values,
                                          source=name,
                                          widget=data['widget'],
                                          widget_write=data['widget_write'],
                                          text_write=data['text_write'],
                                          sql_val=data['sql_write'],
                                          alarm_level=source[5]
                                          )

            @staticmethod
            async def async_get_source(source_type: str, sources: str, login: str, password: str):
                if source_type == 'image-http':
                    h = httplib2.Http(os.path.abspath('__file__'))
                    h.add_credentials(login, password)
                    response, content = h.request(sources)
                    image = cv2.imdecode(numpy.frombuffer(content, numpy.uint8), cv2.IMREAD_COLOR)
                    return image
                elif source_type == 'video-rtsp' or 'video-file':
                    cam_stream = cv2.VideoCapture(sources)
                    _, image = cam_stream.read()
                    cam_stream.release()
                    return image

            @staticmethod
            def multithread_method(data: dict):
                def thread_loop(source):
                    while True:
                        if not data['pause']():
                            cv2.destroyAllWindows()
                            break
                        else:
                            AnalyzeClass.analyze(source, data)
                        time.sleep(1 / data['speed_analysis'])

                for src in data['sources']:
                    threading.Thread(target=thread_loop, args=(src,)).start()

            @staticmethod
            def multiprocess_method(data: dict):
                def process_loop():
                    while True:
                        if not data['pause']():
                            cv2.destroyAllWindows()
                            break
                        else:
                            with multiprocessing.Pool(data['process_cores']) as process:
                                process.map(AnalyzeClass.multi, _data)
                        time.sleep(1 / data['speed_analysis'])

                _data = []
                for loop in data['sources']:
                    __data = data.copy()
                    del __data['widget']
                    __data['source'] = loop
                    _data.append(__data)
                threading.Thread(target=process_loop).start()

            @staticmethod
            def multi(kwargs):
                source = kwargs['source']
                kwargs['widget'] = None
                AnalyzeClass.analyze(source, kwargs)

            @staticmethod
            def complex_method(data: dict):
                def thread_loop(source):
                    while True:
                        if not data['pause']():
                            cv2.destroyAllWindows()
                            break
                        else:
                            asyncio.run(AnalyzeClass.async_complex_analiz(source, data))
                        time.sleep(1 / data['speed_analysis'])

                for src in data['sources']:
                    threading.Thread(target=thread_loop, args=(src,)).start()

            @staticmethod
            async def async_complex_analiz(source, data: dict):
                try:
                    image = await AnalyzeClass.async_get_source(data['source_type'], source[0], data['login_cam'],
                                                                data['password_cam'])
                    mask = source[1]
                    name = source[4]
                    if data['render_debug'] == 'all':
                        AnalyzeClass.render_flip(image=image, flipcode=0, name=name,
                                                 resolution_debug=data['resolution_debug'])
                        AnalyzeClass.render_cvtcolor(image=image, color_type=cv2.COLOR_RGB2GRAY, name=name,
                                                     resolution_debug=data['resolution_debug'])
                        AnalyzeClass.render_shapes(name=name, resolution_debug=data['resolution_debug'])
                        AnalyzeClass.render_origin(image=image, name=name,
                                                   resolution_debug=data['resolution_debug'])
                        AnalyzeClass.render_cropping_image(image=image, name=name,
                                                           resolution_debug=data['resolution_debug'])
                        AnalyzeClass.render_bitwise_and(image=image, mask=mask, name=name,
                                                        resolution_debug=data['resolution_debug'])
                        AnalyzeClass.render_bitwise_not_white(image=image, mask=mask, name=name,
                                                              resolution_debug=data['resolution_debug'])
                        AnalyzeClass.render_cvtcolor_to_hsv(image=image, name=name,
                                                            resolution_debug=data['resolution_debug'])
                        AnalyzeClass.render_threshold(image=image, name=name,
                                                      resolution_debug=data['resolution_debug'])
                        AnalyzeClass.render_inrange(image=image, sensitivity_analysis=source[2],
                                                    name=name,
                                                    resolution_debug=data['resolution_debug'])
                        AnalyzeClass.render_canny_edges(image=image,
                                                        sensitivity_analysis=source[2],
                                                        name=name,
                                                        resolution_debug=data['resolution_debug'])
                        AnalyzeClass.render_final(image=image, mask=mask,
                                                  sensitivity_analysis=source[2],
                                                  correct_coefficient=source[3],
                                                  name=name,
                                                  resolution_debug=data['resolution_debug'])
                    elif data['render_debug'] == 'extended':
                        AnalyzeClass.render_origin(image=image, name=name,
                                                   resolution_debug=data['resolution_debug'])
                        AnalyzeClass.render_inrange(image=image, sensitivity_analysis=source[2],
                                                    name=name,
                                                    resolution_debug=data['resolution_debug'])
                        AnalyzeClass.render_final(image=image, mask=mask,
                                                  sensitivity_analysis=source[2],
                                                  correct_coefficient=source[3],
                                                  name=name,
                                                  resolution_debug=data['resolution_debug'])
                    elif data['render_debug'] == 'final':
                        AnalyzeClass.render_final(image=image, mask=mask,
                                                  sensitivity_analysis=source[2],
                                                  correct_coefficient=source[3],
                                                  name=name,
                                                  resolution_debug=data['resolution_debug'])
                    elif data['render_debug'] == 'source':
                        AnalyzeClass.render_origin(image=image, name=name,
                                                   resolution_debug=data['resolution_debug'])
                    cv2.waitKey(round(1000 / data['speed_video_stream']))
                    values = AnalyzeClass.result_final(image=image, mask=mask,
                                                       sensitivity_analysis=source[2],
                                                       correct_coefficient=source[3])
                    AnalyzeClass.write_result(ip_sql=data['ip_sql'],
                                              server_sql=data['server_sql'],
                                              port_sql=data['port_sql'],
                                              database_sql=data['database_sql'],
                                              user_sql=data['user_sql'],
                                              password_sql=data['password_sql'],
                                              sql_now_check=data['sql_now_check'],
                                              table_now_sql=data['table_now_sql'],
                                              rows_now_sql=data['rows_now_sql'],
                                              sql_data_check=data['sql_data_check'],
                                              table_data_sql=data['table_data_sql'],
                                              rows_data_sql=data['rows_data_sql'],
                                              values=values,
                                              source=name,
                                              widget=data['widget'],
                                              widget_write=data['widget_write'],
                                              text_write=data['text_write'],
                                              sql_val=data['sql_write'],
                                              alarm_level=source[5])
                except Exception as ex:
                    LoggingClass.logging(ex)
                    print(f'analyze func error')
                    print(ex)
                    # SendMail.sender_email(subject='error', text='analyze func error')

            @staticmethod
            def analyze(source, data: dict):
                try:
                    image = AnalyzeClass.get_source(data['source_type'], source[0], data['login_cam'],
                                                    data['password_cam'])
                    mask = source[1]
                    name = source[0].split("192.168.")[1].strip().split(":")[0].strip()
                    if data['render_debug'] == 'all':
                        AnalyzeClass.render_origin(image=image, name=name,
                                                   resolution_debug=data['resolution_debug'])
                        AnalyzeClass.render_cropping_image(image=image, name=name,
                                                           resolution_debug=data['resolution_debug'])
                        AnalyzeClass.render_bitwise_and(image=image, mask=mask, name=name,
                                                        resolution_debug=data['resolution_debug'])
                        AnalyzeClass.render_bitwise_not_white(image=image, mask=mask, name=name,
                                                              resolution_debug=data['resolution_debug'])
                        AnalyzeClass.render_cvtcolor_to_hsv(image=image, name=name,
                                                            resolution_debug=data['resolution_debug'])
                        AnalyzeClass.render_threshold(image=image, name=name,
                                                      resolution_debug=data['resolution_debug'])
                        AnalyzeClass.render_inrange(image=image, sensitivity_analysis=source[2],
                                                    name=name,
                                                    resolution_debug=data['resolution_debug'])
                        AnalyzeClass.render_canny_edges(image=image,
                                                        sensitivity_analysis=source[2],
                                                        name=name,
                                                        resolution_debug=data['resolution_debug'])
                        AnalyzeClass.render_final(image=image, mask=mask,
                                                  sensitivity_analysis=source[2],
                                                  correct_coefficient=source[3],
                                                  name=name,
                                                  resolution_debug=data['resolution_debug'])
                    elif data['render_debug'] == 'extended':
                        AnalyzeClass.render_origin(image=image, name=name,
                                                   resolution_debug=data['resolution_debug'])
                        AnalyzeClass.render_inrange(image=image, sensitivity_analysis=source[2],
                                                    name=name,
                                                    resolution_debug=data['resolution_debug'])
                        AnalyzeClass.render_final(image=image, mask=mask,
                                                  sensitivity_analysis=source[2],
                                                  correct_coefficient=source[3],
                                                  name=name,
                                                  resolution_debug=data['resolution_debug'])
                    elif data['render_debug'] == 'final':
                        AnalyzeClass.render_final(image=image, mask=mask,
                                                  sensitivity_analysis=source[2],
                                                  correct_coefficient=source[3],
                                                  name=name,
                                                  resolution_debug=data['resolution_debug'])
                    elif data['render_debug'] == 'source':
                        AnalyzeClass.render_origin(image=image, name=name,
                                                   resolution_debug=data['resolution_debug'])
                    cv2.waitKey(round(1000 / data['speed_video_stream']))
                    values = AnalyzeClass.result_final(image=image, mask=mask,
                                                       sensitivity_analysis=source[2],
                                                       correct_coefficient=source[3])
                    AnalyzeClass.write_result(
                        ip_sql=data['ip_sql'],
                        server_sql=data['server_sql'],
                        port_sql=data['port_sql'],
                        database_sql=data['database_sql'],
                        user_sql=data['user_sql'],
                        password_sql=data['password_sql'],
                        sql_now_check=data['sql_now_check'],
                        table_now_sql=data['table_now_sql'],
                        rows_now_sql=data['rows_now_sql'],
                        sql_data_check=data['sql_data_check'],
                        table_data_sql=data['table_data_sql'],
                        rows_data_sql=data['rows_data_sql'],
                        values=values,
                        source=name,
                        widget=data['widget'],
                        widget_write=data['widget_write'],
                        text_write=data['text_write'],
                        sql_val=data['sql_write'],
                        alarm_level=source[5]
                    )
                except Exception as ex:
                    LoggingClass.logging(ex)
                    print(f'{TimeUtils.get_current_time()} : analyze func error')
                    print(ex)

            @staticmethod
            def get_full_sources(source_type: str, sources: list, masks: list, protocol: str, login: str, password: str,
                                 port: int, sensitivity: list, correct: list, alias_device: list, alarm_level: list):
                try:
                    _sources = []
                    for x in sources:
                        index = sources.index(x)
                        if source_type == 'image-http':
                            _sources.append([f'{protocol}://192.168.{x}:{port}/ISAPI/Streaming/channels/101/'
                                             f'picture?snapShotImageType=JPEG', cv2.imread(masks[index], 0),
                                             sensitivity[index], correct[index], alias_device[index],
                                             alarm_level[index]])
                        elif source_type == 'video-rtsp':
                            _sources.append(
                                [f'{protocol}://{login}:{password}@192.168.{x}:{port}', cv2.imread(masks[index], 0),
                                 sensitivity[index], correct[index], alias_device[index], alarm_level[index]])
                        elif source_type == 'video-file':
                            _sources.append([f'{x}', cv2.imread(masks[index], 0), sensitivity[index], correct[index],
                                             alias_device[index], alarm_level[index]])
                    return _sources
                except Exception as ex:
                    LoggingClass.logging(ex)
                    print(f'get_full_sources error : {ex}')

            @staticmethod
            def get_source(source_type: str, sources: str, login: str, password: str):
                try:
                    if source_type == 'image-http':
                        h = httplib2.Http("/path/to/cache-directory")
                        h.add_credentials(login, password)
                        response, content = h.request(sources)
                        image = cv2.imdecode(numpy.frombuffer(content, numpy.uint8), cv2.IMREAD_COLOR)
                        return image
                    elif source_type == 'video-rtsp' or 'video-file':
                        cam_stream = cv2.VideoCapture(sources)
                        _, image = cam_stream.read()
                        cam_stream.release()
                        return image
                except Exception as ex:
                    LoggingClass.logging(ex)
                    print(f'get_source func error')
                    print(ex)

            @staticmethod
            def render_origin(image, name, resolution_debug):
                AnalyzeClass.render(name=f"origin : {name}", source=image, resolution_debug=resolution_debug)

            @staticmethod
            def render_cropping_image(image, name, resolution_debug):
                cropping_image = image[250:1080, 600:1720]
                AnalyzeClass.render(name=f"cropping_image : {name}", source=cropping_image,
                                    resolution_debug=resolution_debug)

            @staticmethod
            def render_bitwise_not_white(image, mask, name, resolution_debug):
                bitwise_not = cv2.bitwise_not(image, image, mask=mask)
                AnalyzeClass.render(name=f"_bitwise_not_white : {name}", source=bitwise_not,
                                    resolution_debug=resolution_debug)

            @staticmethod
            def render_bitwise_and(image, mask, name, resolution_debug):
                bitwise_and = cv2.bitwise_and(image, image, mask=mask)
                AnalyzeClass.render(name=f"bitwise_and : {name}", source=bitwise_and, resolution_debug=resolution_debug)

            @staticmethod
            def render_threshold(image, name, resolution_debug):
                _, threshold = cv2.threshold(image, 220, 255, cv2.THRESH_BINARY_INV)
                AnalyzeClass.render(name=f"threshold : {name}", source=threshold, resolution_debug=resolution_debug)

            @staticmethod
            def render_cvtcolor_to_hsv(image, name, resolution_debug):
                cvtcolor = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
                AnalyzeClass.render(name=f"cvtcolor_to_hsv : {name}", source=cvtcolor,
                                    resolution_debug=resolution_debug)

            @staticmethod
            def render_inrange(image, sensitivity_analysis, name, resolution_debug):
                cvtcolor = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
                inrange = cv2.inRange(cvtcolor, numpy.array([0, 0, 255 - sensitivity_analysis], dtype=numpy.uint8),
                                      numpy.array([255, sensitivity_analysis, 255], dtype=numpy.uint8))
                AnalyzeClass.render(name=f"inrange : {name}", source=inrange, resolution_debug=resolution_debug)

            @staticmethod
            def render_canny_edges(image, sensitivity_analysis, name, resolution_debug):
                canny = cv2.Canny(image, sensitivity_analysis, sensitivity_analysis, apertureSize=3, L2gradient=True)
                AnalyzeClass.render(name=f"canny_edges : {name}", source=canny, resolution_debug=resolution_debug)

            @staticmethod
            def render_shapes(name, resolution_debug):
                red = (0, 0, 255)
                green = (0, 255, 0)
                blue = (255, 0, 0)
                yellow = (0, 255, 255)
                numpy.set_printoptions(threshold=0)
                img = numpy.zeros(shape=(512, 512, 3), dtype=numpy.uint8)
                cv2.line(
                    img=img,
                    pt1=(0, 0),
                    pt2=(311, 511),
                    color=blue,
                    thickness=10
                )
                cv2.rectangle(
                    img=img,
                    pt1=(30, 166),
                    pt2=(130, 266),
                    color=green,
                    thickness=3
                )
                cv2.circle(
                    img=img,
                    center=(222, 222),
                    radius=50,
                    color=(255.111, 111),
                    thickness=-1
                )
                cv2.ellipse(
                    img=img,
                    center=(333, 333),
                    axes=(50, 20),
                    angle=0,
                    startAngle=0,
                    endAngle=150,
                    color=red,
                    thickness=-1
                )
                pts = numpy.array(
                    [[10, 5], [20, 30], [70, 20], [50, 10]],
                    dtype=numpy.int32
                )
                pts = pts.reshape((-1, 1, 2,))
                cv2.polylines(
                    img=img,
                    pts=[pts],
                    isClosed=True,
                    color=yellow,
                    thickness=5
                )
                cv2.putText(
                    img=img,
                    text="SOL",
                    org=(10, 400),
                    fontFace=cv2.FONT_ITALIC,
                    fontScale=3.5,
                    color=(255, 255, 255),
                    thickness=2
                )
                AnalyzeClass.render(name=f"shapes : {name}", source=img, resolution_debug=resolution_debug)

            @staticmethod
            def render_cvtcolor(image, color_type, name, resolution_debug):
                cvtcolor = cv2.cvtColor(image, color_type)
                AnalyzeClass.render(name=f"cvtcolor : {name}", source=cvtcolor, resolution_debug=resolution_debug)

            @staticmethod
            def render_flip(image, flipcode, name, resolution_debug):
                flip = cv2.flip(image, flipcode)
                AnalyzeClass.render(name=f"flip : {name}", source=flip, resolution_debug=resolution_debug)

            @staticmethod
            def render_final(image, mask, sensitivity_analysis, correct_coefficient, name, resolution_debug):
                bitwise_and = cv2.bitwise_and(image, image, mask=mask)
                cvtcolor = cv2.cvtColor(bitwise_and, cv2.COLOR_BGR2HSV)
                inrange = cv2.inRange(cvtcolor, numpy.array([0, 0, 255 - sensitivity_analysis], dtype=numpy.uint8),
                                      numpy.array([255, sensitivity_analysis, 255], dtype=numpy.uint8))
                cv2.putText(inrange,
                            f"{numpy.sum(inrange > 0) / numpy.sum(mask > 0) * 100 * correct_coefficient:0.2f}%",
                            (int(1920 / 5), int(1080 / 2)), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 255, 255), 3)
                AnalyzeClass.render(name=f"final : {name}", source=inrange, resolution_debug=resolution_debug)

            @staticmethod
            def render(name: str, source, resolution_debug: list):
                try:
                    if source is not None:
                        img = cv2.resize(source, (resolution_debug[0], resolution_debug[1]),
                                         interpolation=cv2.INTER_AREA)
                        cv2.imshow(name, img)
                except Exception as ex:
                    LoggingClass.logging(ex)
                    print(ex)

            @staticmethod
            def result_final(image, mask, sensitivity_analysis, correct_coefficient):
                bitwise_and = cv2.bitwise_and(image, image, mask=mask)
                cvtcolor = cv2.cvtColor(bitwise_and, cv2.COLOR_BGR2HSV)
                inrange = cv2.inRange(cvtcolor, numpy.array([0, 0, 255 - sensitivity_analysis], dtype=numpy.uint8),
                                      numpy.array([255, sensitivity_analysis, 255], dtype=numpy.uint8))
                try:
                    return round(numpy.sum(inrange > 0) / numpy.sum(mask > 0) * 100 * correct_coefficient, 2)
                except Exception as ex:
                    LoggingClass.logging(ex)
                    print(f'result_final func error : {ex}')
                    return 0.0

            @staticmethod
            def write_result(ip_sql: str, server_sql: str, port_sql: str, database_sql: str, user_sql: str,
                             password_sql: str,
                             sql_now_check: bool, table_now_sql: str, rows_now_sql: list, sql_data_check: bool,
                             table_data_sql: str, rows_data_sql: list, source: str, values: float, widget,
                             widget_write: bool,
                             text_write: bool, sql_val: bool, alarm_level: int):
                sql_datetime = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
                boolean = 0
                if values > alarm_level:
                    boolean = 1
                _values = [source, values, boolean, sql_datetime]
                if widget_write:
                    try:
                        widget(f'{_values}')
                    except Exception as ex:
                        LoggingClass.logging(ex)
                        print(ex)
                if text_write:
                    try:
                        with open('db.txt', 'a') as db:
                            db.write(f'{_values}\n')
                    except Exception as ex:
                        LoggingClass.logging(ex)
                        print(ex)
                if sql_val:
                    try:
                        if sql_now_check:
                            SQLClass.sql_post_now(ip=ip_sql, server=server_sql, port=port_sql, database=database_sql,
                                                  username=user_sql, password=password_sql, table=table_now_sql,
                                                  rows=rows_now_sql, values=_values)
                        if sql_data_check:
                            SQLClass.sql_post_data(ip=ip_sql, server=server_sql, port=port_sql, database=database_sql,
                                                   username=user_sql, password=password_sql, table=table_data_sql,
                                                   rows=rows_data_sql, values=_values)
                    except Exception as ex:
                        LoggingClass.logging(ex)
                        print(ex)

            @staticmethod
            def make_snapshot(data: dict):
                h = httplib2.Http("/path/to/cache-directory")
                h.add_credentials(name=data['login_cam'], password=data['password_cam'])
                sources = f"{data['protocol_cam_type']}://192.168.{data['ip_cam_snapshot']}:{data['port_cam']}/" \
                          f"ISAPI/Streaming/channels/101/picture?snapShotImageType=JPEG"
                response, content = h.request(sources)
                with open(data["name_snapshot"], 'wb') as file:
                    file.write(content)
                # cv2.imwrite('1.png', img, [int(cv2.IMWRITE_JPEG_QUALITY), 95])
                # cv2.imwrite('1.png', img, [int(cv2.IMWRITE_PNG_COMPRESSION), 9])

            @staticmethod
            def play_rtsp():
                cap = cv2.VideoCapture('rtsp://admin:q1234567@192.168.15.229:554/cam/realmonitor?channel=1&subtype=0')
                # cap = cv2.VideoCapture('rtsp://admin:nehrfvths123@192.168.15.140:554')
                # cap = cv2.VideoCapture('rtsp://192.168.15.229:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif')
                # cap = cv2.VideoCapture('rtsp://192.168.15.229:554/live')
                # cap = cv2.VideoCapture('rtsp://admin:q1234567@192.168.15.229:554/cam/realmonitor?channel=2&subtype=1')
                # cap = cv2.VideoCapture('rtsp://admin:q1234567@192.168.15.229:554/cam/realmonitor?channel=33&subtype=0')
                # sources = f"http://192.168.15.227/cgi-bin/snapshot.cgi?channel=road?loginuse=admin&loginpas=q1234567"
                # sources = f"http://192.168.15.227/cgi-bin/snapshot.cgi?loginuse=admin&loginpas=q1234567"
                # sources = f"http://192.168.15.227/cgi-bin/snapshot.cgi?chn=1&u=admin&p=q1234567"
                # sources = f"http://192.168.15.227/cgi-bin/snapshot.cgi?1"
                # sources = f"rtsp://192.168.15.227:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif"
                # sources = f"rtsp://192.168.15.227:554/live"
                # sources = f"rtsp://admin:q1234567@192.168.15.227:554/cam/realmonitor?channel=1&subtype=1"
                # sources = f"rtsp://admin:q1234567@192.168.15.227:554/cam/realmonitor?channel=1&subtype=0"
                # sources = f"rtsp://admin:nehrfvths123@192.168.15.140:554"
                while True:
                    try:
                        ret, frame = cap.read()
                        cv2.imshow("Capturing", frame)
                        if cv2.waitKey(1) & 0xFF == ord('q'):
                            break
                    except Exception as ex:
                        print(ex)
                cv2.destroyAllWindows()
                cap.release()

########################################################################################################################

# прочитать изображение в память (подать путь к изображению - от пользователя) - чтение с диска
# выдать данных об изображении
# обработка изображения (подать все нужные параметры - от пользователя)
# выдать данных об итоговом изображении
# запись (сохранение результата) - перезапись/или сохранить как

import sys
import time
from PySide6.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QGridLayout, QCheckBox, QPushButton, QSlider, \
    QComboBox
import cv2  # pip install opencv-python


class MainWindow(QWidget):  # MainWindow - класс наследник(дочерний) от класса QWidget(родитель)
    def __init__(self, width=640, height=480, title="title"):
        QWidget.__init__(self)  # тут происходит вызов конструктора для родителя

        self.setWindowTitle(title)
        self.resize(width, height)

        self.image_data = None

        # layout = QVBoxLayout()
        # self.setLayout(layout)
        #
        # self.line_edit = QLineEdit()
        # layout.addWidget(self.line_edit)
        #
        # self.line_edit1 = QLineEdit()
        # layout.addWidget(self.line_edit1)
        #
        # self.label = QLabel()
        # layout.addWidget(self.label)

        self.layout = QGridLayout()  # экземпляр класса интерфейса grid(сетка)
        self.setLayout(self.layout)  # вкладываем QGridLayout -> MainWindow(QWidget)

        self.label_path = QLabel('Путь к файлу: ')  # экзампляр строки текста
        self.layout.addWidget(self.label_path, 1, 1)

        self.line_edit_path = QLineEdit('image_data/dino.jpg')  # экзампляр строки ввода текста
        self.layout.addWidget(self.line_edit_path, 2, 1)  # вкладываем QLineEdit -> QGridLayout

        self.label_check = QLabel('Статус: ')  # экзампляр строки текста
        self.layout.addWidget(self.label_check, 1, 2)

        self.check_box_status = QCheckBox()  # экзампляр чек бокса
        self.check_box_status.setChecked(False)
        self.layout.addWidget(self.check_box_status, 2, 2)  # вкладываем QCheckBox -> QGridLayout

        self.push_button_check = QPushButton('проверить наличие файла')  # экзампляр строки ввода текста
        self.push_button_check.clicked.connect(self.read_and_check_image_in_path)
        # self.push_button_check.setGeometry(QtCore.QRect(200, 150, 93, 28))
        self.layout.addWidget(self.push_button_check, 2, 3)  # вкладываем QLineEdit -> QGridLayout

        self.label_width = QLabel('Ширина: ')
        self.layout.addWidget(self.label_width, 3, 1)

        self.label_height = QLabel('Высота: ')
        self.layout.addWidget(self.label_height, 3, 2)

        self.line_edit_width = QLineEdit('0')  # экзампляр строки ввода текста
        self.layout.addWidget(self.line_edit_width, 4, 1)  # вкладываем QLineEdit -> QGridLayout

        self.line_edit_height = QLineEdit('0')  # экзампляр строки ввода текста
        self.layout.addWidget(self.line_edit_height, 4, 2)  # вкладываем QLineEdit -> QGridLayout

        self.check_box_wb = QCheckBox()  # экзампляр чек бокса
        self.check_box_wb.setChecked(False)
        self.layout.addWidget(self.check_box_wb, 5, 1)  # вкладываем QCheckBox -> QGridLayout

        self.label_check_wb = QLabel('сделать чёрно-белым: ')  # экзампляр строки текста
        self.layout.addWidget(self.label_check_wb, 5, 2)

        self.check_box_protect = QCheckBox()  # экзампляр чек бокса
        self.check_box_protect.setChecked(False)
        self.check_box_protect.stateChanged.connect(self.protect)
        self.layout.addWidget(self.check_box_protect, 5, 3)  # вкладываем QCheckBox -> QGridLayout

        self.label_check_box_protect = QLabel('подтвердить изменения: ')  # экзампляр строки текста
        self.layout.addWidget(self.label_check_box_protect, 5, 4)

        # self.slider_quality = QSlider(Qt.Horizontal)
        self.slider_quality = QSlider()
        self.slider_quality.setMinimum(1)
        self.slider_quality.setMaximum(100)
        self.slider_quality.setValue(95)
        self.layout.addWidget(self.slider_quality, 4, 5)

        self.label_slider_quality = QLabel('качество: ')  # экзампляр строки текста
        self.layout.addWidget(self.label_slider_quality, 5, 5)

        self.label_1 = QLabel('')
        self.layout.addWidget(self.label_1, 6, 1)

        self.push_button_start = QPushButton('выполнить')  # экзампляр строки ввода текста
        self.push_button_start.clicked.connect(self.start)
        self.push_button_start.setEnabled(False)
        # self.push_button_check.setGeometry(QtCore.QRect(200, 150, 93, 28))
        self.layout.addWidget(self.push_button_start, 7, 1)  # вкладываем QLineEdit -> QGridLayout

        self.push_button_stop = QPushButton('отменить')  # экзампляр строки ввода текста
        self.push_button_stop.clicked.connect(self.stop)
        # self.push_button_check.setGeometry(QtCore.QRect(200, 150, 93, 28))
        self.layout.addWidget(self.push_button_stop, 7, 3)  # вкладываем QLineEdit -> QGridLayout

        self.combo_box_filter = QComboBox()
        self.combo_box_filter.addItem("гаусс")
        self.combo_box_filter.addItem("фильтр 2")
        self.combo_box_filter.addItems(["фильтр 3", "фильтр 4", "фильтр 5"])

        self.layout.addWidget(self.combo_box_filter, 7, 4)  # вкладываем QComboBox -> QGridLayout

        # self.line_edit1 = QLineEdit()  # экзампляр строки ввода текста
        # self.layout2.addWidget(self.line_edit1)  # вкладываем QLineEdit -> QGridLayout
        #
        # self.line_edit2 = QLineEdit()  # экзампляр строки ввода текста
        # self.layout2.addWidget(self.line_edit2, 2, 2)  # вкладываем QLineEdit -> QGridLayout

        # self.line_edit3 = self.render_line_edit(self.layout2, '111111111', 2, 2)

        # self.line_edit3 = QLineEdit()  # экзампляр строки ввода текста
        # self.layout2.addWidget(self.line_edit3)  # вкладываем QLineEdit -> QGridLayout

        # self.line_edit.textChanged.connect(self.line_edit_text_changed)

        def delay(seconds: float):
            time.sleep(seconds)
            # тут код(поток исполнения)
            self.show()
        delay(0.5)
        # self.show()

    def read_and_check_image_in_path(self):

        value = self.line_edit_path.text()
        print(value)

        # тут мы будем проверять наличие файла по пути в строке

        # opencv
        # self.image_data = пиксели

        # C:\Project\Github_Projects\PyE-221-1\dino.jpg - абсолютный
        # dino.jpg - относительный
        # img1 = cv2.imread(value, cv2.IMREAD_GRAYSCALE)  # читаем изображение по пути, с флагом для серого
        # cv2.imshow('dino_window1', img1)  # рендерит(отрисовывает на экране) массив пикселей - изображение

        try:
            img2 = cv2.imread(value, cv2.IMREAD_COLOR)  # читаем изображение по пути, с флагом для цветного
        except Exception as error:
            print(error)
            img2 = []

        print(img2)
        print(len(img2))
        print(type(img2))

        if len(img2) > 0:  # [] - False, [''] - True, '' - False, '1' - True
            cv2.imshow('dino_window2', img2)  # рендерит(отрисовывает на экране) массив пикселей - изображение
            cv2.waitKey(1)  # для задержки отображения кадра (если изображение, то нужен параметр 1)
            # cv2.imwrite('dino2.jpg', img)

            has_file = True
            print('изображение успешно прочитано')

            self.image_data = img2
            print(self.image_data.shape)
            # height, width = self.image_data.shape[:2]  # -> (1920, 1080)
            height, width, channels = self.image_data.shape  # -> (1920, 1080, 3)

            self.line_edit_width.setText(str(width))
            self.line_edit_height.setText(str(height))

        else:
            has_file = False
            print('изображение не прочитано!')

            self.line_edit_width.setText("0")
            self.line_edit_height.setText("0")

        self.check_box_status.setChecked(has_file)

        # self.push_button_check.hide()  # прятать элемент интерфейса

    def start(self):
        print("start")

        # combo = self.combo_box_filter.itemText(3)
        combo = self.combo_box_filter.currentText()
        print(combo)

        white_black = bool(self.check_box_wb.isChecked())

        quality = int(self.slider_quality.value())
        width = int(self.line_edit_width.text())
        height = int(self.line_edit_height.text())

        image = self.image_data
        print(type(image))

        if white_black:
            image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # BGR(RGB) -> GRAY
            image = cv2.threshold(image_gray, 127, 255, cv2.THRESH_BINARY)[1]  # GRAY -> WHITE

        # value = 100  # 0 -> 255
        # if value > 127:
        #     value = 1
        # else:
        #     value = 0

        image = cv2.resize(image, (width, height))

        # 0 200 400
        #  150 250
        # image = image[150:250:1]  # обрезка

        cv2.imwrite("image_data/dino_new.jpg", image, [cv2.IMWRITE_JPEG_QUALITY, quality])

    def stop(self):
        print("stop")
        pass

    def protect(self):
        self.push_button_start.setEnabled(self.check_box_protect.isChecked())

    def render_line_edit(self, parent, default="", row=1, col=1):
        new = QLineEdit(default)
        parent.addWidget(new, row, col)
        return new

    def create_line_edit(self):
        self.layout.addWidget(QLineEdit())
        return

    # def line_edit_text_changed(self, text):
    #     try:
    #         text = round(course_dollar * float(text), 3)
    #         self.label.setText("Ваша сумма: " + str(text) + " $")
    #     except Exception as error:
    #         self.label.setText('ошибка ввода данных')


app = QApplication(sys.argv)
mw = MainWindow(640, 480, 'image analyse')  # создаём инстанс (экземпляр) класса
# пока класс не умрёт, эта часть кода не затронется
app.exec()  # очистка памяти

app1 = QApplication(sys.argv)
app1.exec()

########################################################################################################################


@staticmethod
def example_cv():
    class AppContainerClass:
        def __init__(self):
            self.app = QtWidgets.QApplication([])
            self.widget = None

        def create_ui(self, title, width, height, icon, play_f, stop_f, quit_f, snapshot_f):
            self.widget = MainWidgetClass(title, width, height, icon, play_f, stop_f, quit_f, snapshot_f)
            return self.widget

        @staticmethod
        def create_qlable(text: str, _parent, background=False):
            _widget = QtWidgets.QLabel(text)
            if background:
                _widget.setAutoFillBackground(True)
                _widget.setStyleSheet("QLabel { background-color: rgba(0, 0, 0, 255); color : white; }")
            _parent.addWidget(_widget)
            return _widget

        @staticmethod
        def create_qpushbutton(_parent, _connect_func, _text='set'):
            _widget = QtWidgets.QPushButton(_text)
            _parent.addWidget(_widget)
            _widget.clicked.connect(_connect_func)
            return _widget

        @staticmethod
        def create_qcheckbox(_parent, _text='check?', default=False):
            _widget = QtWidgets.QCheckBox(_text)
            _widget.setChecked(default)
            _parent.addWidget(_widget)
            return _widget

        @staticmethod
        def create_qcombobox(_parent, _text: list, default=None):
            _widget = QtWidgets.QComboBox()
            _widget.addItems([x for x in _text])
            _widget.setCurrentText(default)
            _parent.addWidget(_widget)
            return _widget

        @staticmethod
        def create_qradiobutton(_parent, _text: str, default=False):
            _widget = QtWidgets.QRadioButton(_text)
            _widget.setChecked(default)
            _parent.addWidget(_widget)
            return _widget

    class MainWidgetClass(QtWidgets.QWidget):
        def __init__(self, title="APP", width=640, height=480, icon="", play_f=None, stop_f=None, quit_f=None,
                     snapshot_f=None):
            super().__init__()

            self.play_f = play_f
            self.snapshot_f = snapshot_f
            self.resize(width, height)
            self.setWindowTitle(title)
            self.setWindowIcon(QtGui.QIcon(icon))
            self.resolution_debug = []
            self.v_layout_m = QtWidgets.QVBoxLayout(self)

            # MANAGEMENT
            self.h_layout_g_management = QtWidgets.QHBoxLayout()
            self.v_layout_m.addLayout(self.h_layout_g_management)
            self.g_management_set = AppContainerClass.create_qlable('MANAGEMENT', self.h_layout_g_management,
                                                                    background=True)
            self.h_layout_management_1 = QtWidgets.QHBoxLayout()
            self.v_layout_m.addLayout(self.h_layout_management_1)
            self.play_QPushButton = AppContainerClass.create_qpushbutton(self.h_layout_management_1,
                                                                         self.play_btn_func,
                                                                         'play')
            self.stop_QPushButton = AppContainerClass.create_qpushbutton(self.h_layout_management_1, stop_f, 'stop')
            self.quit_QPushButton = AppContainerClass.create_qpushbutton(self.h_layout_management_1, quit_f, 'quit')
            # CAMERAS
            self.h_layout_g_cam = QtWidgets.QHBoxLayout()
            self.v_layout_m.addLayout(self.h_layout_g_cam)
            self.g_cam_set = AppContainerClass.create_qlable('CAMERAS', self.h_layout_g_cam, background=True)
            self.h_layout_cam_1 = QtWidgets.QHBoxLayout()
            self.v_layout_m.addLayout(self.h_layout_cam_1)
            self.protocol_cam_type = AppContainerClass.create_qlable('PROTOCOL TYPE : http', self.h_layout_cam_1)
            self.set_protocol_cam_type = AppContainerClass.create_qpushbutton(self.h_layout_cam_1,
                                                                              self.get_protocol_cam_type_button)
            self.port_cam = AppContainerClass.create_qlable('PORT CAM : 80', self.h_layout_cam_1)
            self.set_port_cam = AppContainerClass.create_qpushbutton(self.h_layout_cam_1, self.get_port_cam_button)
            self.login_cam = AppContainerClass.create_qlable('LOGIN CAM : admin', self.h_layout_cam_1)
            self.set_login_cam = AppContainerClass.create_qpushbutton(self.h_layout_cam_1,
                                                                      self.get_login_cam_button)
            self.password_cam = AppContainerClass.create_qlable('PASSWORD CAM : q1234567', self.h_layout_cam_1)
            self.set_password_cam = AppContainerClass.create_qpushbutton(self.h_layout_cam_1,
                                                                         self.get_password_cam_button)
            self.h_layout_cam_2 = QtWidgets.QHBoxLayout()
            self.v_layout_m.addLayout(self.h_layout_cam_2)
            self.alias_device = AppContainerClass.create_qlable(
                'ALIAS DEVICE : 16/1 | 16/2 | 16/3 | 16/4 | 16/5 | 16/6 '
                '| 16/7 | 16/8 | 16/9 | 16/10', self.h_layout_cam_2)
            self.set_alias_device = AppContainerClass.create_qpushbutton(self.h_layout_cam_2,
                                                                         self.get_alias_device_button)
            self.h_layout_cam_3 = QtWidgets.QHBoxLayout()
            self.v_layout_m.addLayout(self.h_layout_cam_3)
            self.ip_cam = AppContainerClass.create_qlable(
                'IP CAM : 15.202 | 15.206 | 15.207 | 15.208 | 15.209 | 15.210 '
                '| 15.211 | 15.203 | 15.204 | 15.205', self.h_layout_cam_3)
            self.set_ip_cam = AppContainerClass.create_qpushbutton(self.h_layout_cam_3, self.get_ip_cam_button)
            self.h_layout_cam_4 = QtWidgets.QHBoxLayout()
            self.v_layout_m.addLayout(self.h_layout_cam_4)
            self.mask_cam = AppContainerClass.create_qlable(
                'MASK CAM : m_16_1.jpg | m_16_2.jpg | m_16_3.jpg | m_16_4.jpg '
                '| m_16_5.jpg | m_16_6.jpg | m_16_7.jpg | m_16_8.jpg '
                '| m_16_9.jpg | m_16_10.jpg', self.h_layout_cam_4)
            self.set_mask_cam = AppContainerClass.create_qpushbutton(self.h_layout_cam_4, self.get_mask_cam_button)
            self.h_layout_cam_5 = QtWidgets.QHBoxLayout()
            self.v_layout_m.addLayout(self.h_layout_cam_5)
            self.sensitivity_analysis = AppContainerClass.create_qlable(
                'SENSITIVITY ANALYSIS : 115 | 115 | 115 | 115 '
                '| 115 | 115 | 115 | 115 | 115 | 115',
                self.h_layout_cam_5)
            self.set_sensitivity_analysis = AppContainerClass.create_qpushbutton(self.h_layout_cam_5,
                                                                                 self.get_sensitivity_analysis_button)
            self.h_layout_cam_6 = QtWidgets.QHBoxLayout()
            self.v_layout_m.addLayout(self.h_layout_cam_6)
            self.alarm_level = AppContainerClass.create_qlable('ALARM LEVEL : 30 | 30 | 30 | 30 '
                                                               '| 30 | 30 | 30 | 30 | 30 | 30',
                                                               self.h_layout_cam_6)
            self.set_alarm_level = AppContainerClass.create_qpushbutton(self.h_layout_cam_6,
                                                                        self.get_alarm_level_button)
            self.h_layout_cam_7 = QtWidgets.QHBoxLayout()
            self.v_layout_m.addLayout(self.h_layout_cam_7)
            self.correct_coefficient = AppContainerClass.create_qlable(
                'CORRECT COEFFICIENT : 1.0 | 1.0 | 1.0 | 1.0 | 1.0 '
                '| 1.0 | 1.0 | 1.0 | 1.0 | 1.0', self.h_layout_cam_7)
            self.set_correct_coefficient = AppContainerClass.create_qpushbutton(self.h_layout_cam_7,
                                                                                self.get_correct_coefficient_button)
            # SQL
            self.h_layout_g_sql = QtWidgets.QHBoxLayout()
            self.v_layout_m.addLayout(self.h_layout_g_sql)
            self.g_sql_set = AppContainerClass.create_qlable('SQL', self.h_layout_g_sql, background=True)
            self.h_layout_sql_1 = QtWidgets.QHBoxLayout()
            self.v_layout_m.addLayout(self.h_layout_sql_1)
            self.sql_write = AppContainerClass.create_qcheckbox(self.h_layout_sql_1, 'CONNECT TO SQL?')
            self.ip_sql = AppContainerClass.create_qlable('IP SQL SERVER : 192.168.15.87', self.h_layout_sql_1)
            self.set_ip_sql = AppContainerClass.create_qpushbutton(self.h_layout_sql_1, self.get_ip_sql_button)
            self.server_sql = AppContainerClass.create_qlable(r'SERVER SQL : DESKTOP-SM7K050\COMPUTER_VISION',
                                                              self.h_layout_sql_1)
            self.set_server_sql = AppContainerClass.create_qpushbutton(self.h_layout_sql_1,
                                                                       self.get_server_sql_button)
            self.port_sql = AppContainerClass.create_qlable('PORT SQL SERVER : 1433', self.h_layout_sql_1)
            self.set_port_sql = AppContainerClass.create_qpushbutton(self.h_layout_sql_1, self.get_port_sql_button)
            self.h_layout_sql_2 = QtWidgets.QHBoxLayout()
            self.v_layout_m.addLayout(self.h_layout_sql_2)
            self.database_sql = AppContainerClass.create_qlable('DATABASE SQL : analiz_16grohot',
                                                                self.h_layout_sql_2)
            self.set_database_sql = AppContainerClass.create_qpushbutton(self.h_layout_sql_2,
                                                                         self.get_database_sql_button)
            self.user_sql = AppContainerClass.create_qlable('USER SQL : computer_vision', self.h_layout_sql_2)
            self.set_user_sql = AppContainerClass.create_qpushbutton(self.h_layout_sql_2, self.get_user_sql_button)
            self.h_layout_sql_3 = QtWidgets.QHBoxLayout()
            self.v_layout_m.addLayout(self.h_layout_sql_3)
            self.password_sql = AppContainerClass.create_qlable('PASSWORD SQL : vision12345678',
                                                                self.h_layout_sql_2)
            self.set_password_sql = AppContainerClass.create_qpushbutton(self.h_layout_sql_2,
                                                                         self.get_password_sql_button)
            self.sql_now_check = AppContainerClass.create_qcheckbox(self.h_layout_sql_3, 'WRITE NOW SQL?')
            self.table_now_sql = AppContainerClass.create_qlable('TABLE NOW SQL : grohot16_now_table',
                                                                 self.h_layout_sql_3)
            self.set_table_now_sql = AppContainerClass.create_qpushbutton(self.h_layout_sql_3,
                                                                          self.get_table_now_sql_button)
            self.rows_now_sql = AppContainerClass.create_qlable('ROWS NOW SQL : device_row | value_row | alarm_row '
                                                                '| datetime_row', self.h_layout_sql_3)
            self.set_rows_now_sql = AppContainerClass.create_qpushbutton(self.h_layout_sql_3,
                                                                         self.get_rows_now_sql_button)
            self.h_layout_sql_4 = QtWidgets.QHBoxLayout()
            self.v_layout_m.addLayout(self.h_layout_sql_4)
            self.sql_data_check = AppContainerClass.create_qcheckbox(self.h_layout_sql_4, 'WRITE DATA SQL?')
            self.table_data_sql = AppContainerClass.create_qlable('TABLE DATA SQL : grohot16_data_table',
                                                                  self.h_layout_sql_4)
            self.set_table_data_sql = AppContainerClass.create_qpushbutton(self.h_layout_sql_4,
                                                                           self.get_table_data_sql_button)
            self.rows_data_sql = AppContainerClass.create_qlable(
                'ROWS DATA SQL : device_row | value_row | alarm_row '
                '| datetime_row', self.h_layout_sql_4)
            self.set_rows_data_sql = AppContainerClass.create_qpushbutton(self.h_layout_sql_4,
                                                                          self.get_rows_data_sql_button)
            # DEBUG
            self.h_layout_g_debug = QtWidgets.QHBoxLayout()
            self.v_layout_m.addLayout(self.h_layout_g_debug)
            self.g_debug_set = AppContainerClass.create_qlable('DEBUG', self.h_layout_g_debug, background=True)
            self.h_layout_debug_1 = QtWidgets.QHBoxLayout()
            self.v_layout_m.addLayout(self.h_layout_debug_1)
            self.auto_import_check = AppContainerClass.create_qcheckbox(self.h_layout_debug_1, 'AUTO IMPORT?')
            self.auto_play_check = AppContainerClass.create_qcheckbox(self.h_layout_debug_1, 'AUTO PLAY?')
            self.speed_analysis = AppContainerClass.create_qlable('SPEED ANALYSIS : 1.0', self.h_layout_debug_1)
            self.set_speed_analysis = AppContainerClass.create_qpushbutton(self.h_layout_debug_1,
                                                                           self.get_speed_analysis_button)
            self.speed_video_stream = AppContainerClass.create_qlable('SPEED VIDEO-STREAM : 1.0',
                                                                      self.h_layout_debug_1)
            self.set_speed_video_stream = AppContainerClass.create_qpushbutton(self.h_layout_debug_1,
                                                                               self.get_speed_video_stream_button)
            self.h_layout_debug_2 = QtWidgets.QHBoxLayout()
            self.v_layout_m.addLayout(self.h_layout_debug_2)
            self.widget_data_value = AppContainerClass.create_qlable('0.00%', self.h_layout_debug_2)
            self.h_layout_debug_2.addStretch()
            self.widget_write = AppContainerClass.create_qcheckbox(self.h_layout_debug_2, 'WRITE TO WIDGET?')
            self.text_write = AppContainerClass.create_qcheckbox(self.h_layout_debug_2, 'WRITE TO TEXT?')
            self.source_win_type = AppContainerClass.create_qlable('SOURCE TYPE :', self.h_layout_debug_2)
            self.source_type = AppContainerClass.create_qcombobox(self.h_layout_debug_2,
                                                                  ['image-http', 'video-rtsp', 'video-file'],
                                                                  'image-http')
            self.compute_win_debug = AppContainerClass.create_qlable('COMPUTE TYPE :', self.h_layout_debug_2)
            self.compute_debug = AppContainerClass.create_qcombobox(self.h_layout_debug_2,
                                                                    ['sync', 'async', 'multithread',
                                                                     'multiprocess', 'complex'],
                                                                    'complex')
            self.process_cores = AppContainerClass.create_qlable('PROCESS CORES : 4', self.h_layout_debug_2)
            self.set_process_cores = AppContainerClass.create_qpushbutton(self.h_layout_debug_2,
                                                                          self.get_process_cores_button)
            self.h_layout_debug_3 = QtWidgets.QHBoxLayout()
            self.v_layout_m.addLayout(self.h_layout_debug_3)
            self.render_win_debug = AppContainerClass.create_qlable('Render windows :', self.h_layout_debug_3)
            self.render_debug = AppContainerClass.create_qcombobox(self.h_layout_debug_3,
                                                                   ['none', 'source', 'final', 'extended',
                                                                    'all'], 'none')
            self.resolution_debug_1 = AppContainerClass.create_qradiobutton(self.h_layout_debug_3, '320x240',
                                                                            default=True)
            self.resolution_debug_1.toggled.connect(self.set_resolution_debug(self.resolution_debug_1, 320, 240))
            self.resolution_debug_2 = AppContainerClass.create_qradiobutton(self.h_layout_debug_3, '640x480')
            self.resolution_debug_2.toggled.connect(self.set_resolution_debug(self.resolution_debug_2, 640, 480))
            self.resolution_debug_3 = AppContainerClass.create_qradiobutton(self.h_layout_debug_3, '1280x720')
            self.resolution_debug_3.toggled.connect(self.set_resolution_debug(self.resolution_debug_3, 1280, 720))
            self.resolution_debug_4 = AppContainerClass.create_qradiobutton(self.h_layout_debug_3, '1920x1080')
            self.resolution_debug_4.toggled.connect(self.set_resolution_debug(self.resolution_debug_4, 1920, 1080))
            self.resolution_debug_5 = AppContainerClass.create_qradiobutton(self.h_layout_debug_3, '2560x1600')
            self.resolution_debug_5.toggled.connect(self.set_resolution_debug(self.resolution_debug_5, 2560, 1600))
            self.resolution_debug_6 = AppContainerClass.create_qradiobutton(self.h_layout_debug_3, '3840x2160')
            self.resolution_debug_6.toggled.connect(self.set_resolution_debug(self.resolution_debug_6, 3840, 2160))
            # IMPORTS
            self.h_layout_g_imports = QtWidgets.QHBoxLayout()
            self.v_layout_m.addLayout(self.h_layout_g_imports)
            self.g_imports_set = AppContainerClass.create_qlable('IMPORTS', self.h_layout_g_imports,
                                                                 background=True)
            self.h_layout_imports_1 = QtWidgets.QHBoxLayout()
            self.v_layout_m.addLayout(self.h_layout_imports_1)
            self.import_file = AppContainerClass.create_qlable('SETTINGS FILE NAME : settings',
                                                               self.h_layout_imports_1)
            self.set_import_file = AppContainerClass.create_qpushbutton(self.h_layout_imports_1,
                                                                        self.get_settings_file_name)
            self.export_QPushButton = AppContainerClass.create_qpushbutton(self.h_layout_imports_1,
                                                                           self.export_settings_func, 'export')
            self.import_QPushButton = AppContainerClass.create_qpushbutton(self.h_layout_imports_1,
                                                                           self.import_settings_func, 'import')
            # SHOT
            self.h_layout_g_shot = QtWidgets.QHBoxLayout()
            self.v_layout_m.addLayout(self.h_layout_g_shot)
            self.g_shot_set = AppContainerClass.create_qlable('SHOT', self.h_layout_g_shot, background=True)
            self.h_layout_shot_1 = QtWidgets.QHBoxLayout()
            self.v_layout_m.addLayout(self.h_layout_shot_1)
            self.ip_cam_snapshot = AppContainerClass.create_qlable('ip-cam : 15.204', self.h_layout_shot_1)
            self.set_ip_cam_snapshot = AppContainerClass.create_qpushbutton(self.h_layout_shot_1,
                                                                            self.get_ip_cam_snapshot_button)
            self.name_snapshot = AppContainerClass.create_qlable('file name : picture.jpg', self.h_layout_shot_1)
            self.set_name_snapshot = AppContainerClass.create_qpushbutton(self.h_layout_shot_1,
                                                                          self.set_name_snapshot_button)
            self.snapshot_QPushButton = AppContainerClass.create_qpushbutton(self.h_layout_shot_1,
                                                                             self.snapshot_btn_func,
                                                                             'snapshot')

            self.setLayout(self.v_layout_m)
            self.auto_play_func()
            self.auto_import_settings_func()

        def get_speed_analysis_button(self):
            widget = self.speed_analysis
            value, success = QtWidgets.QInputDialog.getDouble(self, f'Set {widget.text().split(":")[0].strip()}',
                                                              f'{widget.text().split(":")[0].strip()} value:',
                                                              1.0, 0.01, 50.0, 2)
            if success:
                widget.setText(f'{widget.text().split(":")[0].strip()} : {str(value)}')

        def get_speed_video_stream_button(self):
            widget = self.speed_video_stream
            value, success = QtWidgets.QInputDialog.getDouble(self, f'Set {widget.text().split(":")[0].strip()}',
                                                              f'{widget.text().split(":")[0].strip()} value:',
                                                              1.0, 0.01, 50.0, 2)
            if success:
                widget.setText(f'{widget.text().split(":")[0].strip()} : {str(value)}')

        def get_sensitivity_analysis_button(self):
            widget = self.sensitivity_analysis
            value, success = QtWidgets.QInputDialog.getText(self, f'Set {widget.text().split(":")[0].strip()}',
                                                            f'{widget.text().split(":")[0].strip()} value:',
                                                            text=f'{widget.text().split(":")[1].strip()}')
            if success:
                widget.setText(f'{widget.text().split(":")[0].strip()} : {str(value)}')

        def get_alarm_level_button(self):
            widget = self.alarm_level
            value, success = QtWidgets.QInputDialog.getText(self, f'Set {widget.text().split(":")[0].strip()}',
                                                            f'{widget.text().split(":")[0].strip()} value:',
                                                            text=f'{widget.text().split(":")[1].strip()}')
            if success:
                widget.setText(f'{widget.text().split(":")[0].strip()} : {str(value)}')

        def get_correct_coefficient_button(self):
            widget = self.correct_coefficient
            value, success = QtWidgets.QInputDialog.getText(self, f'Set {widget.text().split(":")[0].strip()}',
                                                            f'{widget.text().split(":")[0].strip()} value:',
                                                            text=f'{widget.text().split(":")[1].strip()}')
            if success:
                widget.setText(f'{widget.text().split(":")[0].strip()} : {str(value)}')

        def get_protocol_cam_type_button(self):
            widget = self.protocol_cam_type
            value, success = QtWidgets.QInputDialog.getText(self, f'Set {widget.text().split(":")[0].strip()}',
                                                            f'{widget.text().split(":")[0].strip()} value:',
                                                            text=f'{widget.text().split(":")[1].strip()}')
            if success:
                widget.setText(f'{widget.text().split(":")[0].strip()} : {str(value)}')

        def get_port_cam_button(self):
            widget = self.port_cam
            value, success = QtWidgets.QInputDialog.getInt(self, f'Set {widget.text().split(":")[0].strip()}',
                                                           f'{widget.text().split(":")[0].strip()} value:',
                                                           554, 1, 9999, 5)
            if success:
                widget.setText(f'{widget.text().split(":")[0].strip()} : {str(value)}')

        def get_login_cam_button(self):
            widget = self.login_cam
            value, success = QtWidgets.QInputDialog.getText(self, f'Set {widget.text().split(":")[0].strip()}',
                                                            f'{widget.text().split(":")[0].strip()} value:',
                                                            text=f'{widget.text().split(":")[1].strip()}')
            if success:
                widget.setText(f'{widget.text().split(":")[0].strip()} : {str(value)}')

        def get_password_cam_button(self):
            widget = self.password_cam
            value, success = QtWidgets.QInputDialog.getText(self, f'Set {widget.text().split(":")[0].strip()}',
                                                            f'{widget.text().split(":")[0].strip()} value:',
                                                            text=f'{widget.text().split(":")[1].strip()}')
            if success:
                widget.setText(f'{widget.text().split(":")[0].strip()} : {str(value)}')

        def get_alias_device_button(self):
            widget = self.alias_device
            value, success = QtWidgets.QInputDialog.getText(self, f'Set {widget.text().split(":")[0].strip()}',
                                                            f'{widget.text().split(":")[0].strip()} value:',
                                                            text=f'{widget.text().split(":")[1].strip()}')
            if success:
                widget.setText(f'{widget.text().split(":")[0].strip()} : {str(value)}')

        def get_ip_cam_button(self):
            widget = self.ip_cam
            value, success = QtWidgets.QInputDialog.getText(self, f'Set {widget.text().split(":")[0].strip()}',
                                                            f'{widget.text().split(":")[0].strip()} value:',
                                                            text=f'{widget.text().split(":")[1].strip()}')
            if success:
                widget.setText(f'{widget.text().split(":")[0].strip()} : {str(value)}')

        def get_mask_cam_button(self):
            widget = self.mask_cam
            value, success = QtWidgets.QInputDialog.getText(self, f'Set {widget.text().split(":")[0].strip()}',
                                                            f'{widget.text().split(":")[0].strip()} value:',
                                                            text=f'{widget.text().split(":")[1].strip()}')
            if success:
                widget.setText(f'{widget.text().split(":")[0].strip()} : {str(value)}')

        def get_ip_sql_button(self):
            widget = self.ip_sql
            value, success = QtWidgets.QInputDialog.getText(self, f'Set {widget.text().split(":")[0].strip()}',
                                                            f'{widget.text().split(":")[0].strip()} value:',
                                                            text=f'{widget.text().split(":")[1].strip()}')
            if success:
                widget.setText(f'{widget.text().split(":")[0].strip()} : {str(value)}')

        def get_server_sql_button(self):
            widget = self.server_sql
            value, success = QtWidgets.QInputDialog.getText(self, f'Set {widget.text().split(":")[0].strip()}',
                                                            f'{widget.text().split(":")[0].strip()} value:',
                                                            text=f'{widget.text().split(":")[1].strip()}')
            if success:
                widget.setText(f'{widget.text().split(":")[0].strip()} : {str(value)}')

        def get_port_sql_button(self):
            widget = self.port_sql
            value, success = QtWidgets.QInputDialog.getText(self, f'Set {widget.text().split(":")[0].strip()}',
                                                            f'{widget.text().split(":")[0].strip()} value:',
                                                            text=f'{widget.text().split(":")[1].strip()}')
            if success:
                widget.setText(f'{widget.text().split(":")[0].strip()} : {str(value)}')

        def get_database_sql_button(self):
            widget = self.database_sql
            value, success = QtWidgets.QInputDialog.getText(self, f'Set {widget.text().split(":")[0].strip()}',
                                                            f'{widget.text().split(":")[0].strip()} value:',
                                                            text=f'{widget.text().split(":")[1].strip()}')
            if success:
                widget.setText(f'{widget.text().split(":")[0].strip()} : {str(value)}')

        def get_user_sql_button(self):
            widget = self.user_sql
            value, success = QtWidgets.QInputDialog.getText(self, f'Set {widget.text().split(":")[0].strip()}',
                                                            f'{widget.text().split(":")[0].strip()} value:',
                                                            text=f'{widget.text().split(":")[1].strip()}')
            if success:
                widget.setText(f'{widget.text().split(":")[0].strip()} : {str(value)}')

        def get_password_sql_button(self):
            widget = self.password_sql
            value, success = QtWidgets.QInputDialog.getText(self, f'Set {widget.text().split(":")[0].strip()}',
                                                            f'{widget.text().split(":")[0].strip()} value:',
                                                            text=f'{widget.text().split(":")[1].strip()}')
            if success:
                widget.setText(f'{widget.text().split(":")[0].strip()} : {str(value)}')

        def get_table_now_sql_button(self):
            widget = self.table_now_sql
            value, success = QtWidgets.QInputDialog.getText(self, f'Set {widget.text().split(":")[0].strip()}',
                                                            f'{widget.text().split(":")[0].strip()} value:',
                                                            text=f'{widget.text().split(":")[1].strip()}')
            if success:
                widget.setText(f'{widget.text().split(":")[0].strip()} : {str(value)}')

        def get_rows_now_sql_button(self):
            widget = self.rows_now_sql
            value, success = QtWidgets.QInputDialog.getText(self, f'Set {widget.text().split(":")[0].strip()}',
                                                            f'{widget.text().split(":")[0].strip()} value:',
                                                            text=f'{widget.text().split(":")[1].strip()}')
            if success:
                widget.setText(f'{widget.text().split(":")[0].strip()} : {str(value)}')

        def get_table_data_sql_button(self):
            widget = self.table_data_sql
            value, success = QtWidgets.QInputDialog.getText(self, f'Set {widget.text().split(":")[0].strip()}',
                                                            f'{widget.text().split(":")[0].strip()} value:',
                                                            text=f'{widget.text().split(":")[1].strip()}')
            if success:
                widget.setText(f'{widget.text().split(":")[0].strip()} : {str(value)}')

        def get_rows_data_sql_button(self):
            widget = self.rows_data_sql
            value, success = QtWidgets.QInputDialog.getText(self, f'Set {widget.text().split(":")[0].strip()}',
                                                            f'{widget.text().split(":")[0].strip()} value:',
                                                            text=f'{widget.text().split(":")[1].strip()}')
            if success:
                widget.setText(f'{widget.text().split(":")[0].strip()} : {str(value)}')

        def get_settings_file_name(self):
            widget = self.import_file
            value, success = QtWidgets.QInputDialog.getText(self, f'Set {widget.text().split(":")[0].strip()}',
                                                            f'{widget.text().split(":")[0].strip()} value:',
                                                            text=f'{widget.text().split(":")[1].strip()}')
            if success:
                widget.setText(f'{widget.text().split(":")[0].strip()} : {str(value)}')

        def set_resolution_debug(self, radio, width: int, height: int):
            self.resolution_debug.append([radio, width, height])

        def get_window_resolution(self):
            for radio in self.resolution_debug:
                try:
                    if radio[0].isChecked():
                        return [int(radio[1]), int(radio[2])]
                except Exception as ex:
                    print(ex)

        def set_window_resolution(self, value):
            for radio in self.resolution_debug:
                try:
                    if radio[1] == value[0]:
                        radio[0].setChecked(True)
                    else:
                        radio[0].setChecked(False)
                except Exception as ex:
                    print(ex)

        def get_process_cores_button(self):
            widget = self.process_cores
            value, success = QtWidgets.QInputDialog.getInt(self, f'Set {widget.text().split(":")[0].strip()}',
                                                           f'{widget.text().split(":")[0].strip()} value:',
                                                           4, 1, 16, 5)
            if success:
                widget.setText(f'{widget.text().split(":")[0].strip()} : {str(value)}')

        def get_ip_cam_snapshot_button(self):
            widget = self.ip_cam_snapshot
            value, success = QtWidgets.QInputDialog.getText(self, f'Set {widget.text().split(":")[0].strip()}',
                                                            f'{widget.text().split(":")[0].strip()} value:',
                                                            text=f'{widget.text().split(":")[1].strip()}')
            if success:
                widget.setText(f'{widget.text().split(":")[0].strip()} : {str(value)}')

        def set_name_snapshot_button(self):
            widget = self.name_snapshot
            value, success = QtWidgets.QInputDialog.getText(self, f'Set {widget.text().split(":")[0].strip()}',
                                                            f'{widget.text().split(":")[0].strip()} value:',
                                                            text=f'{widget.text().split(":")[1].strip()}')
            if success:
                widget.setText(f'{widget.text().split(":")[0].strip()} : {str(value)}')

        def get_string_from_list(self, source: list):
            value = ''
            for x in source:
                value = f'{value} | {x}'
            return value[3::]

        def set_data_func(self, value: str):
            try:
                self.widget_data_value.setText(f"{value}")
            except Exception as ex:
                LoggingClass.logging(ex)
                print(f'set_data_func error : {ex}')

        def create_data_func(self):
            try:
                data = {
                    'protocol_cam_type': str(self.protocol_cam_type.text().split(':')[1].strip()),
                    'port_cam': int(self.port_cam.text().split(':')[1].strip()),
                    'login_cam': str(self.login_cam.text().split(':')[1].strip()),
                    'password_cam': str(self.password_cam.text().split(':')[1].strip()),
                    'alias_device': list(
                        [x.strip() for x in self.alias_device.text().split(':')[1].strip().split('|')]),
                    'ip_cam': list([x.strip() for x in self.ip_cam.text().split(':')[1].strip().split('|')]),
                    'mask_cam': list([x.strip() for x in self.mask_cam.text().split(':')[1].strip().split('|')]),
                    'sensitivity_analysis': list([int(x.strip()) for x in
                                                  self.sensitivity_analysis.text().split(':')[1].strip().split(
                                                      '|')]),
                    'alarm_level': list(
                        [int(x.strip()) for x in self.alarm_level.text().split(':')[1].strip().split('|')]),
                    'correct_coefficient': list([float(x.strip()) for x in
                                                 self.correct_coefficient.text().split(':')[1].strip().split('|')]),

                    'sql_write': bool(self.sql_write.isChecked()),
                    'ip_sql': str(self.ip_sql.text().split(':')[1].strip()),
                    'server_sql': str(self.server_sql.text().split(':')[1].strip()),
                    'port_sql': str(self.port_sql.text().split(':')[1].strip()),
                    'database_sql': str(self.database_sql.text().split(':')[1].strip()),
                    'user_sql': str(self.user_sql.text().split(':')[1].strip()),
                    'password_sql': str(self.password_sql.text().split(':')[1].strip()),
                    'sql_now_check': bool(self.sql_now_check.isChecked()),
                    'table_now_sql': str(self.table_now_sql.text().split(':')[1].strip()),
                    'rows_now_sql': list(
                        [x.strip() for x in self.rows_now_sql.text().split(':')[1].strip().split('|')]),
                    'sql_data_check': bool(self.sql_data_check.isChecked()),
                    'table_data_sql': str(self.table_data_sql.text().split(':')[1].strip()),
                    'rows_data_sql': list(
                        [x.strip() for x in self.rows_data_sql.text().split(':')[1].strip().split('|')]),

                    'auto_import_check': bool(self.auto_import_check.isChecked()),
                    'auto_play_check': bool(self.auto_play_check.isChecked()),
                    'speed_analysis': float(self.speed_analysis.text().split(':')[1].strip()),
                    'speed_video_stream': float(self.speed_video_stream.text().split(':')[1].strip()),

                    'widget_write': bool(self.widget_write.isChecked()),
                    'text_write': bool(self.text_write.isChecked()),
                    'widget': self.set_data_func,
                    'source_type': str(self.source_type.currentText().strip()),
                    'compute_debug': str(self.compute_debug.currentText().strip()),
                    'process_cores': int(self.process_cores.text().split(':')[1].strip()),
                    'render_debug': str(self.render_debug.currentText().strip()),
                    'resolution_debug': list(self.get_window_resolution()),

                    'import_file': str(self.import_file.text().split(':')[1].strip()),

                    'ip_cam_snapshot': str(self.ip_cam_snapshot.text().split(":")[1].strip()),
                    'name_snapshot': str(self.name_snapshot.text().split(":")[1].strip()),
                }
                return data
            except Exception as ex:
                LoggingClass.logging(ex)
                print(f'create_data_func error : {ex}')

        def play_btn_func(self):
            try:
                data = self.create_data_func()
                self.play_f(data=data)
            except Exception as ex:
                LoggingClass.logging(ex)
                print(f'play_btn_func error : {ex}')

        def snapshot_btn_func(self):
            try:
                data = self.create_data_func()
                self.snapshot_f(data=data)
            except Exception as ex:
                LoggingClass.logging(ex)
                print(f'snapshot_btn_func error : {ex}')

        def export_settings_func(self):
            try:
                data = self.create_data_func()
                del data['widget']
                JsonClass.write_json_to_file(dictionary=data)
            except Exception as ex:
                LoggingClass.logging(ex)
                print(f'export_settings_func error : {ex}')

        def import_settings_func(self):
            try:
                data = self.create_data_func()
                data = JsonClass.read_json_from_file(data)
                self.protocol_cam_type.setText(f'{self.protocol_cam_type.text().split(":")[0].strip()} : '
                                               f'{str(data["protocol_cam_type"])}')
                self.port_cam.setText(f'{self.port_cam.text().split(":")[0].strip()} : '
                                      f'{str(data["port_cam"])}')
                self.login_cam.setText(f'{self.login_cam.text().split(":")[0].strip()} : '
                                       f'{str(data["login_cam"])}')
                self.password_cam.setText(f'{self.password_cam.text().split(":")[0].strip()} : '
                                          f'{str(data["password_cam"])}')
                self.alias_device.setText(f'{self.alias_device.text().split(":")[0].strip()} : '
                                          f'{self.get_string_from_list(data["alias_device"])}')
                self.ip_cam.setText(f'{self.ip_cam.text().split(":")[0].strip()} : '
                                    f'{self.get_string_from_list(data["ip_cam"])}')
                self.mask_cam.setText(f'{self.mask_cam.text().split(":")[0].strip()} : '
                                      f'{self.get_string_from_list(data["mask_cam"])}')
                self.sensitivity_analysis.setText(f'{self.sensitivity_analysis.text().split(":")[0].strip()} : '
                                                  f'{self.get_string_from_list(data["sensitivity_analysis"])}')
                self.alarm_level.setText(f'{self.alarm_level.text().split(":")[0].strip()} : '
                                         f'{self.get_string_from_list(data["alarm_level"])}')
                self.correct_coefficient.setText(f'{self.correct_coefficient.text().split(":")[0].strip()} : '
                                                 f'{self.get_string_from_list(data["correct_coefficient"])}')
                self.sql_write.setChecked(data["sql_write"])
                self.ip_sql.setText(f'{self.ip_sql.text().split(":")[0].strip()} : {str(data["ip_sql"])}')
                self.server_sql.setText(
                    f'{self.server_sql.text().split(":")[0].strip()} : {str(data["server_sql"])}')
                self.port_sql.setText(f'{self.port_sql.text().split(":")[0].strip()} : {str(data["port_sql"])}')
                self.database_sql.setText(f'{self.database_sql.text().split(":")[0].strip()} : '
                                          f'{str(data["database_sql"])}')
                self.user_sql.setText(f'{self.user_sql.text().split(":")[0].strip()} : '
                                      f'{str(data["user_sql"])}')
                self.password_sql.setText(f'{self.password_sql.text().split(":")[0].strip()} : '
                                          f'{str(data["password_sql"])}')
                self.sql_now_check.setChecked(data["sql_now_check"])
                self.table_now_sql.setText(f'{self.table_now_sql.text().split(":")[0].strip()} : '
                                           f'{str(data["table_now_sql"])}')
                self.rows_now_sql.setText(f'{self.rows_now_sql.text().split(":")[0].strip()} : '
                                          f'{self.get_string_from_list(data["rows_now_sql"])}')
                self.sql_data_check.setChecked(data["sql_data_check"])
                self.table_data_sql.setText(f'{self.table_data_sql.text().split(":")[0].strip()} : '
                                            f'{str(data["table_data_sql"])}')
                self.rows_data_sql.setText(f'{self.rows_data_sql.text().split(":")[0].strip()} : '
                                           f'{self.get_string_from_list(data["rows_data_sql"])}')
                self.auto_import_check.setChecked(data["auto_import_check"])
                self.auto_play_check.setChecked(data["auto_play_check"])
                self.speed_analysis.setText(f'{self.speed_analysis.text().split(":")[0].strip()} : '
                                            f'{str(data["speed_analysis"])}')
                self.speed_video_stream.setText(f'{self.speed_video_stream.text().split(":")[0].strip()} : '
                                                f'{str(data["speed_video_stream"])}')
                self.widget_write.setChecked(data["widget_write"])
                self.text_write.setChecked(data["text_write"])
                self.source_type.setCurrentText(data["source_type"])
                self.compute_debug.setCurrentText(data["compute_debug"])
                self.process_cores.setText(f'{self.process_cores.text().split(":")[0].strip()} : '
                                           f'{str(data["process_cores"])}')
                self.render_debug.setCurrentText(data["render_debug"])
                self.set_window_resolution(data["resolution_debug"])
                self.import_file.setText(f'{self.import_file.text().split(":")[0].strip()} : '
                                         f'{str(data["import_file"])}')
                self.ip_cam_snapshot.setText(f'{self.ip_cam_snapshot.text().split(":")[0].strip()} : '
                                             f'{str(data["ip_cam_snapshot"])}')
                self.name_snapshot.setText(f'{self.name_snapshot.text().split(":")[0].strip()} : '
                                           f'{str(data["name_snapshot"])}')
            except Exception as ex:
                LoggingClass.logging(ex)
                print(f'import_settings_func error : {ex}')

        def auto_import_settings_func(self):
            try:
                data = self.create_data_func()
                data = JsonClass.read_json_from_file(data)
                if data['auto_import_check']:
                    self.import_settings_func()
            except Exception as ex:
                LoggingClass.logging(ex)
                print(f'auto_import_settings_func error : {ex}')

        def auto_play_func(self):
            try:
                data = self.create_data_func()
                _data = JsonClass.read_json_from_file(data)
                _data['widget'] = data['widget']
                if _data['auto_play_check']:
                    self.play_f(data=_data)
                    self.showMinimized()
            except Exception as ex:
                LoggingClass.logging(ex)
                print(f'auto_play_func error : {ex}')

########################################################################################################################
