                                     checkNotNull(dataEntity, "given_name", registrationEntity.getGiven_name());
                                     checkNotNull(dataEntity, "family_name", registrationEntity.getFamily_name());
                                     checkNotNull(dataEntity, "mobile_number", registrationEntity.getMobile_number());
                                    checkNotNull(dataEntity, "password", registrationEntity.getPassword());
                                     checkNotNull(dataEntity, "username", registrationEntity.getUsername());
                                     checkNotNull(dataEntity, "birthdate", registrationEntity.getBirthdate().toString());
 
                                     if (dataEntity.getFieldKey().equals("password_echo")) {
                                         if (dataEntity.isRequired() && registrationEntity.getPassword_echo().equals("")) {