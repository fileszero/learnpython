# https://news.mynavi.jp/article/zeropython-34/

import cv2
img = cv2.imread("data/hama.jpg")
print(img.shape)

# グレイスケールに変換
gry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# ファイルに保存
cv2.imwrite("var/hama-gray.jpg", gry)

# ソーベルフィルタを適用
img2 = cv2.Sobel(img, cv2.CV_32F, 1, 0, ksize=5)
# ファイルに保存
cv2.imwrite("var/hama-sobel.jpg", img2)