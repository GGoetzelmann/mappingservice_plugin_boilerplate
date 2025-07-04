from PIL import Image
import numpy as np
import csv
import sys
import argparse
import logging

logging.basicConfig(level=logging.INFO)

def map_input_to_output(input_file_p, output_file_p, map_file_p):

    logging.info("Reading map file: {}".format(map_file_p))
    with open(map_file_p, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter='\t', quotechar='"')


        # load the image
        logging.info("Reading input file: {}".format(input_file_p))
        im = Image.open(input_file_p)
        im = im.convert('RGBA')
        npimg = np.array(im)

        red, green, blue, alpha = npimg.T  # Temporarily unpack the bands for readability

        for row in csvreader:
            logging.info("Processing color mapping: {}".format(row))
            col1 = eval(row[0])
            col2 = eval(row[1])

            # Replace white with red... (leaves alpha values alone...)
            orig_color = (red == col1[0]) & (blue == col1[1]) & (green == col1[2])
            npimg[..., :-1][orig_color.T] = col2

        logging.info("Writing output file: {}".format(output_file_p))
        output_image = Image.fromarray(npimg)
        output_image.save(output_file_p)

def run_cli():

    parser = argparse.ArgumentParser(description='Example script for mappers')
    parser.add_argument('-i','--input', help='Input file as file path', required=True)
    parser.add_argument('-m', '--map', help='Map file as path or remote URI', required=True)
    parser.add_argument('-o', '--output', help='Path to output json file', required=True)

    args = parser.parse_args(sys.argv[1:])
    map_input_to_output(args.input, args.output, args.map)