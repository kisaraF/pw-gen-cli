import click
import random, string


# Group chain of commands
@click.group()
def pw_gen():
    pass




@click.command()
def get_help():
    output_str = """
    Welcome to strong password generator!\n
    Characteristics of a good password:
    - Contains at least 10 characters
    - Contains upper case, lower case letters & numbers & symbols with a balanced mix\n
    """
    click.echo(output_str)


@click.command()
@click.option('--char_count', default=10, help='Number of characters for the password. Default would be 10')
# @click.argument('char_count')
def gen_password(char_count):
    master = []
    for i in range(round(char_count * 0.2)):
        master.append(random.randint(0,9))

    for j in range(round(char_count * 0.3)):
        master.append(string.ascii_lowercase[random.randint(0,len(string.ascii_lowercase)-1)])

    for k in range(round(char_count * 0.3)):
        master.append(string.ascii_uppercase[random.randint(0,len(string.ascii_uppercase)-1)])

    for l in range(round(char_count * 0.2)):
        master.append(string.punctuation[random.randint(0,len(string.punctuation)-1)])

    random.shuffle(master)
    pw_text = "".join([str(i) for i in master])

    output_str = f"""
    Your Password: {pw_text}
    Number of characters: {len(pw_text)}

    !!!Important!!!
    Save it to a Password Manager NOW
    """
    
    click.echo(output_str)


pw_gen.add_command(get_help)
pw_gen.add_command(gen_password)

if __name__ == "__main__":
    pw_gen()
