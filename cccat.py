import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description='A copy of the command line tool cat.')
    parser.add_argument('filenames', type=str, nargs='*', help='the files to read')
    parser.add_argument('-n', action='store_true', help='number all output lines')
    parser.add_argument('-b', action='store_true', help='number non-blank output lines')
    args = parser.parse_args()
    
    mark_non_blank_lines = args.b
    mark_line_number = args.n or mark_non_blank_lines
        
    if len(args.filenames) == 0 or args.filenames[0] == '-':
        try:
            custom_print(sys.stdin, mark_line_number, mark_non_blank_lines)
        except KeyboardInterrupt:
            print('')
            sys.exit(0)
        return
    
    for path in args.filenames:
        read_file(path, mark_line_number, mark_non_blank_lines)


def read_file(path, mark_line_number, mark_non_blank_lines):
    try:
        with open(path, 'r') as file:
            custom_print(file, mark_line_number, mark_non_blank_lines)
    except FileNotFoundError:
        print(f'cccat: {path}: No such file or directory')
    except IOError as e:
        print(f'cccat: {path}: I/O error({e.errno}): {e.strerror}')
        
        
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