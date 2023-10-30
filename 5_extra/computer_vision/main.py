import cv2
from cv2 import Mat

# чтение изображения в цвете(или через api от камеры hikvision/dahua)
source: Mat = cv2.imread("16_1.jpg", cv2.IMREAD_COLOR)
# изменение размера
source = cv2.resize(source, (640, 480), interpolation=cv2.INTER_AREA)
print(type(source), len(source))
# вывод на дисплей
cv2.imshow("source", source)

# чтение маски в ч/б
mask: Mat = cv2.imread("m_16_1.jpg", 0)
mask = cv2.resize(mask, (640, 480), interpolation=cv2.INTER_AREA)
cv2.imshow("mask", mask)

# bitwise_and - https://www.educba.com/opencv-bitwise_and/
# побитовые операции умножения, "для отсечения ненужной области"
bitwise_and = cv2.bitwise_and(src1=source, src2=source, mask=mask)
cv2.imshow("bitwise_and", bitwise_and)

# cvtColor - https://www.geeksforgeeks.org/python-opencv-cv2-cvtcolor-method/
# превращение в HSV
cvt_color = cv2.cvtColor(bitwise_and, cv2.COLOR_BGR2HSV)
cv2.imshow("cvt_color", cvt_color)

# cvt_color.convertTo  - https://docs.opencv.org/3.4/de/d25/imgproc_color_conversions.html
# добавление яркости всему изображению
# BrightLevel = 50
# cvt_color2 = cvt_color.convertTo(-1, -1, (BrightLevel - 50))
# cv2.imshow("cvt_color2", cvt_color2)

# inRange - https://docs.opencv.org/3.4/da/d97/tutorial_threshold_inRange.html
# "разделение всего пространства HSV на 2 цвета по диапазону"
point_1_1 = 0
point_1_2 = 0
point_1_3 = 160  # TODO нужно менять для увеличения/уменьшения чувствительности
point_2_1 = 255
point_2_2 = 25  # TODO нужно менять для уменьшения/укрупнения плотности
point_2_3 = 255
in_range = cv2.inRange(cvt_color,(point_1_1, point_1_2 ,point_1_3),(point_2_1, point_2_2, point_2_3))
cv2.imshow("in_range", in_range)

cv2.waitKey(0)
cv2.destroyAllWindows()

# минимальный уровень для значений маски
CountNotZero = 1
# финальный множитель для корректировки значения
CorrectCoefficient = 1.0

# countNonZero - метод, для посчёта "не нулевых" значений в матрице
# result = cv2.countNonZero(final > CountNotZero) / cv2.countNonZero(mask) * 100 * CorrectCoefficient

# всё, что меньше этого уровня превращается в ноль(для защиты от всплесков)
NullLevel = 10
