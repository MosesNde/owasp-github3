             customer_username = event["data"]["metadata"]["customer_username"]
 
     except (SignatureVerificationError, WebhookInvalidPayload) as e:
        return HttpResponse(e, status=400)
 
     logger.info(f"Received event: id={event.id}, type={event.type}")
     return HttpResponse("ok", status=200)