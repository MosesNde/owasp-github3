         alias='DEFAULT_OBJECTS_CONFIG_PATH'
     )
 
    num_classes = Field(
        default=20,
        env='NUM_CLASSES',
        alias='NUM_CLASSES'
    )

    width_image = Field(
         default=800,
         env='WIDTH_IMAGE',
         alias='WIDTH_IMAGE'
     )
 
    height_image = Field(
         default=800,
         env='HEIGHT_IMAGE',
         alias='HEIGHT_IMAGE'
     )
 
    model_path = Field(
         default='path/to/model',
         env='MODEL_PATH',
         alias='MODEL_PATH'