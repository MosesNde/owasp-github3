                 private void checkNotNull(RegistrationSetupResultDataEntity dataEntity, String key, String registrationEntityValue) {
                     if (dataEntity.getFieldKey().equals(key)
                             && dataEntity.isRequired()
                            && registrationEntityValue.equals("")) {
                         String errorMessage = key + " must not be empty";
                         registerFieldsresult.failure(WebAuthError.getShared(context).propertyMissingException(errorMessage, methodName));
                     }