             UserViewModel user = UserService.getInstance().getUserByUserName(request.getParameter("username"));
             HttpSession session = request.getSession();
             UserViewModel currUser = (UserViewModel) session.getAttribute("admin");
            if(Objects.equals(currUser.getUsername(), user.getUsername())){
                if (session.getAttribute("admin") == null)
                    session.setAttribute("admin",user);
             }
         }
         ServletUtils.redirect(response, request.getContextPath() + "/admin/user/detail?userId=" + reqUpdate.getUserId() + error);