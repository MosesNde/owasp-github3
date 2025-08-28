 import { Router } from 'express';
 import { StatusCodes } from 'http-status-codes';
 import twilio from 'twilio';
 
 import AuthenticationMiddleWare from '../authentication/authentication.middleware';
 import TwilioController from './twilio.controller';
         authenticationService, destinyService, userService, worldRepository,
     });
 
     twilioRouter.route('/destiny/r')
         .post(async (req, res, next) => await middleware.authenticateUser(req, res, next),
             async (req, res) => {
                     body,
                     cookies: requestCookies = {},
                 } = req;
 
                 // Reconstruct the URL using known, trusted components
                 const reconstructedUrl = `${process.env.PROTOCOL}://${process.env.DOMAIN}/twilio/destiny/r`;
 
                if (!validateRequest(authToken, header, reconstructedUrl, body)) {
                     res.writeHead(StatusCodes.FORBIDDEN);
 
                     return res.end();
                 }
 
                 const { cookies = {}, media, message } = await twilioController.request({
                    body,
                     cookies: requestCookies,
                 });
 
             } = req;
             const claimCheck = query['claim-check-number'];
             const notificationType = query['notification-type'];
 
            if (!validateRequest(authToken, header, `${process.env.PROTOCOL}://${process.env.DOMAIN}${originalUrl}`, body)) {
                 res.writeHead(StatusCodes.FORBIDDEN);
 
                 return res.end();
             }
 
             await twilioController.statusCallback({
                ...body,
                 ...(claimCheck && { ClaimCheck: claimCheck }),
                 ...(notificationType && { NotificationType: notificationType }),
             });