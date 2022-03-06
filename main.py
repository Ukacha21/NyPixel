from tkinter import *
from tkinter import filedialog
from PIL import Image as PILImage
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatIconButton, MDIconButton
from kivy.uix.image import Image as kimage
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivy.uix.screenmanager import ScreenManager

rtk = Tk()
rtk.geometry("1x1")
rtk.overrideredirect(1)



class AnyPixel(MDApp):

    def browsePic(*args):
        try:
            global image
            image = filedialog.askopenfilename(filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("icon files", "*.ico")])
            global nextPic
            nextPic = PILImage.open(image)

            homeLabel.text="File open\n1.Enter width and height down\n2. Press Resize Button"
    

            
        except AttributeError:
            homeLabel.text="Sorry, we couldn't open it\nwould you like to try it again?"
    

    def savePic(*args):
        #del setOne
        #del setTwo
        try:
            print(newPic)

            newPic.save(filedialog.asksaveasfilename(filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("icon files", "*.ico")]))
            homeLabel.text="Saved Successfully!"
        except NameError:
            homeLabel.text="Please make sure you followed the steps above"
    
    def resizePic(*args):
        try:
            width = int(resX.text)
            height = int(resY.text)

            global newPic
            newPic = nextPic.resize((width, height), PILImage.ANTIALIAS)
            homeLabel.text="Successfully resized\n You can save it now..."
            print(width, height)
        except:
            homeLabel.text="Something went wrong\nplease try again..."

    state = 0
    def invert_colors(self, *args):
        if self.state == 0:
            self.theme_cls.theme_style = "Dark"
            self.state = 1
        elif self.state == 1:
            self.theme_cls.theme_style = "Light"
            self.state = 0

    def build(self):
        #self.theme_cls.material_style = "M3"
        self.theme_cls.theme_style = "Light"
        
        #['Red', 'Pink', 'Purple', 'DeepPurple', 'Indigo', 'Blue', 'LightBlue', 'Cyan', 'Teal', 
        #'Green', 'LightGreen', 'Lime', 'Yellow', 'Amber', 'Orange', 'DeepOrange', 'Brown', 'Gray', 'BlueGray']
        self.theme_cls.primary_palette = "Teal"
        #self.theme_cls.secondary_palette = "Yellow"
        #scrManager = ScreenManager()
        self.icon = "logo.png"
        
        global smanager
        smanager = ScreenManager()

        global root
        root = MDScreen()
        global infoScreen
        infoScreen = MDScreen()

        smanager.add_widget(root)
        
        root.add_widget(
            kimage(
                source = "logo.png",
                pos_hint = {"center_x": .5, "center_y": .4},

            )
        )


        hometext = "Please start by uploding your file\nusing the upload botton below"
        global homeLabel
        homeLabel = MDLabel(
            text = hometext,
            font_style="H5",
            pos_hint = {"center_x": .5, "center_y": .8},
            halign="center",
            font_size="100sp"
            )


        colorButton = MDIconButton(
            icon="invert-colors",
            pos_hint = {"center_x": .9, "center_y": .9},
            on_press = self.invert_colors
        )

        global resX
        resX = MDTextField(
            hint_text="enter width in pixels",
            helper_text= "this field is required",
            helper_text_mode = "on_error",
            required = True,
            size_hint = (.5, 1),
            #max_text_length = 8,
            #multiline = False,
            pos_hint = {"center_x": .5, "center_y": .5}
            )

        global resY
        resY = MDTextField(
            hint_text="enter height in pixels",
            helper_text= "this field is required",
            helper_text_mode = "on_error",
            required = True,
            size_hint = (.5, 1),
            #max_text_length = 8,
            #multiline = False,
            pos_hint = {"center_x": .5, "center_y": .3}
            )

        brosweButton = MDRectangleFlatIconButton(
            icon = "file-upload",
            text="open",
            pos_hint = {"center_x": .5, "center_y": .6},
            on_press = self.browsePic

            )

        resizeButton = MDRectangleFlatIconButton(
            icon = "file-upload",
            text="Resize",
            pos_hint = {"center_x": .4, "center_y": .1},
            on_press = self.resizePic

            )

        saveButton = MDRectangleFlatIconButton(
            icon = "floppy",
            text="save",
            pos_hint = {"center_x": .6, "center_y": .1},
            on_press = self.savePic

        )


        root.add_widget(homeLabel)
        root.add_widget(resX)
        root.add_widget(resY)
        root.add_widget(brosweButton)
        root.add_widget(resizeButton)
        root.add_widget(saveButton)
        root.add_widget(colorButton)

        



        return smanager
AnyPixel().run()


