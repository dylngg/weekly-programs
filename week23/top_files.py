import os
import time
import argparse


def main(args):
    parser = argparse.ArgumentParser(description='Find the biggest files in a directory')
    parser.add_argument('-d', '--directory', help='Input for the working directory', required=True)
    parser.add_argument('-f', '--files', help='Input for the number of files to be displayed', required=True)
    args = parser.parse_args()

    working_dir = '/Users/dylngg'
    if args.directory:
        working_dir = str(args.directory)

    num_of_files = 10
    if args.files:
        num_of_files = int(args.files)

    start_time = time.time()
    files = {}
    for folder_names, subfolders, file_names in os.walk(working_dir):

        # get item size
        for item in file_names:
            path = os.path.join(folder_names, item)
            try:
                size = os.stat(path).st_size
                files[size] = path

            except:
                pass

    # create list of keys
    keys = list(files.keys())
    keys.sort()

    # get nth largest keys
    top_keys = keys[-num_of_files:]

    # print items
    print('Top ' + str(num_of_files) + ' Files (' + working_dir + '):')
    print('---------------------------------')
    [print(bytes_to_mb(key) + ' : ' + abs_to_rel_path(working_dir, files[key])) for key in top_keys]

    print('\nTime: ' + str(time.time() - start_time) + 's')


def bytes_to_mb(byte):
    mb = str(byte / 1000000)

    return mb[:5] + ' MB'


def abs_to_rel_path(working_dir, abs_path):
    rel_path = abs_path.replace(working_dir, '')

    return rel_path


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
