             return;
 		}
 		String filteredUsername = StringEscapeUtils.escapeHtml4(username);
		URLEncoder.encode(filteredUsername, "UTF-8");
 		
 		String filteredPassword = StringEscapeUtils.escapeHtml4(password);
		URLEncoder.encode(filteredPassword, "UTF-8");
 		try {
 			User u = userservice.checkLogin(username, password);
 			if (u != null) {
 				HttpSession session = request.getSession();
				session.setAttribute("username", filteredUsername);
 				response.sendRedirect(request.getContextPath() + "/");
 			} else {
 				request.setAttribute("errorMsg", "Sai tài khoản hoặc mật khẩu!!!");