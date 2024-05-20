import sys
import argparse
import os.path

def main():
    parser = argparse.ArgumentParser(description='A copy of the command line tool cat.')
    parser.add_argument('filenames', type=str, nargs='*', help='accepts a filename to show the content from')
    parser.add_argument('-n', dest='mark_line_number', action='store_true', help='switch on/off line numbers along with the content to show')
    parser.add_argument('-b', dest='mark_non_blank_lines', action='store_true', help='mark line numbers along with non-blank lines only')
    args = parser.parse_args()
    
    mark_non_blank_lines = args.mark_non_blank_lines
    mark_line_number = args.mark_line_number or mark_non_blank_lines
        
    if len(args.filenames) == 0 or args.filenames[0] == '-':
        try:
            custom_print(sys.stdin, mark_line_number, mark_non_blank_lines)
        except KeyboardInterrupt:
            print('')
            sys.exit(0)
        return
    
    for path in args.filenames:
        if not os.path.exists(path):
            print(f'cccat: {path}: No such file or directory')
            continue
        read_file(path, mark_line_number, mark_non_blank_lines)


def read_file(path, mark_line_number, mark_non_blank_lines):
    with open(path, 'r') as file:
        custom_print(file, mark_line_number, mark_non_blank_lines)
        
        
def custom_print(lines, mark_line_number, mark_non_blank_lines):
    count = 1
    for line in lines:
        l = line.rstrip()
        if not mark_line_number or (l.strip() == '' and mark_non_blank_lines):
            print(l)
        else:
             print(f'{count} {l}')
             count += 1
       
            
if __name__ == '__main__':
    main()