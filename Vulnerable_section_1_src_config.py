 
 
 def add_gwm_config(cfg):
    cfg.VISUAILZIE = CN()
    cfg.VISUAILZIE.RESOLUTION = (96, 160)
     cfg.EMA = CN()
     cfg.EMA.WARMUP_ITER = 1500
     cfg.EMA.UPDATE_INTERVAL = 10