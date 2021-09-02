import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'



def image_convert(img):
    img = Image.open(img) #cv2.imread("dnd.png")
    text = pytesseract.image_to_string(img)
    return text

def img_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def remove_noice(image):
    return cv2.medianBlur(image, 5)

def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

#img = img_grayscale(img)
#img = thresholding(img)
#img = remove_noice(img)
