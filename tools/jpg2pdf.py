from PIL import Image

def convert_jpg_to_pdf(image_paths, output_path):
    image_list = [Image.open(img).convert('RGB') for img in image_paths]
    image_list[0].save(output_path, save_all=True, append_images=image_list[1:])
