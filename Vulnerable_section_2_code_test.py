 
     # ----- VN Start -----
     ## Explaination: Split images into n^2 sub-images (comment if already done)
    split_all_images(input_folder = opt['datasets']['TD']['data_path'],
                     output_folder = opt['datasets']['TD']['split_path_ori'],
                     num_images = opt['datasets']['TD']['num_images'],
                     num_child_on_width_size = opt['datasets']['TD']['num_child_on_width_size'],
                     num_child_on_height_size = opt['datasets']['TD']['num_child_on_height_size'])
     # ----- VN End -----
 
     # Create train and val dataloader