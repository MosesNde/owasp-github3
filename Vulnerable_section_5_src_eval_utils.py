         image_viz: image visualization
         header_text: header text
     '''
    h ,w = cfg.VISUAILZIE.RESOLUTION
     masks_pred = torch.stack([x['sem_seg'] for x in preds], 0)
     masks_softmaxed = torch.softmax(masks_pred, dim=1)
     image_vizs = []
         frame_mean_iou = np.nanmean(list(seq_scores.values())) * 100
 
     if writer:
        header = get_vis_header(images_viz[0].size(2), cfg.VISUAILZIE.RESOLUTION[1], header_text)
        print("image_viz size", len(images_viz))
        print("header shape", header.shape)
         # print("header_text", header_text) #header_text ['rgb', 'gt_flow', 'gt_seg', 'pred_seg', 'rec_flow', 'slot', 'slot', 'slot', 'slot']
         images_viz = torch.cat(images_viz, dim=1)
         images_viz = torch.cat([header, images_viz], dim=1)