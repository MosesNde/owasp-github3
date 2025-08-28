 
     @NotEmpty(message = "Password should not be empty")
     @NotNull(message = "Password is mandatory")
    @Pattern(regexp = "^[a-z0-9_\\-\\.]+$", message = "password has illegal chars")
     @Size(min = 1, message = "password length should be between 1 - 127")
     @Size(max = 127, message = "password length should be between 1 - 127")
     String password;