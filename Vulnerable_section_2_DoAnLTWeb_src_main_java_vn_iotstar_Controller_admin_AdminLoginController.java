 		try {
 			if (admin_check != null) {
 				HttpSession session = request.getSession();
				session.setAttribute("admin-username", username);
				session.setAttribute("admin-password", password);
 				response.sendRedirect(request.getContextPath() + "/admin/homepage");
 			} else {
 				request.setAttribute("errorMessage", "Tài khoản hoặc mật khẩu không chính xác !!!");