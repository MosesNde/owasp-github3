         flowgaps = self.flow_dir[random_gap]
         vid = random.choice(flowgaps)
         flos = random.choice(vid)
         dataset_dict = {}
         dataset_dict["flow_dir"] = str(vid[0][0])
         fname = Path(flos[0]).stem
         gt_dir = (self.data_dir[2] / dname / fname).with_suffix('.png')
         flow_file_path = str(flos[0])
         number_str = flow_file_path.split('/')[-1].split('.')[0]
        if self.focus_series is not None:
            number_str = self.focus_series
         number_int = int(number_str)
         rgb_dir_list = str(rgb_dir).split('/')
         rgb_dir_list[-1] = f"{number_int:05d}.jpg"
                 rgb_big = F.interpolate(rgb_big[None], size=(1080, 1920), mode='bicubic').clamp(0., 255.)[0]
 
         # print('not here', rgb.min(), rgb.max())
        input = DT.AugInput(rgb)
 
         # Apply the augmentation:
        preprocessing_transforms = self.transforms(input)  # type: DT.Transform
        rgb = input.image
         if self.photometric_aug:
             rgb_aug = Image.fromarray(rgb.astype(np.uint8))
             rgb_aug = self.photometric_aug(rgb_aug)
         d2_utils.check_image_size(dataset_dict, flo0)
         if os.path.exists(gt_dir):
             sem_seg_gt = d2_utils.read_image(str(gt_dir))
            sem_seg_gt = preprocessing_transforms.apply_segmentation(sem_seg_gt)
             # sem_seg_gt = cv2.resize(sem_seg_gt, (self.resolution[1], self.resolution[0]), interpolation=cv2.INTER_NEAREST)
             if sem_seg_gt.ndim == 3:
                 sem_seg_gt = sem_seg_gt[:, :, 0]
 
         if os.path.exists(gt_dir):
             sem_seg_gt_ori = d2_utils.read_image(gt_dir)
            sem_seg_gt = preprocessing_transforms.apply_segmentation(sem_seg_gt_ori)
             if sem_seg_gt.ndim == 3:
                 sem_seg_gt = sem_seg_gt[:, :, 0]
                 sem_seg_gt_ori = sem_seg_gt_ori[:, :, 0]
         gwm_dir = (Path(str(self.data_dir[2]).replace('Annotations', 'gwm')) / dname / fname).with_suffix('.png')
         if gwm_dir.exists():
             gwm_seg_gt = d2_utils.read_image(str(gwm_dir))
            gwm_seg_gt = preprocessing_transforms.apply_segmentation(gwm_seg_gt)
             gwm_seg_gt = np.array(gwm_seg_gt)
             # gwm_seg_gt = cv2.resize(gwm_seg_gt, (self.resolution[1], self.resolution[0]), interpolation=cv2.INTER_NEAREST)
             if gwm_seg_gt.ndim == 3: