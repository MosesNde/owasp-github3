 
     # Get the latest processed date from the run context
     # This enables backfilling if needed
    # Access config correctly from the nested structure
    config = context.op_config if hasattr(context, "op_config") else {}
    from_date_str = config.get("from_date")
    to_date_str = config.get("to_date")
     from_date = None
     to_date = None
 