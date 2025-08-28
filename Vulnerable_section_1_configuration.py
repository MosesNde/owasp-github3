 
 # Training settings
 BATCH_SIZE = 32
ITERS = 1200
 WORKERS = 4
 PRINT_FREQ = 200  # PRINTING FREQUENCY (fixed typo)
 GRAD_CLIP = None
 WEIGHT_DECAY = 5e-4  # Fixed typo
 
 # Learning rate schedule
DECAY_LR_AT = [800, 1000]  # DECAY LEARNING RATE AT THESE ITERATIONS (fixed typo and renamed for clarity)
 DECAY_LR_COEFF = 0.1  # Fixed typo
\ No newline at end of file