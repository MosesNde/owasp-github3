 			User u = userservice.checkLogin(username, password);
 			if (u != null) {
 				HttpSession session = request.getSession();
				session.setAttribute("username", username);
 				response.sendRedirect(request.getContextPath() + "/");
 			} else {
 				request.setAttribute("errorMsg", "Sai tài khoản hoặc mật khẩu!!!");