from picamera import Color, PiCamera

camera = PiCamera()
camera.rotation = 180
camera.annotate_background = Color('black')
