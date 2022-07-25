import uvicorn

if __name__ == '__main__':
    uvicorn.run('app:app', host="172.29.204.211", port=5000, reload=True)