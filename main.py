import uvicorn

if __name__ == '__main__':
    uvicorn.run('app:app', host="192.168.1.3", port=5000, reload=True)
