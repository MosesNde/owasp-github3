 csrf = CSRFProtect(app)
 
 app.config.update(
    # SESSION_COOKIE_SECURE = True,       # HTTPS 전용
     SESSION_COOKIE_HTTPONLY = True,     # JS 접근 차단
     SESSION_COOKIE_SAMESITE = "Lax",    # 필요하면 Strict
     PERMANENT_SESSION_LIFETIME = 3600,  # 1시간(필요에 맞게)