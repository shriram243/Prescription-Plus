import uvicorn

if __name__ == '__main__':
    uvicorn.run('app:app', host="127.0.0.1", port=5000, reload=True)
    # uvicorn.run('app:app', host="192.168.97.140", port=5000, reload=True)
