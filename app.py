import cv2
from kivy.metrics import dp
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture

class CameraApp(App):
    def build(self):
        # Crear la interfaz de usuario
        layout = BoxLayout(orientation='vertical')

        # División de la pantalla en 25%, 50% y 25%

        # Primer 25% con fondo azul y una imagen al centro
        header = BoxLayout(size_hint=(1, 0.25))
        header.canvas.add(Color(0, 0, 1))  # Color azul
        header.canvas.add(Rectangle(pos=header.pos, size=header.size))
        logo = Image(source='logo.png', size_hint=(None, None), size=(dp(100), dp(100)))
        header.add_widget(logo)
        layout.add_widget(header)

        # 50% para la imagen de la cámara
        # Crear un widget de imagen para mostrar el video de la cámara
        self.img = Image()

        # Agregar la imagen al diseño
        layout.add_widget(self.img)

        # Último 25% con un recuadro blanco y margen de separación
        footer = BoxLayout(size_hint=(1, 0.25))
        footer.padding = [0, dp(10)]  # Margen del 5%
        footer.canvas.add(Color(1, 1, 1))  # Color blanco
        footer.canvas.add(Rectangle(pos=footer.pos, size=footer.size))
        layout.add_widget(footer)

        # Iniciar la captura de video
        self.capture = cv2.VideoCapture(0)

        # Llamar al método update() cada 1/30 segundos
        Clock.schedule_interval(self.update, 1.0 / 30.0)

        return layout

    def update(self, dt):
        # Capturar frame de la cámara
        ret, frame = self.capture.read()

        if ret:
            # Convertir el frame de BGR a RGB
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Crear una textura Kivy desde el frame
            buf1 = cv2.flip(frame_rgb, 0)
            buf = buf1.tostring()
            texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='rgb')
            texture.blit_buffer(buf, colorfmt='rgb', bufferfmt='ubyte')

            # Actualizar la imagen
            self.img.texture = texture

    def on_stop(self):
        # Liberar la cámara al cerrar la aplicación
        self.capture.release()

if __name__ == '__main__':
    CameraApp().run()
