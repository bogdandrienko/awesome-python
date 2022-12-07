def checkpolidrom(value1: str) -> bool:
    # val1, val2 = value1, value1[::-1]
    if value1 == value1[::-1]:
        return True
    else:
        return False


print(checkpolidrom("голод 1долог"))
print("run"[::])  # - пересобирает строку кроме последнего символа
print("run"[-1])  # - берёт последний символ


def recur_sum(max_val: int) -> None:
    if max_val < -100:
        return None
    else:
        print(max_val)
        recur_sum(max_val - 1)  # 9 8 7 6


# recur_sum(10)


def getfactorial(n: int) -> int:
    res = 1
    for i in range(1, n + 1):  # [1, 2, 3, 4, 5]
        res *= i
    return res


print(getfactorial(3))  # 3 628 800


def getfactorial1(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * getfactorial1(n - 1)  # (4, 5)


print(getfactorial1(4))  # 3 628 800







#############################################################################################################################################


class GeoClass:
    @staticmethod
    def get_hypotenuse(x1: float, y1: float, x2: float, y2: float):
        """"
        Принимает: "пару" точек - их широту и долготу.
        Возвращает: корень из суммы квадратов разностей широты и долготы двух пар точек, ака гипотенузу.
        """
        return math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))

    @staticmethod
    def get_haversine(latitude_1: float, longitude_1: float, latitude_2: float, longitude_2: float):
        """"
        Принимает: "пару" точек - их широту и долготу.
        Возвращает: значение расстояния по гипотенузе двух точек, в метрах, ака формула гаверсинуса.
        """
        delta_latitude = latitude_2 * math.pi / 180 - latitude_1 * math.pi / 180
        delta_longitude = longitude_2 * math.pi / 180 - longitude_1 * math.pi / 180
        a = math.sin(delta_latitude / 2) * math.sin(delta_latitude / 2) + math.cos(latitude_1 * math.pi / 180) * \
            math.cos(latitude_2 * math.pi / 180) * math.sin(delta_longitude / 2) * math.sin(delta_longitude / 2)
        return round(math.atan2(math.sqrt(a), math.sqrt(1 - a)) * 6378.137 * 2 * 1000)

    @staticmethod
    def find_near_point(point_arr: list, point_latitude: float, point_longitude: float):
        """"
        Принимает: массив точек в которых надо искать, где первый элемент это широта, а второй долгоа. Также данные
        точки ближайшие координаты которой надо найти.
        Возвращает: данные точки из массива точек, которая соответствует ближайшему значению целевой точки.
        """
        result = None
        for coord in point_arr:
            if coord[0] <= point_latitude and coord[1] <= point_longitude:
                result = coord
        if result is None:
            result = point_arr[0]
        return result

    @staticmethod
    def get_vector_arr(point_arr):
        """
        Принимает: массив "точек" - первый элемент это имя точки, второй и третий это широта и долгота, а четвёртый
        связи.
        Возвращает: массив "векторов" - первый элемент это имя вектора, второй это расстояние через формулу
        "гаверсинуса".
        """
        # Points = [PointName, latitude, longitude, PointLinks]
        # point1 = ["1", 52.14303, 61.22812, "2"]
        # point2 = ["2", 52.1431, 61.22829, "1|3"]
        # Vectors = [VectorName, length(meters)]
        # vector1 = ["1|2", 12]
        # vector2 = ["2|3", 14]

        vector_arr = []
        for point in point_arr:
            lat1 = point[0]
            lon1 = point[1]
            vector1 = point[2]
            link_arr = point[3].split("|")
            for link in link_arr:
                for point_1 in point_arr:
                    if point_1[2] == link:
                        lat2 = point_1[0]
                        lon2 = point_1[1]
                        vector2 = link
                        length = GeoClass.get_haversine(lat1, lon1, lat2, lon2)
                        vector_arr.append([f"{vector1}|{vector2}", length])
        return vector_arr

    @staticmethod
    def create_cube_object(point: list):
        latitude = point[0]
        longitude = point[1]
        first = [latitude - 0.000002 * 1.62, longitude - 0.000002, 0]
        second = [latitude - 0.000002 * 1.62, longitude + 0.000002, 0]
        third = [latitude + 0.000002 * 1.62, longitude + 0.000002, 0]
        fourth = [latitude + 0.000002 * 1.62, longitude - 0.000002, 0]
        string_object = ''
        for iteration in [first, second, third, fourth, first]:
            num = 1
            for i in iteration:
                if num == 3:
                    string_object += f"{i} "
                else:
                    string_object += f"{i},"
                num += 1
        text_d = '' \
            # f"""<Placemark>
        # 	<name>object</name>
        # 	<Polygon>
        # 		<outerBoundaryIs>
        # 			<LinearRing>
        # 				<coordinates>
        # 					{string_object}
        # 				</coordinates>
        # 			</LinearRing>
        # 		</outerBoundaryIs>
        # 	</Polygon>
        # </Placemark>"""
        return text_d

    @staticmethod
    def create_point_object(point: list):
        latitude = point[0]
        longitude = point[1]
        id_s = point[2]
        # first = [latitude - 0.000002 * 1.62, longitude - 0.000002, 0]
        # second = [latitude - 0.000002 * 1.62, longitude + 0.000002, 0]
        # third = [latitude + 0.000002 * 1.62, longitude + 0.000002, 0]
        # fourth = [latitude + 0.000002 * 1.62, longitude - 0.000002, 0]
        # string_object = ''
        # for iteration in [first, second, third, fourth, first]:
        #     num = 1
        #     for i in iteration:
        #         if num == 3:
        #             string_object += f"{i} "
        #         else:
        #             string_object += f"{i},"
        #         num += 1
        text_d = f"""<Placemark>
                <name>Точка: {id_s}</name>
                <Point>
                    <coordinates>{latitude},{longitude},0</coordinates>
                </Point>
            </Placemark>"""
        return text_d

    @staticmethod
    def generate_xlsx():
        # connection = pg.connect(
        #     host="192.168.1.6",
        #     database="navSections",
        #     port="5432",
        #     user="postgres",
        #     password="nF2ArtXK"
        # )
        # # postgresql_select_query = f"SELECT device, navtime, ROUND(CAST(latitude AS numeric),
        # {request.POST['request_value']}), ROUND(CAST(longitude AS numeric), {request.POST['request_value']}) " \
        # #                           "FROM public.navdata_202108 " \
        # #                           f"WHERE device BETWEEN {request.POST['request_between_first']} AND
        # {request.POST['request_between_last']} AND timezone('UTC', to_timestamp(navtime)) >
        # (CURRENT_TIMESTAMP - INTERVAL '{request.POST['request_hours']} hours') AND flags != 64 " \
        # #                           "ORDER BY device, navtime DESC;"
        # postgresql_select_query = f"SELECT device, navtime, ROUND(CAST(latitude AS numeric),
        # {request.POST['request_value']}), ROUND(CAST(longitude AS numeric), {request.POST['request_value']}) " \
        #                           "FROM public.navdata_202108 " \
        #                           f"WHERE device BETWEEN {request.POST['request_between_first']} AND
        #                           {request.POST['request_between_last']} AND timezone('UTC', to_timestamp(navtime)) >
        #                           (CURRENT_TIMESTAMP - INTERVAL '{request.POST['request_minutes']} minutes') AND
        #                           flags != 64 " \
        #                           "ORDER BY device, navtime DESC;"
        # cursor = connection.cursor()
        # cursor.execute(postgresql_select_query)
        # mobile_records = cursor.fetchall()
        mobile_records = []
        cols = ["устройство", "дата и время", "широта", "долгота", "высота", "скорость", "ds", "направление",
                "флаги ошибок"]
        all_arr = []
        for rows in mobile_records:
            arr = []
            for value in rows:
                id_s = rows.index(value)
                if id_s == 1:
                    arr.append(datetime.datetime.fromtimestamp(int(value - 21600)).strftime('%Y-%m-%d %H:%M:%S'))
                else:
                    arr.append(value)
            all_arr.append(arr)
        wb = openpyxl.Workbook()
        sheet = wb.active
        sheet.title = 'Страница 1'
        for n in cols:
            sheet[f'{get_column_letter(cols.index(n) + 1)}1'] = n
        for n in all_arr:
            for i in n:
                if i:
                    sheet[f'{get_column_letter(n.index(i) + 1)}{all_arr.index(n) + 2}'] = i
                else:
                    sheet[f'{get_column_letter(n.index(i) + 1)}{all_arr.index(n) + 2}'] = '0.0'
        wb.save('static/media/data/geo.xlsx')
        postgresql_select_query = None
        return [cols, all_arr, postgresql_select_query]

    @staticmethod
    def generate_kml():
        # Чтение Excel
        file_xlsx = 'static/media/data/geo_1.xlsx'
        workbook = openpyxl.load_workbook(file_xlsx)
        sheet = workbook.active

        # Чтение из Excel
        final = 0
        for num in range(2, 10000000):
            if backend_utils.ExcelClass.get_sheet_value("A", num, sheet=sheet) is None or '':
                final = num
                break
        array = []
        for num in range(2, final):
            array.append(
                [backend_utils.ExcelClass.get_sheet_value("D", num, sheet=sheet),
                 backend_utils.ExcelClass.get_sheet_value("C", num, sheet=sheet),
                 backend_utils.ExcelClass.get_sheet_value("A", num, sheet=sheet)]
            )

        # Генерация объекта и субъекта
        point_obj = [61.22330, 52.14113, 'БелАЗ']
        point_sub = [61.22891, 52.14334, 'Экскаватор']
        text_x = GeoClass.create_point_object(point_obj)
        text_y = GeoClass.create_point_object(point_sub)

        # Цена рёбер
        count = 0
        for current in array:
            index = array.index(current)
            if index != 0:
                previous = [array[index - 1][0], array[index - 1][1]]
            else:
                previous = [current[0], current[1]]

            count += GeoClass.get_hypotenuse(current[0], current[1], previous[0], previous[1])
        print(round(count, 5))

        # Генерация линий по цветам
        device_arr = []
        previous_device = 0
        text_b = ''
        colors = ['FFFFFFFF', 'FF0000FF', 'FFFF0000', 'FF00FF00', 'FF00FFFF', 'FF0F0F0F', 'FFF0F0F0']
        colors_alias = [': Чё', ': Кр', ': Си', ': Зе', ': Жё', ': Доп1', ': Доп2']
        current_color = colors[0]
        for current in array:
            # index = array.index(current)
            if previous_device is not current[2]:
                device_arr.append(str(current[2]) + colors_alias[len(device_arr) + 1])
                previous_device = current[2]
                current_color = colors[colors.index(current_color) + 1]
            # if index != 0:
            #     previous = [array[index - 1][0], array[index - 1][1]]
            # else:
            #     previous = [current[0], current[1]]
            # text_b += f"""<Placemark>
            #       <Style>
            #         <LineStyle>
            #           <color>{current_color}</color>
            #         </LineStyle>
            #       </Style>
            #       <LineString>
            #         <coordinates>{previous[0]},{previous[1]},0 {current[0]},{current[1]},0 </coordinates>
            #       </LineString>
            #   </Placemark>
            # """
            #
            # # Генерация точек
            # text_b += GeoClass.create_cube_object([current[0], current[1], index])

        # Генерация имени документа из цветов
        dev = ''
        for x in device_arr:
            dev += f"{x} | "

        # Начало kml
        text_a = f"""<?xml version="1.0" encoding="utf-8"?>
          <kml xmlns="http://earth.google.com/kml/2.2">
            <Document>
              <name>{dev}</name>
                """

        # Конец kml
        text_c = R"""</Document>
        </kml>"""

        # Запись в kml
        with open("static/media/data/geo.kml", "w", encoding="utf-8") as file:
            file.write(text_a + text_b + text_x + text_y + text_c)

    @staticmethod
    def generate_way(object_, subject_, point_arr):
        # Генерация общей карты
        text_map = GeoClass.generate_map(point_arr, 'FF0000FF')
        # text_map = ''

        # Генерация объекта и субъекта
        point_obj = [object_[0], object_[1], "ЭКГ"]
        point_sub = [subject_[0], subject_[1], "БелАЗ"]
        text_obj = GeoClass.create_point_object(point_obj)
        text_sub = GeoClass.create_point_object(point_sub)

        path = GeoClass.generate_path(object_, subject_, point_arr)
        # print(path[0])
        # Генерация карты пути
        text_path = GeoClass.generate_map(path[0], 'FFFF0000')

        # Генерация имени документа из цветов
        dev = ''
        for x in [object_[0], subject_[0]]:
            dev += f"{x} | "
        dev += f"{path[1]} meters"
        print(f"{path[1]} meters")

        # Начало kml
        text_title = f"""<?xml version="1.0" encoding="utf-8"?>
          <kml xmlns="http://earth.google.com/kml/2.2">
            <Document>
              <name>{dev}</name>
                """

        # Конец kml
        text_footer = R"""</Document>
        </kml>"""

        # Запись в kml
        try:
            os.remove("static/media/data/geo_1.kml")
        except Exception as error:
            DjangoClass.LoggingClass.logging_errors_local(error=error, function_error='generate_way')
        with open("static/media/data/geo_5.kml", "w", encoding="utf-8") as file:
            file.write(text_title + text_map + text_path + text_obj + text_sub + text_footer)

    @staticmethod
    def generate_path(object_, subject_, point_arr):
        """"
        Генерация пути синего цвета из всех валидных точек и расчёт расстояния.
        """
        # Путь маршрут
        path = []
        # Расстояние пути
        path_distantion = 0

        # Откуда начинаем путь
        from_point = object_
        print(f"from_point: {from_point}")
        # from_point: [61.232109, 52.146845, '38', '37|39']

        # Где завершаем путь
        to_point = subject_
        print(f"to_point: {to_point}")
        # to_point: [61.229219, 52.143999, '12', '11|13']

        # Генерация маршрута
        # От исходной точки идём к её линиям связи, выбираем самую короткую к финальной точке, "наступаем" туда, цикл.
        start_point = from_point
        final_point = to_point

        path.append(from_point)
        while True:
            print('\n*****************')
            print('while', start_point[2], final_point[2])
            links = start_point[3].split("|")
            print(f"links: {links}")
            # links: ['38', '40']

            near_points = []
            for point in point_arr:
                for link in links:
                    if point[2] == link:
                        try:
                            near_points.index(point)
                        except Exception as error:
                            DjangoClass.LoggingClass.logging_errors_local(error=error, function_error='generate_path')
                            near_points.append(point)
            print(f"near_points: {near_points}")
            # near_points: [[61.232054, 52.146927, '38', '37|39'], [61.232384, 52.147085, '40', '39|41']]

            destinations = []
            for point in near_points:
                destinations.append(GeoClass.get_haversine(point[0], point[1], final_point[0], final_point[1]))
            print(f"destinations: {destinations}")
            # destinations: [[61.232054, 52.146927, '38', '37|39'], [61.232384, 52.147085, '40', '39|41']]

            min_point = min(destinations)
            print(f"min_point: {min_point}")
            # min_point: 367

            if min_point == 0:
                next_point = final_point
                print(f"next_point: {next_point}")
                # next_point: [61.232101, 52.146821, '45', '44|46']

                dist = GeoClass.get_haversine(start_point[0], start_point[1], final_point[0], final_point[1])
                print(f"dist: {dist}")
                # dist: 22

                path_distantion += dist
                path.append(next_point)
                break

            next_point = near_points[destinations.index(min_point)]
            print(f"next_point: {next_point}")
            # next_point: [61.232101, 52.146821, '45', '44|46']

            dist = GeoClass.get_haversine(start_point[0], start_point[1], next_point[0], next_point[1])
            print(f"dist: {dist}")
            # dist: 22

            path_distantion += dist
            start_point = next_point
            path.append(next_point)
            print('*****************\n')
        return [path, path_distantion]

    @staticmethod
    def generate_path_old(object_, subject_, point_arr):
        """"
        Генерация пути синего цвета из всех валидных точек.
        """
        # Генерация маршрута
        # От исходной точки идём к её линиям связи, выбираем самую короткую к финальной точке, "наступаем" туда, цикл.
        path = []
        path_dist = 0
        current_point = subject_
        # subject_: [61.232230610495556, 52.14697472947569, '21', '20|22']
        previous_point = subject_
        for loop in range(len(point_arr)):
            # links: ['20', '22']
            links = current_point[3].split("|")
            near_points = []
            for point in point_arr:
                for link in links:
                    if point[2] == link:
                        # print(point[2])
                        try:
                            near_points.index(point)
                        except Exception as error:
                            DjangoClass.LoggingClass.logging_errors_local(
                                error=error, function_error='generate_path_old'
                            )
                            near_points.append(point)

            # Первые две линии не брать, а к последней по индексу добавлять ещё одну связь.
            min_dist = 9999
            # print(near_points)
            for point in near_points:
                # object_: [61.2293618582404, 52.143978995225346, '4', '3|5']
                dist = GeoClass.get_haversine(point[0], point[1], object_[0], object_[1])
                # print(f"dist: {dist}")
                if min_dist > dist:
                    min_dist = dist
                    current_point = point
                    path.append(point)
                    distantion = GeoClass.get_haversine(point[0], point[1], previous_point[0], previous_point[1])
                    print(f"prev: {previous_point}   |   curr: {point}     |       deist: {distantion}m")
                    path_dist += distantion
                previous_point = point
        print(path_dist)
        path_dist = 0
        for x in path:
            path_dist += GeoClass.get_haversine(x[0], x[1], object_[0], object_[1])
            print(GeoClass.get_haversine(x[0], x[1], object_[0], object_[1]))
        return [path, path_dist]

    @staticmethod
    def generate_map(point_arr, color):
        """"
        Генерация карты выбранного цвета из всех валидных точек.
        """
        text = ''
        for current in point_arr:
            index = point_arr.index(current)
            if index != 0:
                previous = [point_arr[index - 1][0], point_arr[index - 1][1]]
            else:
                previous = [current[0], current[1]]
            text += f"""<Placemark>
                  <Style>
                    <LineStyle>
                      <color>{color}</color>
                    </LineStyle>
                  </Style>
                  <LineString>
                    <coordinates>{previous[0]},{previous[1]},0 {current[0]},{current[1]},0 </coordinates>
                  </LineString>
              </Placemark>
            """
            # Генерация точек
            text += GeoClass.create_cube_object([current[0], current[1], index])
        return text

    @staticmethod
    def read_kml(val: list):
        """"
        Чтение из kml-файла
        """
        with open("static/media/data/geo.kml", 'rt', encoding="utf-8") as file:
            data = file.read()
        k = kml.KML()
        k.from_string(data)
        features = list(k.features())
        k2 = list(features[0].features())
        arr = []
        for feat in k2:
            string = str(feat.geometry).split('(')[1].split('0.0')[0].split(' ')
            arr.append([float(string[0]), float(string[1])])
        if val is None:
            val = [61.2200083333333, 52.147525]
        val2 = 0
        val3 = 0
        for loop1 in arr:
            # Мы должны найти к какой из точек он ближе(разница двух элементов массива)
            if val[0] > loop1[0]:
                for loop2 in arr:
                    if val[1] > loop2[1]:
                        val2 = loop1[0]
                        val3 = loop1[1]
                        break
        print([val2, val3])
        return [val2, val3]

    @staticmethod
    def create_style():
        # f"""
        # <gx:CascadingStyle kml:id="__managed_style_25130D559F1CA685BFB3">
        # 	<Style>
        # 		<IconStyle>
        # 			<scale>1.2</scale>
        # 			<Icon>
        # 				<href>https://earth.google.com/earth/rpc/cc/icon?color=1976d2&amp;id=2000&amp;scale=4</href>
        # 			</Icon>
        # 			<hotSpot x="64" y="128" xunits="pixels" yunits="insetPixels"/>
        # 		</IconStyle>
        # 		<LabelStyle>
        # 		</LabelStyle>
        # 		<LineStyle>
        # 			<color>ff2dc0fb</color>
        # 			<width>6</width>
        # 		</LineStyle>
        # 		<PolyStyle>
        # 			<color>40ffffff</color>
        # 		</PolyStyle>
        # 		<BalloonStyle>
        # 			<displayMode>hide</displayMode>
        # 		</BalloonStyle>
        # 	</Style>
        # </gx:CascadingStyle>
        # <gx:CascadingStyle kml:id="__managed_style_1A4EFD26461CA685BFB3">
        # 	<Style>
        # 		<IconStyle>
        # 			<Icon>
        # 				<href>https://earth.google.com/earth/rpc/cc/icon?color=1976d2&amp;id=2000&amp;scale=4</href>
        # 			</Icon>
        # 			<hotSpot x="64" y="128" xunits="pixels" yunits="insetPixels"/>
        # 		</IconStyle>
        # 		<LabelStyle>
        # 		</LabelStyle>
        # 		<LineStyle>
        # 			<color>ff2dc0fb</color>
        # 			<width>4</width>
        # 		</LineStyle>
        # 		<PolyStyle>
        # 			<color>40ffffff</color>
        # 		</PolyStyle>
        # 		<BalloonStyle>
        # 			<displayMode>hide</displayMode>
        # 		</BalloonStyle>
        # 	</Style>
        # </gx:CascadingStyle>
        # <StyleMap id="__managed_style_047C2286A81CA685BFB3">
        # 	<Pair>
        # 		<key>normal</key>
        # 		<styleUrl>#__managed_style_1A4EFD26461CA685BFB3</styleUrl>
        # 	</Pair>
        # 	<Pair>
        # 		<key>highlight</key>
        # 		<styleUrl>#__managed_style_25130D559F1CA685BFB3</styleUrl>
        # 	</Pair>
        # </StyleMap>
        # <Placemark id="0D045F86381CA685BFB2">
        # 	<name>Самосвал</name>
        # 	<LookAt>
        # 		<longitude>61.2344061029136</longitude>
        # 		<latitude>52.17019183209385</latitude>
        # 		<altitude>282.7747547496757</altitude>
        # 		<heading>0</heading>
        # 		<tilt>0</tilt>
        # 		<gx:fovy>35</gx:fovy>
        # 		<range>1198.571236050484</range>
        # 		<altitudeMode>absolute</altitudeMode>
        # 	</LookAt>
        # 	<styleUrl>#__managed_style_047C2286A81CA685BFB3</styleUrl>
        # 	<Point>
        # 		<coordinates>61.23500224897153,52.17263169824412,281.7092496784567</coordinates>
        # 	</Point>
        # </Placemark>
        # <Placemark id="0B4EA6F59B1CA68601E0">
        # 	<name>Экскаватор</name>
        # 	<LookAt>
        # 		<longitude>61.23624067458115</longitude>
        # 		<latitude>52.17416232356366</latitude>
        # 		<altitude>277.5968564918906</altitude>
        # 		<heading>-0.5372217869872089</heading>
        # 		<tilt>53.57834275643886</tilt>
        # 		<gx:fovy>35</gx:fovy>
        # 		<range>2536.120178802812</range>
        # 		<altitudeMode>absolute</altitudeMode>
        # 	</LookAt>
        # 	<styleUrl>#__managed_style_047C2286A81CA685BFB3</styleUrl>
        # 	<Point>
        # 		<coordinates>61.23654046107902,52.16710625511239,297.4562999141254</coordinates>
        # 	</Point>
        # </Placemark>"""
        pass
        
##################################################################################################


import hashlib
from traceback import print_last

# hash_object = hashlib.md5("12345".encode())
hash_object = hashlib.sha256("key1".encode('utf-8'))
print(hash_object.hexdigest())

dict1 = {
    "key1": {"key1": {
        "key1": {"key1": "value1"},
        "key2": {"key1": "value1"},
    }},
    "key2": {"key1": "value1"},
}

numbers_orig = [5, 2, 6, 7, 8, 12, 15, 111]
words_orig = ["hello", 'Alice', "ball", 'eleven', '12']


def myBubbleSort(myList):
    for i in range(len(myList) - 1):
        for j in range(len(myList) - i - 1):
            if myList[j] < myList[j + 1]:
                temp = myList[j]
                myList[j] = myList[j + 1]
                myList[j + 1] = temp


print("Original list:")
print(numbers_orig)
myBubbleSort(numbers_orig)
print("Sorted list:")
print(numbers_orig)


class A:
    val1 = 12

    def __init__(self, val1) -> None:
        self.val = val1
        self.__val2 = val1 + 5


class B:
    val2 = 12

    def __init__(self, val1) -> None:
        pass


A.val1
A.val

n = [1, 2, 3, 4, 5]  # 1s

for i in n:
    pass  # i

n = [1, 2, 3, 4, 5, 6]  # 1s
h = [1, 2, 3, 4, 5]  # 1s

for i in n:
    for i in h:
        pass  # i

########################################################################################################################

# -*- coding: utf-8 -*-

# @Date    : 2018-10-12
# @Author  : Peng Shiyu

class CaesarCipher(object):
    """
    Цезарь шифрование и дешифрование
    """

    def __crypt(self, char, key):
        """
                 Зашифровать одну букву, смещение
                 @param char: {str} один символ
                 @param key: {num} смещение
                 @return: {str} зашифрованный символ
        """
        if not char.isalpha():
            return char
        else:
            base = "A" if char.isupper() else "a"
            return chr((ord(char) - ord(base) + key) % 26 + ord(base))

    def encrypt(self, char, key):
        """
                 Шифровать персонажей
        """
        return self.__crypt(char, key)

    def decrypt(self, char, key):
        """
                 Расшифровать символы
        """
        return self.__crypt(char, -key)

    def __crypt_text(self, func, text, key):
        """
               Зашифровать текст
               @param char: {str} текст
               @param key: {num} смещение
               @return: {str} зашифрованный текст
       """
        lines = []
        for line in text.split("\n"):
            words = []
            for word in line.split(" "):
                chars = []
                for char in word:
                    chars.append(func(char, key))
                words.append("".join(chars))
            lines.append(" ".join(words))
        return "\n".join(lines)

    def encrypt_text(self, text, key):
        """
                 Зашифровать текст
        """
        return self.__crypt_text(self.encrypt, text, key)

    def decrypt_text(self, text, key):
        """
                 Расшифровать текст
        """
        return self.__crypt_text(self.decrypt, text, key)


if __name__ == '__main__':
    plain = """
    you know? I love you!
    """
    key = 3

    cipher = CaesarCipher()

    # Шифрование
    print(cipher.encrypt_text(plain, key))
    # brx nqrz? L oryh brx!

    # Расшифровать
    print(cipher.decrypt_text("brx nqrz? L oryh brx!", key))
    # you know? I love you!

########################################################################################################################


