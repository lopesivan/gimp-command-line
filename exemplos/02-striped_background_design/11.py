def activity_eleven(draw, image, layer):
    if 0:
        GY2 = float(image.height) * 1000 / 1618  # GY2 golden rules ...

        GX1 = float(image.width) * 382 / 1000    # golden rules ...
        GX2 = float(image.width) * 1000 / 1618   # golden rules ...

        X = GX1 * 1000 / 1618

        s_height = ( float(image.height) - GY2 ) * 1000 / 1618 \
                   - draw.STEP \
                   - 2 * int(draw.STEP)

        Y = GY2 + int(draw.STEP) + s_height / 2

        radius = (GX2 - GX1) / 2 - int(draw.STEP)

        draw.circle_selection(image, layer, X, Y, radius)

    draw.set_default_fg_bg()

    GX1 = float(image.width) * 382 / 1000    # golden rules ...
    GX2 = float(image.width) * 1000 / 1618   # golden rules ...

    radius = ((GX2 - GX1) / 2 ) * 2

    print ("diametro = %s" % radius)

    # load texture
    moon_texture_file_path = "/home/ivan/workspace/learning/learning-gimp/scripts/exemplos/python/02-striped_background_design/moon.png"

    moon_layer = draw.layer_texture(image, moon_texture_file_path, 132)

    pdb.gimp_desaturate_full(moon_layer, 0) # 0, 1, 2
    draw.set_softlight_opacity(moon_layer, 70)

    if 0:
        pdb.gimp_context_set_brush(draw.my_brush('myBrush', 1, 1))

        #draw a square around the image
        ctrlPoints = [X, Y,
                      X, Y
        ]

        pdb.gimp_paintbrush_default(layer, len(ctrlPoints), ctrlPoints)
        #pdb.gimp_pencil(layer, len(ctrlPoints), ctrlPoints)
        pdb.gimp_brush_delete('myBrush')

    if 0:
        # draw one
        pdb.gimp_context_set_brush('monsoonami splatter 2')

        #draw a square around the image
        ctrlPoints = [X - radius * (1 / random.randint(1, 10)), Y - radius * (1 / random.randint(1, 10))

        ]

        pdb.gimp_context_set_brush_size(7.1)
        pdb.gimp_paintbrush_default(layer, len(ctrlPoints), ctrlPoints)

        # draw two
        pdb.gimp_context_set_brush('monsoonami splatter 1')

        #draw a square around the image
        ctrlPoints = [X + radius * (1 / random.randint(1, 10)), Y + radius * (1 / random.randint(1, 10))

        ]

        pdb.gimp_context_set_brush_size(7.1)
        pdb.gimp_paintbrush_default(layer, len(ctrlPoints), ctrlPoints)

        #pdb.gimp_pencil(layer, len(ctrlPoints), ctrlPoints)
        #pdb.gimp_brush_delete('myBrush')

    if 0:
        # draw one
        pdb.gimp_context_set_brush('Bird')

        #draw a square around the image
        ctrlPoints = [X - radius * (1 / random.randint(1, 10)), Y - radius * (1 / random.randint(1, 10))

        ]

        pdb.gimp_context_set_brush_size(1000.2)
        pdb.gimp_paintbrush_default(layer, len(ctrlPoints), ctrlPoints)

        # draw two
        pdb.gimp_context_set_brush('Acrylic 03')
        #pdb.gimp_context_set_brush('monsoonami splatter 5')


        #draw a square around the image
        ctrlPoints = [X + radius * (1 / random.randint(1, 10)), Y + radius * (1 / random.randint(1, 10))

        ]

        pdb.gimp_context_set_brush_size(1000.2)
        pdb.gimp_paintbrush_default(layer, len(ctrlPoints), ctrlPoints)

        #pdb.gimp_pencil(layer, len(ctrlPoints), ctrlPoints)
        #pdb.gimp_brush_delete('myBrush')

    draw.set_softlight_opacity(layer, 38.6)
    pdb.gimp_selection_none(image)
