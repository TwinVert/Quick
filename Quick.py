import tkinter as tk
import base64

# Function to encode the user's input string to base64
def perform_encode_base64():
    plaintext = plaintext_entry.get()  # Get the user's input
    encoded_data = base64.b64encode(plaintext.encode('utf-8'))  # Encode the string to base64
    encoded_str = str(encoded_data, 'utf-8')
    encoded_text.set(encoded_str)  # Display the encoded string

# Function to decode base64 back to normal string
def perform_decode_base64():
    encoded_str = encoded_text.get()  # Get the encoded string
    padding_needed = len(encoded_str) % 4
    if padding_needed:
        encoded_str += "="* (4 - padding_needed)
    try:
        decoded_data = base64.b64decode(encoded_str)  # Decode the string from base64
        decoded_str = str(decoded_data, 'utf-8')
        decoded_text.set(decoded_str)  # Display the decoded string
    except UnicodeDecodeError:
        decoded_text.set("Unable to decode. The input string might not be valid base64 or the original string might not be utf-8.")

# Function to copy the encoded string to clipboard
def copy_encoded_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(encoded_text.get())

# Function to copy the decoded string to clipboard
def copy_decoded_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(decoded_text.get())

# Set up the main tkinter window
root = tk.Tk()
root.title('Base64 Encoder & Decoder')

# Set window size to user's screen size
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f'{screen_width}x{screen_height}')  # Adjust window size to fit the screen

main_frame = tk.Frame(root)
main_frame.pack(padx=10, pady=10)

# Set up the user interface
tk.Label(main_frame, text="Input your string:").pack()
plaintext_entry = tk.Entry(main_frame, width=50)
plaintext_entry.pack(pady=5)

encode_button = tk.Button(main_frame, text="Encode Base64", command=perform_encode_base64)
encode_button.pack(pady=5)

encoded_text = tk.StringVar()
tk.Label(main_frame, text="Encoded string:").pack()
encoded_label = tk.Label(main_frame, textvariable=encoded_text)
encoded_label.pack(pady=5)

copy_encoded_button = tk.Button(main_frame, text="Copy Encoded", command=copy_encoded_to_clipboard)
copy_encoded_button.pack(pady=5)

decode_button = tk.Button(main_frame, text="Decode Base64", command=perform_decode_base64)
decode_button.pack(pady=5)

decoded_text = tk.StringVar()
tk.Label(main_frame, text="Decoded string:").pack()
decoded_label = tk.Label(main_frame, textvariable=decoded_text)
decoded_label.pack(pady=5)

copy_decoded_button = tk.Button(main_frame, text="Copy Decoded", command=copy_decoded_to_clipboard)
copy_decoded_button.pack(pady=5)

root.mainloop()  # Run the tkinter event loop