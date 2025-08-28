 def handler(event, context):
 
     def cfn_error(message=None):
        logger.error("| cfn_error: %s" % message)
         cfn_send(event, context, CFN_FAILED, reason=message, physicalResourceId=event.get('PhysicalResourceId', None))
 
 
             physical_id = "aws.cdk.s3deployment.%s" % str(uuid4())
         else:
             if not physical_id:
                cfn_error("invalid request: request type is '%s' but 'PhysicalResourceId' is not defined" % {request_type})
                 return
 
         # delete or create/update (only if "retain_on_delete" is false)