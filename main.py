'''
@author: KhomZ
'''
from captcha.image import ImageCaptcha
from captcha.audio import AudioCaptcha


image = ImageCaptcha()
audio = AudioCaptcha()


data = audio.generate('1234')
audio.write('1234', '1.wav')
# data = audio.generate('abcd')
# audio.write('abcd', '1.wav')

data = image.generate('1234')
image.write('1234', '1.png')
# data = image.generate('abcd')
# image.write('abcd', '1.png')


# if __name__ == '__main__':
#     main()
