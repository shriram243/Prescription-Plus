import uvicorn

if __name__ == '__main__':
    uvicorn.run('app:app', host="172.29.200.190", port=5000, reload=True)
    # uvicorn.run('app:app', host="172.29.195.37", port=5000, reload=True)
