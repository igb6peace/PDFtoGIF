from pdf2image import convert_from_path
from PIL import Image
import os


pdf_dir = 'rk'
output_dir = pdf_dir


pdf_files = [f for f in os.listdir(pdf_dir) if f.endswith('.pdf')]


for pdf_file in pdf_files:
    
    pdf_path = os.path.join(pdf_dir, pdf_file)
    
    output_gif_path = os.path.join(output_dir, os.path.splitext(pdf_file)[0] + '.gif')
    
    
    images = convert_from_path(pdf_path)
    
   
    if images:
        images[0].save(output_gif_path, save_all=True, append_images=images[1:], optimize=False, duration=500, loop=0)
        print(f"GIF has been generated.: {output_gif_path}")
    else:
        print(f"No: {pdf_file}")

print("Conversion Complete")
