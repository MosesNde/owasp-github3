                     if writer:
                         flow = torch.stack([x['flow'].to(model.device) for x in sample]).clip(-20, 20)
                         image_viz, header_text = get_unsup_image_viz(model, cfg, sample, criterion)
                        header = get_vis_header(image_viz.size(2), cfg.VISUAILZIE.RESOLUTION[1], header_text)
                         image_viz = torch.cat([header, image_viz], dim=1)
                         writer.add_image('train/images', image_viz, iteration + 1)
                     if cfg.WANDB.ENABLE and (iteration + 1) % 2500 == 0: