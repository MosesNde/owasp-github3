                 .antMatchers("/api/v1/user/**").hasAuthority("ADMIN")
 //                STUDENT ENDPOINT
                 .antMatchers(HttpMethod.GET, "/api/v1/student").permitAll()
                .antMatchers(HttpMethod.DELETE, "/api/v1/student").hasAuthority("ADMIN")
                 .antMatchers("/api/v1/student/**").hasAnyAuthority("ADMIN", "STUDENT")
 //                TEACHER ENDPOINT
                 .antMatchers(HttpMethod.GET, "/api/v1/teacher").permitAll()
                .antMatchers(HttpMethod.DELETE, "/api/v1/teacher").hasAuthority("ADMIN")
                 .antMatchers("/api/v1/teacher/**").hasAnyAuthority("ADMIN", "TEACHER")
 //                SUBJECT ENDPOINT
                 .antMatchers(HttpMethod.GET, "/api/v1/subject").permitAll()