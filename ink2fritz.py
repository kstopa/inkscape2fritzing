#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "K. Stopa"
__copyright__ = "Copyright 2020"
__license__ = "LGPLv3"
__version__ = "1.0.0"

import argparse
import xml.etree.ElementTree as ET


def set_layer_ids(svg_path_in, svg_path_out):
    ET.register_namespace('', 'http://www.w3.org/2000/svg')
    ET.register_namespace('dc', 'http://purl.org/dc/elements/1.1/')
    ET.register_namespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
    ET.register_namespace('inkscape', 'http://www.inkscape.org/namespaces/inkscape')
    ET.register_namespace('sodipodi', 'http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd')
    print('Processing {}'.format(svg_path_in))
    doc = ET.parse(svg_path_in)
    svg = doc.getroot()
    # Get main layer
    for layer in svg.iter('{http://www.w3.org/2000/svg}g'):
        label = layer.attrib['{http://www.inkscape.org/namespaces/inkscape}label']
        if 'copper' in label or 'silkscreen' in label:
            print('Changing layer {0} ID from {0} to {1}'.format(layer.attrib['id'], label))
            layer.set('id', label)
    doc.write(svg_path_out)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A simple tool to set ID at SVG files based on layer name.')
    parser.add_argument('-i', '--input', help='Path to the SVG file to be processed.')
    parser.add_argument('-o', '--output', help='Path where a processed file will be stored.')
    args = parser.parse_args()
    set_layer_ids(args.input, args.output)
