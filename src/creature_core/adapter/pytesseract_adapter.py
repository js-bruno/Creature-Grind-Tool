from creature_core.domain.adapter import OpticalRecognition
import pytesseract


class PytesseractAdapter(OpticalRecognition):
    def image_to_string(self, img):
        return pytesseract.image_to_string(img)
