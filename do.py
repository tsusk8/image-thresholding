import cv2
import glob
from tkinter import filedialog
import pathlib

threshold  = 4
file_types = [("all files", "*"), ("jpeg", "*.jpeg"), ("JPEG", "*.JPEG")]

# ファイルを一枚選択する
def selectAFile():
    global threshold
    global file_types

    file = filedialog.askopenfilename(file_types=file_types)
    img  = cv2.imread(file)

    controllThresholding(file, img)

def selectFiles():
    global threshold
    global file_types

    files = filedialog.askopenfilenames(file_types=file_types)
    
    loopThresholding(files)

# ループ文で1枚ずつ処理を実施
def loopThresholding(files):
    for file in files:
        img = cv2.imread(file)

        controllThresholding(file, img)

# フォルダーを選択する
def selectADirectory():
    global threshold

    target_path = filedialog.askdirectory()
    files       = glob.glob(target_path+'/*.jpeg')

    loopThresholding(files)
        
# 閾値処理の実施
def doThresholding(img):
    gray   = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    binary = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)

    return binary

def controllThresholding(file, img):
    binary    = doThresholding(img)
    file_name = pathlib.PurePath(file).stem

    cv2.imwrite('thresholding-' + file_name + '.jpeg', binary)

print('Enter "1" if only one photo is to be processed.')
print('Enter "2" for multiple photos.')
print('To select all the photos in a folder, enter any other value.')

choose = input()

if (choose == '1'):
    selectAFile()
elif (choose == '2'):
    selectFiles()
else:
    selectADirectory()