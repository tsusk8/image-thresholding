import cv2
import glob
from tkinter import filedialog
import pathlib

# 閾値の設定
threshold = 4

# ファイル拡張子の設定
fTyp = [("all files", "*"), ("jpeg", "*.jpeg"), ("JPEG", "*.JPEG")]

# ファイルを一枚選択する
def selectAFile():
    global threshold
    global fTyp

    # ファイル取得
    file = filedialog.askopenfilename(filetypes=fTyp)

    # jpegファイルの読み込み
    img = cv2.imread(file)

    # しきい値処理の実施
    controllThresholding(file, img)

def selectFiles():
    global threshold
    global fTyp

    # ファイル取得
    files = filedialog.askopenfilenames(filetypes=fTyp)
    
    # ループ文で処理を実施
    loopThresholding(files)

# ループ文で1枚ずつ処理を実施
def loopThresholding(files):
    for file in files:
        # jpegファイルの読み込み
        img = cv2.imread(file)

        # しきい値処理の実施
        controllThresholding(file, img)

# フォルダーを選択する
def selectADirectory():
    global threshold

    # 対象のフォルダー選択
    target_path = filedialog.askdirectory()

    # 対象のフォルダー内のjpegのみを取得
    files = glob.glob(target_path+'/*.jpeg')

    # ループ文で処理を実施
    loopThresholding(files)
        
# しきい値処理の実施
def doThresholding(img):
    # cvtColorで変換かける
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # バイナリー化
    ret, binary = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)

    return binary

def controllThresholding(file, img):
    # jpegファイル変換処理
    binary = doThresholding(img)
    
    # ファイル名取得
    file_name = pathlib.PurePath(file).stem

    # 画像保存処理
    cv2.imwrite('thresholding-' + file_name + '.jpeg', binary)

print('how many select your picture?')
choose = input()

# 使い方

# 写真を1枚だけでチェックしたい場合は、「1」を入力
# 写真を複数枚チェックしたい場合は、「2」を入力
# 写真をフォルダーごとチェックしたい場合は「1」、「2」以外を入力

if (choose == '1'):
    selectAFile()
elif (choose == '2'):
    selectFiles()
else:
    selectADirectory()