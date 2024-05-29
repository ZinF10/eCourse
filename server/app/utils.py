from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url


def upload_image(image):
    if image:
        response = upload(image)
        avatar_url, options = cloudinary_url(response['public_id'], format=response['format'])
        return avatar_url
    return None
