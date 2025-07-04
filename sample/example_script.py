import json

from PIL import Image
import numpy as np
import sys
import argparse
import logging

logging.basicConfig(level=logging.INFO)

def map_input_to_output(input_file_p, output_file_p, map_file_p):

    logging.info("Reading map file: {}".format(map_file_p))
    with open(map_file_p, newline='') as json_file:
        jsondata = json.load(json_file)

        assert "color_mapping" in jsondata.keys()

        # load the image
        logging.info("Reading input file: {}".format(input_file_p))
        im = Image.open(input_file_p)
        input_format = im.format
        im = im.convert('RGBA')
        npimg = np.array(im)

        red, green, blue, alpha = npimg.T  # Temporarily unpack the bands for readability

        for c1, c2 in jsondata['color_mapping'].items():
            logging.info("Processing color mapping: {} to {}".format(c1, c2))
            col1 = eval(c1)
            col2 = eval(c2)

            orig_color = (red == col1[0]) & (blue == col1[1]) & (green == col1[2])
            npimg[..., :-1][orig_color.T] = col2

        logging.info("Writing output file: {}".format(output_file_p))
        output_image = Image.fromarray(npimg)
        output_image.save(output_file_p, format=input_format)

def run_cli():

    parser = argparse.ArgumentParser(description='Example script for mappers')
    parser.add_argument('-i','--input', help='Input file as file path', required=True)
    parser.add_argument('-m', '--map', help='Map file as path or remote URI', required=True)
    parser.add_argument('-o', '--output', help='Path to output json file', required=True)

    args = parser.parse_args(sys.argv[1:])
    map_input_to_output(args.input, args.output, args.map)