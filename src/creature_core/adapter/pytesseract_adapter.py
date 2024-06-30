import pytesseract

from creature_core.domain.adapter import OpticalRecognition


class PytesseractAdapter(OpticalRecognition):
    def image_to_string(self, img):
        return pytesseract.image_to_string(img, config="--psm 3")
