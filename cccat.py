import sys
import click

@click.command()
@click.option('-n', "mark_line_number", is_flag=True, help='number all output lines')
@click.option('-b', "mark_non_blank_lines", is_flag=True, help='number non-blank output lines')
@click.argument('filenames', type=click.STRING, nargs=-1)
def cccat(filenames, mark_line_number, mark_non_blank_lines):
    mark_line_number = mark_line_number or mark_non_blank_lines
        
    if len(filenames) == 0 or filenames[0] == '-':
        try:
            custom_print(sys.stdin, mark_line_number, mark_non_blank_lines)
        except KeyboardInterrupt:
            click.echo()
            sys.exit(0)
        return
    
    for path in filenames:
        read_file(path, mark_line_number, mark_non_blank_lines)


def read_file(path, mark_line_number, mark_non_blank_lines):
    try:
        with open(path, 'r') as file:
            custom_print(file, mark_line_number, mark_non_blank_lines)
    except FileNotFoundError:
        click.echo(f'cccat: {path}: No such file or directory')
    except IOError as e:
        click.echo(f'cccat: {path}: I/O error({e.errno}): {e.strerror}')
        
        
def custom_print(lines, mark_line_number, mark_non_blank_lines):
    count = 1
    for line in lines:
        l = line.rstrip()
        if not mark_line_number or (l.strip() == '' and mark_non_blank_lines):
            click.echo(l)
        else:
             click.echo(f'{count} {l}')
             count += 1
       
            
if __name__ == '__main__':
    cccat()