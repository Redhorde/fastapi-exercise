#!/usr/bin/env python3
import uvicorn


def main():
    uvicorn.run('fastapi_app:app', reload=True)


if __name__ == '__main__':
    main()
