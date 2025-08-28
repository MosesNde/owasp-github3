     company.active = active == "on"
 
     await db.commit()
    return RedirectResponse(url=f"/dashboard?token={token}", status_code=HTTP_303_SEE_OTHER)
 
 
 