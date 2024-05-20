import sys
import argparse
import os.path

def main():
    parser = argparse.ArgumentParser(description='A copy of the command line tool cat.')
    parser.add_argument('filenames', type=str, nargs='*', help='accepts a filename to show the content from')
    parser.add_argument('-n', dest='mark_line_number', action='store_true', help='switch on/off line numbers along with the content to show')
    args = parser.parse_args()
    if len(args.filenames) == 0 or args.filenames[0] == '-':
        try:
            custom_print(sys.stdin, args.mark_line_number)
        except KeyboardInterrupt:
            pass
        return
    
    for path in args.filenames:
        if not os.path.exists(path):
            print(f'cccat: {path}: No such file or directory')
            continue
        read_file(path, args.mark_line_number)


def read_file(path,mark_line_number):
    with open(path, 'r') as file:
        custom_print(file, mark_line_number)
        
        
def custom_print(lines, mark_line_number):
    for i,line in enumerate(lines):
        print(line.rstrip() if not mark_line_number else f'{i+1} {line.rstrip()}')
            
if __name__ == '__main__':
    main()