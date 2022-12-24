########################################################################################################################
# TODO обработка изображений

import os
import cv2
import httplib2
import numpy

path = "python.jpg"

# C:\Project\Github_Projects\python-study\2_libraries\python.jpg - абсолютный
# dino.jpg - относительный

# img = пиксели (матрица)
img1 = cv2.imread(path, cv2.IMREAD_GRAYSCALE)  # читаем изображение по пути, с флагом для серого
img2 = cv2.imread(path, cv2.IMREAD_COLOR)  # читаем изображение по пути, с флагом для цветного

height, width, channels = img1.shape  # -> (1920, 1080, 3)
new_width = 1280
new_height = 720
quality = 95

cv2.waitKey(1)  # для задержки отображения кадра (если изображение, то нужен параметр 1)

# cv2.imshow('IMREAD_GRAYSCALE', img1)  # рендерит(отрисовывает на экране) массив пикселей - изображение
cv2.imshow('IMREAD_COLOR', img2)  # рендерит(отрисовывает на экране) массив пикселей - изображение

cv2.waitKey(1)  # для задержки отображения кадра (если изображение, то нужен параметр 1)

resized = cv2.resize(img1, (new_width // 2, new_height // 2), interpolation=cv2.INTER_AREA)
image_gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
cv2.imshow('image_gray', image_gray)  # рендерит(отрисовывает на экране) массив пикселей - изображение
cv2.waitKey(1)  # для задержки отображения кадра (если изображение, то нужен параметр 1)

# cv2.imwrite('dino2.jpg', img)
cv2.imwrite('temp/image_gray.jpg', image_gray, [cv2.IMWRITE_JPEG_QUALITY, quality])

image_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)  # BGR(RGB) -> GRAY
image = cv2.threshold(image_gray, 127, 255, cv2.THRESH_BINARY)[1]  # GRAY -> WHITE

image = cv2.resize(image, (width, height))

image_crop = image[150:250:1]  # обрезка

cv2.imwrite("image_data/dino_new.jpg", image, [cv2.IMWRITE_JPEG_QUALITY, quality])

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # BGR(RGB) -> GRAY
image = cv2.threshold(image_gray, 127, 255, cv2.THRESH_BINARY)[1]  # GRAY -> WHITE

image = cv2.resize(image, (width, height))

cv2.imwrite("image_data/dino_new.jpg", image, [cv2.IMWRITE_JPEG_QUALITY, quality])

cv2.destroyAllWindows()

# cam_stream = cv2.VideoCapture("video.mp4")
cam_stream = cv2.VideoCapture(0)
_, image = cam_stream.read()
cam_stream.release()


########################################################################################################################

def get_data_from_ip_cam():
    mask_char_field = []
    genericipaddress_field = "192.168.0.101"
    # Создание экземпляра объекта библиотеки, установка папки с кешем для библиотеки и таймаута
    h = httplib2.Http(cache="temp", timeout=3)
    # Установка логина от камеры
    login = 'admin'
    # Установка пароля от камеры
    password = 'q1234567'
    # Добавление логина и пароля к авторизации
    h.add_credentials(login, password)
    # Заполнение api-пути для получения изображения по сети от камеры
    sources = f'http://{genericipaddress_field}:80/ISAPI/Streaming/channels/101/picture?snapShotImageType=JPEG'
    # Установка заголовка для запроса
    headers = {
        'user-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    }
    # Получение данных с api камеры
    response, content = h.request(uri=sources, method="GET", headers=headers)
    # Чтение изображения-маски
    mask = cv2.imread(mask_char_field, 0)
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
    print(value)


def render_origin(image, name, resolution_debug):
    render(name=f"origin : {name}", source=image, resolution_debug=resolution_debug)


def render_cropping_image(image, name, resolution_debug):
    cropping_image = image[250:1080, 600:1720]
    render(name=f"cropping_image : {name}", source=cropping_image,
           resolution_debug=resolution_debug)


def render_bitwise_not_white(image, mask, name, resolution_debug):
    bitwise_not = cv2.bitwise_not(image, image, mask=mask)
    render(name=f"_bitwise_not_white : {name}", source=bitwise_not,
           resolution_debug=resolution_debug)


def render_bitwise_and(image, mask, name, resolution_debug):
    bitwise_and = cv2.bitwise_and(image, image, mask=mask)
    render(name=f"bitwise_and : {name}", source=bitwise_and, resolution_debug=resolution_debug)


def render_threshold(image, name, resolution_debug):
    _, threshold = cv2.threshold(image, 220, 255, cv2.THRESH_BINARY_INV)
    render(name=f"threshold : {name}", source=threshold, resolution_debug=resolution_debug)


def render_cvtcolor_to_hsv(image, name, resolution_debug):
    cvtcolor = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    render(name=f"cvtcolor_to_hsv : {name}", source=cvtcolor,
           resolution_debug=resolution_debug)


def render_inrange(image, sensitivity_analysis, name, resolution_debug):
    cvtcolor = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    inrange = cv2.inRange(cvtcolor, numpy.array([0, 0, 255 - sensitivity_analysis], dtype=numpy.uint8),
                          numpy.array([255, sensitivity_analysis, 255], dtype=numpy.uint8))
    render(name=f"inrange : {name}", source=inrange, resolution_debug=resolution_debug)


def render_canny_edges(image, sensitivity_analysis, name, resolution_debug):
    canny = cv2.Canny(image, sensitivity_analysis, sensitivity_analysis, apertureSize=3, L2gradient=True)
    render(name=f"canny_edges : {name}", source=canny, resolution_debug=resolution_debug)


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
    render(name=f"shapes : {name}", source=img, resolution_debug=resolution_debug)


def render_cvtcolor(image, color_type, name, resolution_debug):
    cvtcolor = cv2.cvtColor(image, color_type)
    render(name=f"cvtcolor : {name}", source=cvtcolor, resolution_debug=resolution_debug)


def render_flip(image, flipcode, name, resolution_debug):
    flip = cv2.flip(image, flipcode)
    render(name=f"flip : {name}", source=flip, resolution_debug=resolution_debug)


def render_final(image, mask, sensitivity_analysis, correct_coefficient, name, resolution_debug):
    bitwise_and = cv2.bitwise_and(image, image, mask=mask)
    cvtcolor = cv2.cvtColor(bitwise_and, cv2.COLOR_BGR2HSV)
    inrange = cv2.inRange(cvtcolor, numpy.array([0, 0, 255 - sensitivity_analysis], dtype=numpy.uint8),
                          numpy.array([255, sensitivity_analysis, 255], dtype=numpy.uint8))
    cv2.putText(inrange,
                f"{numpy.sum(inrange > 0) / numpy.sum(mask > 0) * 100 * correct_coefficient:0.2f}%",
                (int(1920 / 5), int(1080 / 2)), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 255, 255), 3)
    render(name=f"final : {name}", source=inrange, resolution_debug=resolution_debug)


def render(name: str, source, resolution_debug: list):
    try:
        if source is not None:
            img = cv2.resize(source, (resolution_debug[0], resolution_debug[1]),
                             interpolation=cv2.INTER_AREA)
            cv2.imshow(name, img)
    except Exception as ex:
        print(ex)


def result_final(image, mask, sensitivity_analysis, correct_coefficient):
    bitwise_and = cv2.bitwise_and(image, image, mask=mask)
    cvtcolor = cv2.cvtColor(bitwise_and, cv2.COLOR_BGR2HSV)
    inrange = cv2.inRange(cvtcolor, numpy.array([0, 0, 255 - sensitivity_analysis], dtype=numpy.uint8),
                          numpy.array([255, sensitivity_analysis, 255], dtype=numpy.uint8))
    try:
        return round(numpy.sum(inrange > 0) / numpy.sum(mask > 0) * 100 * correct_coefficient, 2)
    except Exception as ex:
        print(f'result_final func error : {ex}')
        return 0.0


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
