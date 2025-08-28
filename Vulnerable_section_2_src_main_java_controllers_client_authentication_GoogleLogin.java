                 }
                 else {
                     HttpSession session = request.getSession();
                    if (session.getAttribute("user")== null)
                        session.setAttribute("user", user);
                     ServletUtils.redirect(response, request.getContextPath() + "/home");
                 }
             }