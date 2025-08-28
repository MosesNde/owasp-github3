 		String password = request.getParameter("admin-password");
 		
 		String filteredUsername = StringEscapeUtils.escapeHtml4(username);
		URLEncoder.encode(filteredUsername, "UTF-8");
 		
 		String filteredPassword = StringEscapeUtils.escapeHtml4(password);
		URLEncoder.encode(filteredPassword, "UTF-8");
 		Admin admin = new Admin();
 		admin.setName(request.getParameter("name"));
 		Admin admin_check = adminservice.checkAdminLogin(username, password);
 		try {
 			if (admin_check != null) {
 				HttpSession session = request.getSession();
				session.setAttribute("admin-username", filteredUsername);
				session.setAttribute("admin-password", filteredPassword);
 				response.sendRedirect(request.getContextPath() + "/admin/homepage");
 			} else {
 				request.setAttribute("errorMessage", "Tài khoản hoặc mật khẩu không chính xác !!!");