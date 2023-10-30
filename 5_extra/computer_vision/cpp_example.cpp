void AsyncThreadClass::finishDownload()
{
    try {
        QByteArray data = reply->readAll();
        cv::Mat image_source;
        QPixmap qPixmap;
        if (qPixmap.loadFromData(data, "JPG")) {
            QImage qImage = qPixmap.toImage();
            image_source = cv::Mat(qImage.height(), qImage.width(), CV_8UC4, const_cast<uchar*>(qImage.bits()), static_cast<size_t>(qImage.bytesPerLine()));
            std::string ResourcesCam = UtilitesClass::GetValueFromMap(AllSettings, "ResourcesCam") + UtilitesClass::GetValueFromMap(OneSettings, "MaskCam");
            cv::Mat mask = cv::imread(ResourcesCam, 0);
            cv::Mat bitwise_and;
            cv::bitwise_and(image_source, image_source, bitwise_and, mask);
            cv::Mat cvtcolor;
            cv::cvtColor(bitwise_and, cvtcolor, cv::COLOR_BGR2HSV);
            cvtcolor.convertTo(cvtcolor, -1, 1, std::stoi((UtilitesClass::GetValueFromMap(OneSettings, "BrightLevel"))) - 50);
            image_source.convertTo(image_source, -1, 1, std::stoi((UtilitesClass::GetValueFromMap(OneSettings, "BrightLevel"))) - 50);
            cv::Mat final;
            cv::inRange(cvtcolor, cv::Scalar(std::stoi(UtilitesClass::GetValueFromMap(OneSettings, "Point_1_1")),
                                             std::stoi(UtilitesClass::GetValueFromMap(OneSettings, "Point_1_2")),
                                             std::stoi(UtilitesClass::GetValueFromMap(OneSettings, "Point_1_3"))),
                        cv::Scalar(std::stoi(UtilitesClass::GetValueFromMap(OneSettings, "Point_2_1")),
                                   std::stoi(UtilitesClass::GetValueFromMap(OneSettings, "Point_2_2")),
                                   std::stoi(UtilitesClass::GetValueFromMap(OneSettings, "Point_2_3"))), final);
            final.setTo(std::stoi(UtilitesClass::GetValueFromMap(OneSettings, "InRangeSetTo")), final >= std::stoi(UtilitesClass::GetValueFromMap(OneSettings, "InRangeSetFrom")));
            double result = double(cv::countNonZero(final > std::stoi(UtilitesClass::GetValueFromMap(OneSettings, "CountNotZero")))) / double(cv::countNonZero(mask)) * 100 * std::stod(UtilitesClass::GetValueFromMap(OneSettings, "CorrectCoefficient"));
            if (result > 100)
            {
                result = 100.0;
            }
            else if(result < 0)
            {
                result = 0.0;
            }
            else
            {
                float pow_10 = pow(10.0f, (float)2);
                result = round(result * pow_10) / pow_10;
                if (result < std::stod(UtilitesClass::GetValueFromMap(OneSettings, "NullLevel"))) {
                    result = 0.0;
                }
            }
        }
    }  catch (std::string error) {
        UtilitesClass::WriteTextErrorToLogFile(error);
    }
    delete this;
}