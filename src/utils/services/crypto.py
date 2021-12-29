from PIL import Image


def hide_data_in_image_path_and_save(data: str, image_path: str) -> None:
    """
    Hides the given string into an image and saves it at the same location.

    :param data: the data to be hidden into the image
    :param image_path: the path of the image in which the data will be hidden
    """
    with Image.open(image_path, 'r') as img:
        new_img = hide_data_in_image(data, img)
        photo_full_name = image_path.split('/')[-1]
        photo_name, _ = photo_full_name.split('.')
        new_photo_name = photo_name + '-secret.png' 
        new_img.save(new_photo_name, 'png')


def extract_data_from_image_path(image_path: str) -> str:
    with Image.open(image_path, 'r') as image:
        data = extract_data_from_image(image)
        return data


def hide_data_in_image(data: str, image: Image) -> Image:
    """
    Hides the given data into the given image.

    :param data: the data to be hidden into the image
    :param image: the image in which the data will be hidden
    :returns: the image with the hidden data
    """
    new_image = image.copy()
    _encode_enc(new_image, data)
    return new_image


def extract_data_from_image(image: Image) -> str:
    """
    Retrieves hidden data from the given image.

    :param image: the image which contains the hidden data
    :returns: the extracted data
    """
    data = _decode_enc(image)
    return data


# ============ PRIVATE ============


def _encode_enc(image, data):
    binary_data = _convert_to_binary_data(data)
    data_index = 0
    for x in range(image.width):
        for y in range(image.height):
            if data_index >= len(binary_data):
                return
            
            pixel = image.getpixel((x , y))
            red, green, blue = pixel
            
            local_data = binary_data[data_index : data_index + 6]
            if len(local_data) < 6:
                local_data = (local_data + '0000000')[:6]
            data_index += 6

            red_data   = local_data[ :2]
            green_data = local_data[2:4]
            blue_data  = local_data[4:6]

            red   = (red   & 252) | int(red_data,   2)
            green = (green & 252) | int(green_data, 2)
            blue  = (blue  & 252) | int(blue_data,  2)

            new_pixel = red, green, blue
            image.putpixel((x, y), new_pixel)


def _convert_to_binary_data(data):
    # Converts the data to a binary format
    return ''.join([format(ord(i), '08b') for i in data] + ['00000000'])


def _decode_enc(image):
    binary_data = ''
    go = True
    for x in range(image.width):
        if not go:
            break
        for y in range(image.height):
            
            pixel = image.getpixel((x , y))
            red, green, blue = pixel

            red_data   = red   & 3
            green_data = green & 3
            blue_data  = blue  & 3

            if red_data + green_data + blue_data == 0:
                go = False
                break

            binary_data += format(red_data,   '02b')
            binary_data += format(green_data, '02b')
            binary_data += format(blue_data,  '02b')

    data = _convert_from_binary_data(binary_data)
    return data


def _convert_from_binary_data(binary_data):
    splits = [binary_data[i : i + 8] for i in range(0, len(binary_data), 8)]
    data = ''.join([chr(int(bytes, 2)) for bytes in splits])
    return data
