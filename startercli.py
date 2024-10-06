import click
import os
import subprocess

@click.command()
@click.argument('sitename')
def setup_new_site(sitename):
    """
    CLI to automate new Frappe site setup.
    Usage: new_site_cli.py sitename
    """
    try:
        # Step 1: Create new site
        click.echo(f"Creating new site: {sitename}")
        subprocess.run(['bench', 'new-site', sitename])

        # Step 2: Get starter apps from GitHub
        click.echo("Getting starter apps from GitHub")
        subprocess.run(['bench', 'get-app', 'https://github.com/aloolerp/webdoc'])
        subprocess.run(['bench', '--site', sitename, 'install-app', 'webdoc'])

        subprocess.run(['bench', 'get-app', 'https://github.com/aloolerp/webstarter'])
        subprocess.run(['bench', '--site', sitename, 'install-app', 'webstarter'])

        # Step 3: Install Frappe Types
        click.echo("Installing Frappe Types")
        subprocess.run(['bench', 'get-app', 'https://github.com/The-Commit-Company/frappe-types'])
        subprocess.run(['bench', '--site', sitename, 'install-app', 'frappe_types'])

        # Step 4: Set up Doppio
        click.echo("Setting up Doppio")
        subprocess.run(['bench', 'get-app', 'https://github.com/NagariaHussain/doppio'])
        subprocess.run(['bench', 'add-spa'])

        click.echo(f"Setup complete for site: {sitename}")

    except Exception as e:
        click.echo(f"Error during setup: {e}")


if __name__ == '__main__':
    setup_new_site()
