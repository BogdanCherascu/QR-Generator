from fastapi import FastAPI, Response
import redis
import qrcode
import io

app = FastAPI()

cache = redis.Redis(host='redis_db', port=6379)

@app.get("/generate")
def generate_qr(url: str):
    cached_qr = cache.get(url)
    if cached_qr:
        print("Found in Redis.")
        return Response(content=cached_qr, media_type="image/png")
    
    print("Not found in cache, generating...")
    qr_img = qrcode.make(url)
    
    buf = io.BytesIO()
    qr_img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    
    cache.setex(url, 60, byte_im)
    
    return Response(content=byte_im, media_type="image/png")