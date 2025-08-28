     }
 
     @ExceptionHandler(BussinesLogicException.class)
    public ResponseEntity<String> handleBussinesLogic(BussinesLogicException exception) {
        return new ResponseEntity<>(exception.getMessage(), HttpStatus.NOT_ACCEPTABLE);
     }
 }