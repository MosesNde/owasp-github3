                 getRequest().setAttribute(name, value);
                 break;
             }
            case SESSION_SCOPE: {
                getSession(true).setAttribute(name, value);
                break;
            }
             case APPLICATION_SCOPE: {
                 getServletContext().setAttribute(name, value);
                 break;