 
         dataset_dict = {}
         flow_dir = Path(self.data_dir[0]) / self.samples[idx]
         fid = self.samples_fid[str(flow_dir.parent)][flow_dir]
         flo_ori, h, w = read_flow(str(flow_dir), self.resolution, self.to_rgb)
         flo = einops.rearrange(flo_ori, 'c h w -> h w c')
         dataset_dict["gap"] = 'gap1'
        number = str(flow_dir).split('/')[-1].split('.')[0]
         
         # print(str(flos[0])) #../data/DAVIS2016/Flows_gap1/480p/bear/00006.flo
         # traj path should be ../data/DAVIS2016/Traj/480p/bear_tracks.npy
 
         rgb = d2_utils.read_image(str(rgb_dir)).astype(np.float32)
         original_rgb = torch.as_tensor(np.ascontiguousarray(np.transpose(rgb, (2, 0, 1)).clip(0., 255.))).float()
        if self.read_big:
            rgb_big = d2_utils.read_image(str(rgb_dir).replace('480p', '1080p')).astype(np.float32)
            rgb_big = (torch.as_tensor(np.ascontiguousarray(rgb_big))[:, :, :3]).permute(2, 0, 1).clamp(0., 255.)
            if self.force1080p_transforms is not None:
                rgb_big = F.interpolate(rgb_big[None], size=(1080, 1920), mode='bicubic').clamp(0., 255.)[0]

        input = DT.AugInput(rgb)
 
         # Apply the augmentation:
        preprocessing_transforms = self.transforms(input)  # type: DT.Transform
        rgb = input.image
         rgb = np.transpose(rgb, (2, 0, 1))
         rgb = rgb.clip(0., 255.)
         d2_utils.check_image_size(dataset_dict, flo)
 
         if os.path.exists(gt_dir):
             sem_seg_gt_ori = d2_utils.read_image(gt_dir)
            sem_seg_gt = preprocessing_transforms.apply_segmentation(sem_seg_gt_ori)
             if sem_seg_gt.ndim == 3:
                 sem_seg_gt = sem_seg_gt[:, :, 0]
                 sem_seg_gt_ori = sem_seg_gt_ori[:, :, 0]
         gwm_dir = (Path(str(self.data_dir[2]).replace('Annotations', 'gwm')) / self.samples[idx]).with_suffix(
             '.png')
         if gwm_dir.exists():
            gwm_seg_gt = preprocessing_transforms.apply_segmentation(d2_utils.read_image(str(gwm_dir)))
             gwm_seg_gt = np.array(gwm_seg_gt)
             if gwm_seg_gt.ndim == 3:
                 gwm_seg_gt = gwm_seg_gt[:, :, 0]