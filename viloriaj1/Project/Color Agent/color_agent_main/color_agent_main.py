import tkinter as tk
from PIL import Image, ImageTk  # Import Pillow modules
from tkinter import scrolledtext

def countdown(count):

    waiting_dots = "." * 5
    
    if count > 0:
        # 2. Call this countdown function again after 1000ms (1 second)
        root.after(1000, countdown, count - 1)
        textbox_result.config(state="normal") # Enable result textbox
        textbox_result.insert(tk.END, waiting_dots) # Enter user input to texbox
        textbox_result.config(state="disabled") # response textbox disable
    else:
        textbox_result.config(state="normal") # Enable result textbox
        textbox_result.insert(tk.END, "Search is finished!\n") # Enter user input to texbox
        textbox_result.config(state="disabled") # response textbox disable

def send_text():
    """Accepts user input, submits the question to the agent, and returns the agent's response."""   
    # Get user input from ask textbok
    user_input = textbox_ask.get("1.0", tk.END)

    # Check if the ask textbox is not zero
    if len(user_input) != 0:
        textbox_result.config(state="normal") # Enable result textbox
        textbox_result.insert(tk.END, user_input + "\nWaiting...") # Enter user input to texbox
        
        textbox_result.config(state="disabled") # response textbox disable
        textbox_ask.delete("1.0", tk.END) # clear ask textbox

def new_session():
        """Reonse textbox will be clear."""
        textbox_result.config(state="normal") # Enable result textbox
        textbox_result.delete("1.0", tk.END) # clear result textbox
        textbox_result.config(state="disabled") # response textbox disable

# Create the main window
root = tk.Tk()
root.title("Color Agent")
root.geometry("1280x900")
root.configure(bg="white") #Configure the Main Window

# # 1. Create a frame to act as a structured column container
# layout_container = tk.Frame(root)
# layout_container.pack(pady=20, padx=20) # Apply the outer border margin HERE

# Create label
label_title = tk.Label(root, text="COLOR AGENT", font=("Arial", 25, "bold"), fg="red", background="white")
label_title.place(x=540, y=45)


label_title = tk.Label(root, text="Ask a question or start a conversation...", font=("Arial", 14, "italic"), fg="black", background="white")
label_title.place(x=95, y=700)

#***************************************************************  IMAGE LABELS  ************************************************************************

# Open the image file using Pillow
pil_image = Image.open(r"C:\Users\Jviloria\OneDrive - Konica Minolta\ドキュメント\MCU Python Course\Fall26_104\viloriaj1\Project\Color Agent\Images\color_agent.png")

# Optional: Resize the image if it's too big (width, height)
pil_image = pil_image.resize((100, 100)) 

# Convert the Pillow image into a Tkinter-compatible photo image
tk_image = ImageTk.PhotoImage(pil_image)

# Assign the image to a Label widget
image_label = tk.Label(root, image=tk_image, background="white")
image_label.place(x=425, y=10)

# CRITICAL STEP: Keep a reference to the image!
image_label.image = tk_image 

#***************************************************************************************************************************************************************8


# Create a Text widget: width is in characters, height is in lines of text
textbox_result = scrolledtext.ScrolledText(root, width=120, height=30, font=("Arial", 12))
textbox_result.place(x=95, y=130)
textbox_result.config(state="disabled", background="ivory") # result textbox configuracion

textbox_ask = scrolledtext.ScrolledText(root, width=87, height=5, font=("Arial", 12))
textbox_ask.place(x=95, y=735)
textbox_ask.config(background="ivory") # ask textbox configuracion

# Create button
button_send = tk.Button(root, text="Send", command=lambda: [send_text(), countdown(10)], width=16, height=5,bg="light cyan",activebackground="darkturquoise")
button_send.place(x=920, y=735)

button_new_session = tk.Button(root, text="New Session", command=lambda: new_session(), width=16, height=5, bg="light cyan", activebackground="darkturquoise")
button_new_session.place(x=1055, y=735)


# Start the application loop
root.mainloop()




