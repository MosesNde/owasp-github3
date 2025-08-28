         @app.get("/file={path_or_url:path}", dependencies=[Depends(login_check)])
         async def file(path_or_url: str, request: fastapi.Request):
             blocks = app.get_blocks()
            if utils.validate_url(path_or_url):
                 return RedirectResponse(
                     url=path_or_url, status_code=status.HTTP_302_FOUND
                 )