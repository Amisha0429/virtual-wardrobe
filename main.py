# A Wardrobe app that automates closet to craete outfits.

# Import modules
import os
import random
import tkinter as tk
from PIL import Image, ImageTk


# To open folders and make a list
# ALL_HOODIES is the list of all items in 'hoodies' folder
# ALL_BOTTOMS is the list of all items in 'bottoms' folder
ALL_HOODIES = [str("hoodies/") + file for file in os.listdir("hoodies/") if not file.startswith('.')]
ALL_BOTTOMS = [str("bottoms/") + file for file in os.listdir("bottoms/") if not file.startswith('.')]


# Class for the WardrobeApp
class WardrobeApp:
    
    
    def __init__(self, root):
        self.root = root # Root window

        # Tops and bottoms
        self.hoodie_images = ALL_HOODIES
        self.bottom_images = ALL_BOTTOMS
        self.hoodies_image_path = self.hoodie_images[0] # Initial picture for hoodie
        self.bottom_image_path = self.bottom_images[0] # Initial picture for bottom

        # The 2 frames in app that will display the hoodies and bottoms
        self.hoodies_frame = tk.Frame(self.root, bg='#746D69')
        self.bottoms_frame = tk.Frame(self.root, bg='#746D69')

        # Adding top to the frame
        self.hoodie_image_label = self.apply_photo(self.hoodies_image_path, self.hoodies_frame)
        self.hoodie_image_label.pack(side=tk.TOP)

        # Adding bottom to the frame
        self.bottom_image_label = self.apply_photo(self.bottom_image_path, self.bottoms_frame)
        self.bottom_image_label.pack(side=tk.TOP)

        self.make_background()


    # To create background using width and height and adding initial clothes
    def make_background(self):
        self.root.title('Virtual Wardrobe') # Title for the Root window
        self.root.geometry("500x800") # Width x Height of Window
        self.make_buttons()
        
        self.hoodies_frame.pack(fill=tk.BOTH, expand=tk.YES)
        self.bottoms_frame.pack(fill=tk.BOTH, expand=tk.YES)


    # To create buttons to interchange hoodies/bottoms and create outfit
    def make_buttons(self):
        top_prev_button = tk.Button(self.hoodies_frame, text="<", command=self.get_prev_hoodie)
        top_prev_button.pack(side=tk.LEFT)

        create_outfit_button = tk.Button(self.hoodies_frame, text="Create Outfit", command=self.make_outfit)
        create_outfit_button.pack(side=tk.LEFT)

        top_next_button = tk.Button(self.hoodies_frame, text=">", command=self.get_next_hoodie)
        top_next_button.pack(side=tk.RIGHT)

        bottom_prev_button = tk.Button(self.bottoms_frame, text="<", command=self.get_prev_bottom)
        bottom_prev_button.pack(side=tk.LEFT)

        bottom_next_button = tk.Button(self.bottoms_frame, text=">", command=self.get_next_bottom)
        bottom_next_button.pack(side=tk.RIGHT)


    def apply_photo(self, image, frame):
        top_image_file = Image.open(image)
        image = top_image_file.resize((300, 300), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(frame, image=photo, anchor=tk.CENTER)
        image_label.image = photo

        return image_label


    def update_photo(self, new_image, image_label):
        new_image_file = Image.open(new_image)
        image = new_image_file.resize((300, 300), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        image_label.configure(image=photo)
        image_label.image = photo


    def get_next(self, current_item, category, increment=True):
        item_index = category.index(current_item)
        final_index = len(category) - 1
        next_index = 0

        if increment and item_index == final_index:
            next_index = 0  # The clothing items starts back from beginning
        elif not increment and item_index == 0:
            next_index = final_index  # The clothing item starts from the end
        else:
            incrementor = 1 if increment else -1
            next_index = item_index + incrementor

        next_image = category[next_index]

        # reset the image object
        if current_item in self.hoodie_images:
            image_label = self.hoodie_image_label
            self.hoodies_image_path = next_image
        else:
            image_label = self.bottom_image_label
            self.bottom_image_path = next_image

        # update the photo
        self.update_photo(next_image, image_label)


    def get_next_hoodie(self):
        self.get_next(self.hoodies_image_path, self.hoodie_images, increment=True)


    def get_prev_hoodie(self):
        self.get_next(self.hoodies_image_path, self.hoodie_images, increment=False)


    def get_prev_bottom(self):
        self.get_next(self.bottom_image_path, self.bottom_images, increment=False)


    def get_next_bottom(self):
        self.get_next(self.bottom_image_path, self.bottom_images, increment=True)


    def make_outfit(self):
        # To select an outfit randomly
        new_hoodie_index = random.randint(0, len(self.hoodie_images)-1)
        new_bottom_index = random.randint(0, len(self.bottom_images)-1)

        # To add the clothes onto the screen
        self.update_photo(self.hoodie_images[new_hoodie_index], self.hoodie_image_label)
        self.update_photo(self.bottom_images[new_bottom_index], self.bottom_image_label)


if __name__ == '__main__':
    root = tk.Tk()
    app = WardrobeApp(root)
    root.mainloop()
