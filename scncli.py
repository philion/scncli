import click

@click.group()
def scncli():
    pass

@scncli.command()
def cmd1():
    '''Command on scncli'''
    click.echo('scncli cmd1')

@scncli.command()
def cmd2():
    '''Command on scncli'''
    click.echo('scncli cmd2')

if __name__ == '__main__':
    scncli()
