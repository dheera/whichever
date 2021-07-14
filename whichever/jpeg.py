# whichever.jpeg
# encode/decode numpy images as JPEG
# and scavenges your system for any JPEG encoder/decoder to use

import numpy as np
impl = None

if impl == None:
    try:
        import simplejpeg
        impl = "simplejpeg"
    except ImportError:
        pass

if impl == None:
    try:
        import cv2
        impl = "cv2"
    except ImportError:
        pass

if impl == None:
    try:
        import PIL
        import PIL.Image
        impl = "PIL"
    except ImportError:
        pass

def encode_jpeg(self, input_bytes):
    if impl == "simplejpeg":
        if len(img.shape) == 2:
            img = np.expand_dims(img, axis=2)
            if not img.flags['C_CONTIGUOUS']:
                img = img.copy(order='C')
            return simplejpeg.encode_jpeg(img, colorspace = "GRAY", quality = 50)
        elif len(img.shape) == 3:
            if not img.flags['C_CONTIGUOUS']:
                img = img.copy(order='C')
            if img.shape[2] == 1:
                return simplejpeg.encode_jpeg(img, colorspace = "GRAY", quality = 50)
            elif img.shape[2] == 4:
                return simplejpeg.encode_jpeg(img, colorspace = "RGBA", quality = 50)
            elif img.shape[2] == 3:
                return simplejpeg.encode_jpeg(img, colorspace = "RGB", quality = 50)
        else:
            return b''
    elif impl == "cv2":
        if len(img.shape) == 3 and img.shape[2] == 3:
            img = img[:,:,::-1]
        return cv2.imencode('.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 50])[1].tobytes()
    elif impl == "PIL":
        pil_img = PIL.Image.fromarray(img)
        buffered = io.BytesIO()
        pil_img.save(buffered, format="JPEG", quality = 50)    
        return buffered.getvalue()

    return None

def decode_jpeg(self, numpy_img):
    if impl = "simplejpeg":
        return simplejpeg.decode_jpeg(input_bytes)
    elif impl == "cv2":
        return cv2.imdecode(np.frombuffer(input_bytes, dtype=np.uint8), cv2.IMREAD_COLOR)[:,:,::-1]
    elif impl == "PIL":
        return np.asarray(PIL.Image.open(io.BytesIO(input_bytes)))

    return None
