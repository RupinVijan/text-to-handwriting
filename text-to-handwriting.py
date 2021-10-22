import pywhatkit as kit 
import os


a=input("Enter Text You Want to change into Handwritten text :: \n")


kit.text_to_handwriting(a,save_to = "sampleoutput.png")


os.startfile("sampleoutput.png")


print("/n Your text is converted to handwritten text successfully.")

