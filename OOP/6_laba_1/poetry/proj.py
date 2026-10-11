import click
import json
import os

DB_FILE = 'tasks.json'

def load_tasks():
    if not os.path.exists(DB_FILE):
        return []
    with open(DB_FILE, 'r') as f:
        return json.load(f)

def save_tasks(tasks):
    with open(DB_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

@click.group()
def cli():
    """Простий менеджер завдань на Python."""
    pass

@cli.command()
@click.argument('title')
def add(title):
    """Додати нове завдання."""
    tasks = load_tasks()
    tasks.append({"id": len(tasks) + 1, "title": title, "done": False})
    save_tasks(tasks)
    click.echo(f"✅ Завдання '{title}' додано!")

@cli.command()
def list():
    """Показати всі завдання."""
    tasks = load_tasks()
    if not tasks:
        click.echo("Список порожній.")
        return
    for t in tasks:
        status = "✔" if t['done'] else "✖"
        click.echo(f"{t['id']}. [{status}] {t['title']}")

@cli.command()
@click.argument('task_id', type=int)
def complete(task_id):
    """Позначити завдання як виконане."""
    tasks = load_tasks()
    for t in tasks:
        if t['id'] == task_id:
            t['done'] = True
            save_tasks(tasks)
            click.echo(f"👍 Завдання №{task_id} виконано!")
            return
    click.echo("Завдання не знайдено.")

if __name__ == '__main__':
    cli()