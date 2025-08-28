         }else{
             UserViewModel user = UserService.getInstance().getUserByUserName(request.getParameter("username"));
             HttpSession session = request.getSession();
            if (session.getAttribute("user")== null)
                session.setAttribute("user",user);
             request.setAttribute("user", user);
         }
 