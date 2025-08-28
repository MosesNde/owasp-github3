                     )
                     + column * CONFIG.WELL_SPACING_MM
                     + CONFIG.A1_X_MM
                    + CONFIG.WELLPLATE_OFFSET_X_mm
                 )
                 y_mm = (
                     CONFIG.Y_MM_384_WELLPLATE_UPPERLEFT
                     )
                     + row * CONFIG.WELL_SPACING_MM
                     + CONFIG.A1_Y_MM
                    + CONFIG.WELLPLATE_OFFSET_Y_mm
                 )
                 self.coordinates_mm.append((x_mm, y_mm))
                 self.name.append(chr(ord("A") + row) + str(column + 1))