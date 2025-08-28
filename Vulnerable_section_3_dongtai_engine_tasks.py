     if method_pool is None:
         method_pool = json.loads(method_pool_model.method_pool
                                  ) if method_pool_model.method_pool else []
     engine = VulEngine()
     engine.search(method_pool=method_pool,
                   vul_method_signature=strategy.get('value'))
             for strategy in strategies:
                 if strategy.get('value') in engine.method_pool_signatures:
                     search_and_save_vul(engine, method_pool_model, None, strategy)
        logger.info(f'漏洞检测成功')
         from dongtai_engine.plugins.method_pool import method_pool_after_scan, enable_method_pool_post_scan_hook
         if method_pool_model and enable_method_pool_post_scan_hook(method_pool_model):
             method_pool_after_scan(method_pool_model)