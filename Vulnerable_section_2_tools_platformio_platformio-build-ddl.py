 
         board._manifest["build"]["boot_mode"] = boot_mode
         sys.stderr.write("Warning: you appear to be using legacy option 'build.ld_args.boot_mode'! Use 'build.boot_mode' instead.\n")
        
 
def get_ld_args() -> dict:
     """
     Get linker script parameters from the board manifest
 
    :return: dict with flash_start, flash_size and boot_mode
     """
 
     apply_legacy_ld_args()
         raise ValueError("flash_start is 0, but boot_mode is not 1 (primary)! This is not allowed, as a bootloader is required to use primary boot mode!")
 
     # print linker parameters
    print(f"linker parameters: FLASH_START={flash_start}, FLASH_SIZE={flash_size}; BOOT_MODE={boot_mode}; usable flash size: {flash_size_usable}")
    return {
        flash_start: flash_start,
        flash_size: flash_size,
        boot_mode: boot_mode,
    }
 
 def preprocess_ld_script():
     """
         ld_preprocess_args = [
             *[f"-D {d}" for d in ld_args_defines],
         ]
         ld_preprocess = env.Command(
             ld_script_target,
             ld_script_source,
 	    "ARM_MATH_CM4",
 	    "ARM_MATH_MATRIX_CHECK",
 	    "ARM_MATH_ROUNDING",
        ('__SOURCE_FILE_NAME__', '\\"${SOURCE.file}\\"') # add the source file name to the defines, so it can be used in the code
     ],
 
     # c/c++ include paths