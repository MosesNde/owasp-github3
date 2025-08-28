         img_GT = util.read_img(None, osp.join(parent_path_GT, f"{index}.png"))
         img_GT = img_GT[:, :, [2, 1, 0]]
         img_GT = torch.from_numpy(np.ascontiguousarray(np.transpose(img_GT, (2, 0, 1)))).float().unsqueeze(0)
        img_GT = torch.nn.functional.interpolate(img_GT, size=(512, 512), mode='nearest', align_corners=None)
 
         T, C, W, H = img_GT.shape
         list_h = []
             }
     
     def __len__(self):
        return len(self.image_list_gt * 36)  