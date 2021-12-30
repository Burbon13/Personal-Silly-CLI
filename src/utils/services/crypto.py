from PIL import Image
from random import randrange

# ============ CRYPTO ============


def xor_strings(string, secret):
    if len(string) != len(secret):
        raise Exception('Lenghts of params string and secret must be equal')
    if isinstance(string, str):
        return "".join(chr(ord(a) ^ ord(b)) for a, b in zip(string, secret))
    else:
        return bytes([a ^ b for a, b in zip(string, secret)])


xor_strings('ahaha fsdf dsuhnfsdsdfsd', 'ahaha fsdf dsuhnfsdsdfsd')

# ============ STEGANOGRAPHY ============


def hide_xored_data_in_image_path_and_save(data: str, image_path: str, secret: str) -> None:
    """
    Hides the given string xored into an image and saves it at the same location.

    :param data: the data to be hidden into the image
    :param image_path: the path of the image in which the data will be hidden
    :param secret: the secret with which the string will be xored
    """
    secret = _enlarge_secret(secret, len(data))
    data = xor_strings(data, secret)
    with Image.open(image_path, 'r') as img:
        new_img = hide_data_in_image(data, img)
        new_photo_name = _new_file_path_extended(image_path, 'xored-secret', 'png')
        new_img.save(new_photo_name, 'png')


def extract_xored_data_from_image_path(image_path: str, secret: str) -> str:
    """
    Retrieves hidden data from the given image path.

    :param image: where the image resides
    :param secret: secret used to xor(decrypt) the text
    :returns: the extracted data
    """
    with Image.open(image_path, 'r') as image:
        data = extract_data_from_image(image)
        secret = _enlarge_secret(secret, len(data))
        data = xor_strings(data, secret)
        return data


def hide_data_in_image_path_and_save(data: str, image_path: str) -> None:
    """
    Hides the given string into an image and saves it at the same location.

    :param data: the data to be hidden into the image
    :param image_path: the path of the image in which the data will be hidden
    """
    with Image.open(image_path, 'r') as img:
        new_img = hide_data_in_image(data, img)
        new_photo_name = _new_file_path_extended(image_path, 'secret', 'png')
        new_img.save(new_photo_name, 'png')


def extract_data_from_image_path(image_path: str) -> str:
    """
    Retrieves hidden data from the given image path.

    :param image: where the image resides
    :returns: the extracted data
    """
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


def _new_file_path_extended(file_path: str, extra_part: str, extension: str):
    """
    Example: 
    file_path = './f1/f2/img.ext'
    extra_part = 'extr'
    extension = 'newext'

    --->>> result = './f1/f2/img-extr.newext'
    """
    splits = file_path.split('/')
    splits, file = splits[:-1], splits[-1]
    file_wo_extension = file.split('.')[0]
    new_file_name = f'{file_wo_extension}-{extra_part}.{extension}'
    splits.append(new_file_name)
    new_path = '/'.join(splits)
    return new_path


def _encode_enc(image, data):
    binary_data = _convert_to_binary_data(data)
    data_index = 0
    for x in range(image.width):
        for y in range(image.height):
            if data_index >= len(binary_data):
                return
            
            pixel = image.getpixel((x , y))
            red, green, blue = pixel
            
            local_data = binary_data[data_index : data_index + 4]
            data_index += 4

            red_data   = local_data[ :2]
            green_data = local_data[2:4]
            blue_data  = randrange(3) if data_index < len(binary_data) else 3

            red   = (red   & 252) | int(red_data,   2)
            green = (green & 252) | int(green_data, 2)
            blue  = (blue  & 252) | blue_data

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

            binary_data += format(red_data,   '02b')
            binary_data += format(green_data, '02b')
            if blue_data == 3:
                go = False
                break

    data = _convert_from_binary_data(binary_data)
    return data


def _convert_from_binary_data(binary_data):
    splits = [binary_data[i : i + 8] for i in range(0, len(binary_data), 8)]
    data = ''.join([chr(int(bytes, 2)) for bytes in splits])
    return data


def _enlarge_secret(secret: str, length: int) -> str:
    return (secret * (length // len(secret) + 1))[:length]
