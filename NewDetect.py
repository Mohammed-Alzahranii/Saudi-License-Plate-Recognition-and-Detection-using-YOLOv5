import os
import sys
from pathlib import Path

from collections import defaultdict

from PIL import Image

import torch
import torch.backends.cudnn as cudnn

from models.common import DetectMultiBackend
from utils.datasets import LoadImages, LoadStreams
from utils.general import (check_img_size, cv2,increment_path, non_max_suppression, scale_coords)
from utils.plots import Annotator, colors, save_one_box
from utils.torch_utils import select_device, time_sync

from GUI.LoginWindow import UI_WelcomingPage
from GUI.LoginWindow import UI_Admin

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPixmap

from PyQt6.QtGui import QPixmap

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path).replace('\\', '/')

################################################################################################
def StartDetection():
    device = select_device('cpu')
    PlateModel, CharModel = LoadModels()

    PlateModel.to(device)
    CharModel.to(device)
    cudnn.benchmark = True

    visualize = False
    augment = False
    ImgSize = (608,608)

    DetectPlate(PlateModel, CharModel, ImgSize, visualize, device)

def LoadModels():
    device = select_device('cpu')
    Plate_model = DetectMultiBackend(resource_path('weights/best_Plate.pt'), device=device, dnn=False, data=resource_path('data.yaml'), fp16=False)
    Characters_model = DetectMultiBackend(resource_path('weights/recognition_best.pt'), device=device, dnn=False, data=resource_path('data.yaml'), fp16=False)
    return Plate_model, Characters_model

################################################################################################

def PredicatePlate(PlateModel=None, im=None, path=None, visualize=False, augment=False, device=''):
    dt, seen = [0.0, 0.0, 0.0], 0
    t1 = time_sync()
    im = torch.from_numpy(im).to(device)
    im = im.half() if PlateModel.fp16 else im.float()  # uint8 to fp16/32
    im /= 255  # 0 - 255 to 0.0 - 1.0
    if len(im.shape) == 3:
        im = im[None]  # expand for batch dim
    t2 = time_sync()
    dt[0] += t2 - t1

    # Inference
    visualize = increment_path(resource_path('Out/' / Path(path).stem), mkdir=True) if visualize else False
    pred = PlateModel(im, augment=augment, visualize=visualize)

    t3 = time_sync()
    dt[1] += t3 - t2

    # NMS
    pred = non_max_suppression(pred, .75, .45, None, False, max_det=1)
    dt[2] += time_sync() - t3
    return pred


def GetPlateModelData(PlateModel):
    stride, names, pt = PlateModel.stride, PlateModel.names, PlateModel.pt
    return stride, names, pt


def DetectPlate(PlateModel, CharModel, ImgSize, visualize, device):

    ###########
    app = QtWidgets.QApplication(sys.argv)
    LicensePlateProject = QtWidgets.QMainWindow()
    UI = UI_WelcomingPage()
    UI.setupUi(LicensePlateProject)
    LicensePlateProject.show()
    ###########

    stride, names, pt = GetPlateModelData(PlateModel)
    CheckImg = check_img_size(ImgSize, s=stride)  # check image size


    # Start Webcam
    dataset = LoadStreams('0', CheckImg, stride=stride, auto=pt)
    PlateModel.warmup(imgsz=(1 if pt else len(dataset.img_size), 3, *ImgSize))  # warmup


    UserUI = UI.get_UI()
    dt, seen = [0.0, 0.0, 0.0], 0

    for path, im, im0s, vid_cap, s in dataset:
        UserUI = UI.get_UI()

        if UI.StartDet is True:
            try:
                LastFrameImage = im0s  # The main frame

                Pred = PredicatePlate(PlateModel, im, path, visualize, False, device)
                for i, det in enumerate(Pred):  # per image ( LastFrameImage is important )
                    seen += 1
                    p, LastFrameImage, frame = path[i], im0s[i].copy(), dataset.count
                    annotator = Annotator(LastFrameImage, line_width=3, example=str(names))

                    if len(det):  # if we found something
                        det[:, :4] = scale_coords(im.shape[2:], det[:, :4], annotator.im.shape).round()

                        for *xyxy, conf, cls in reversed(det):  # Loop trhough detected things
                            c = int(cls)
                            CroppedImg = save_one_box(xyxy, LastFrameImage, pad=20, BGR=True, save=False)
                            annotator.box_label(xyxy, f'{names[c]} {conf:.2f}', color=colors(c, True))
                            LastFrameImage = annotator.result()

                            cv2.imwrite(resource_path("Out/DetectedPlate.png"), CroppedImg)

                            original = Image.open(resource_path('Out/DetectedPlate.png'))
                            width, height = original.size
                            ArabicPart = original.crop((0, 0, width, height / 2))
                            EnglishPart = original.crop((0, height / 2, width, height))
                            EnglishPart.save(resource_path('Out/EnglishPart.png'))
                            ArabicPart.save(resource_path('Out/ArabicPart.png'))

                            LastFrameImage = DetectCharacters(CharModel, UserUI, ArabicPart.width, ArabicPart.height, annotator, resource_path('Out/EnglishPart.png'), (480, 480), visualize, device)

                cv2.imwrite(resource_path('Out/Frame.png'), LastFrameImage)
                UserUI.Frame.setPixmap(QPixmap(resource_path('Out/Frame.png')))

            except Exception as e:
                print(e)

################################################################################################

def PredicateChars(CharModel=None, im=None, path=None, visualize=False, augment=False, device=''):
    dt, seen = [0.0, 0.0, 0.0], 0
    t1 = time_sync()
    im = torch.from_numpy(im).to(device)
    im = im.half() if CharModel.fp16 else im.float()  # uint8 to fp16/32
    im /= 255  # 0 - 255 to 0.0 - 1.0
    if len(im.shape) == 3:
        im = im[None]  # expand for batch dim
    t2 = time_sync()
    dt[0] += t2 - t1

    # Inference
    visualize = increment_path('Out/' / Path(path).stem, mkdir=True) if visualize else False
    pred = CharModel(im, augment=augment, visualize=visualize)

    t3 = time_sync()
    dt[1] += t3 - t2

    # NMS
    pred = non_max_suppression(pred, .8, .45, None, False, max_det=100)
    dt[2] += time_sync() - t3
    return pred


def GetCharsModelData(CharModel):
    stride, names, pt = CharModel.stride, CharModel.names, CharModel.pt
    return stride, names, pt


def DetectCharacters(CharModel, UI, OffsetX, OffsetY, annotator, ImgPath, ImgSize, visualize, device):
    stride, names, pt = GetPlateModelData(CharModel)
    CheckImg = check_img_size(ImgSize, s=stride)  # check image size

    data_dict = defaultdict(list)

    # Start Webcam
    dataset = LoadImages(ImgPath, CheckImg, stride=stride, auto=pt)
    CharModel.warmup(imgsz=(1 if pt else len(dataset.img_size), 3, *ImgSize))  # warmup

    dt, seen = [0.0, 0.0, 0.0], 0
    for path, im, im0s, vid_cap, s in dataset:
        Pred = PredicateChars(CharModel, im, path, visualize, False, device)

        for i, det in enumerate(Pred):  # per image ( LastFrameImage is important )
            seen += 1
            p, LastFrameImage, frame = path[i], im0s[i].copy(), dataset.count

            if len(det):  # if we found something
                for *xyxy, conf, cls in reversed(det):  # Loop through detected things
                    c = int(cls)
                    # Storing position with value [ X, 'A' ]..
                    data_dict[xyxy[0]].append(names[int(c)])

        AR_Letter, AR_Number, EN_Letter, EN_Number = TranslateLicensePlate(data_dict)

        UI.ShowResults(EN_Letter, EN_Number, AR_Letter, AR_Number)

        return annotator.result()


def TranslateLicensePlate(data_dict):

    ##########################
    idx = 3
    EnglishChars = 'ABJDRSXTEGKLZNHUV'
    EnglishNums = '0123456789'
    ArabicChars = 'ابحدرسصطعقكلمنهوي'
    ArabicNums = '٠١٢٣٤٥٦٧٨٩'
    ##########################

    EnglishLetter = []
    EnglishNumber = []
    for x, y in sorted(data_dict.items()):
        One = str(y).translate({ord(']'): None})
        Two = str(One).translate({ord('['): None})
        Three = str(Two).translate({ord('\''): None})
        if Three.isdigit():
            EnglishNumber.append(Three)
        else:
            EnglishLetter.append(Three)

    FinalEnglishPlate = ''
    for n in EnglishLetter:
        FinalEnglishPlate = FinalEnglishPlate + n

    FinalEnglishPlate = FinalEnglishPlate + ' '

    for n in EnglishNumber:
        FinalEnglishPlate = FinalEnglishPlate + n

    SaudiLetter = []
    SaudiNumber = []
    for n in FinalEnglishPlate:
        AR_CharIdx = EnglishChars.find(n)
        AR_NumIdx = EnglishNums.find(n)
        if AR_CharIdx >= 0:
            SaudiLetter.append(ArabicChars[AR_CharIdx])
        if AR_NumIdx >= 0:
            SaudiNumber.append(ArabicNums[AR_NumIdx])

    SaudiLetter.reverse()
    SaudiNumber.reverse()

    FinalSaudiPlate = ''
    for n in SaudiLetter:
        FinalSaudiPlate = FinalSaudiPlate + n + ' '
    for n in SaudiNumber:
        FinalSaudiPlate = FinalSaudiPlate + n

    FinalSaudiLetter = ''
    FinalSaudiNumber = ''
    FinalEnglishLetter = ''
    FinalEnglishNumber = ''
    for n in SaudiNumber:
        FinalSaudiNumber = FinalSaudiNumber + n + ' '
    for n in SaudiLetter:
        FinalSaudiLetter = FinalSaudiLetter + n + ' '
    for n in EnglishLetter:
        FinalEnglishLetter = FinalEnglishLetter + n
    for n in EnglishNumber:
        FinalEnglishNumber = FinalEnglishNumber + n

    FinalEnglishLetter = ' ' + FinalEnglishLetter

    return FinalSaudiLetter, FinalSaudiNumber, FinalEnglishLetter, FinalEnglishNumber


################################################################################################

if __name__ == "__main__":
    StartDetection()
